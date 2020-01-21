
import pandas as pd
import numpy as np
# Importing the dataset
dataset = pd.read_csv('wiki_movie_plots_deduped.csv')
plot = dataset['Plot'][0]
genre = dataset['Genre']
import re
plot = re.sub('[^a-zA-Z]', ' ',plot)

import nltk
nltk.download('stopwords')
plot = plot.lower()
plot = plot.split()
notstopwords = ['not']

from nltk.corpus import stopwords

corpus = []
mybag= []    
for data in plot:
    if(data not in stopwords.words('english')):
        mybag.append(data)

mystembag = []

from nltk.stem.porter import PorterStemmer

for data in mybag:
    ps = PorterStemmer()
    stemdata = ps.stem(data)
    if stemdata not in mystembag:
        mystembag.append(stemdata)


plot = ' '.join(mystembag)   
corpus.append(plot)




#corups is collection of all steem revies...
from sklearn.feature_extraction.text  import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset['Genre'].values


#classification
#randomforest


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)
#X_test = sc.transform(X_test)


# Fitting Random Forest Classification to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier.fit(X, y)

# Predicting the Test set results
X_test=input()
X_test = re.sub('[^a-zA-Z]', ' ',X_test)
X_test = X_test.lower()
X_test = X_test.split()

corpus2 = []
mybag2= []    
for data in X_test:
    if(data not in stopwords.words('english')):
        mybag2.append(data)

mystembag2 = []

for data in mybag2:
    ps = PorterStemmer()
    stemdata2 = ps.stem(data)
    if stemdata2 not in mystembag2:
        mystembag2.append(stemdata2)


X_test = ' '.join(mystembag2)   
corpus2.append(X_test)

X_test = cv.fit_transform(corpus).toarray()
X_test = sc.transform(X_test)

y_pred = classifier.predict(X_test)
#dt
#logi