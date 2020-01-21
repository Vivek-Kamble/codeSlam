
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('wiki_movie_plots_deduped.csv')
# library to clean data 
import re  
  
# Natural Language Tool Kit 
import nltk  
  
nltk.download('stopwords') 
  
# to remove stopword 
from nltk.corpus import stopwords 
  
# for Stemming propose  
from nltk.stem.porter import PorterStemmer 
  
# Initialize empty array 
# to append clean text  
corpus = []  
for i in range(0, 34886):  
      
    # column : "Review", row ith 
    plot = re.sub('[^a-zA-Z]', ' ', dataset['Plot'][i])  
      
    # convert all cases to lower cases 
    plot = plot.lower()  
      
    # split to array(default delimiter is " ") 
    plot = plot.split()  
      
    # creating PorterStemmer object to 
    # take main stem of each word 
    ps = PorterStemmer()  
      
    # loop for stemming each word 
    # in string array at ith row     
    plot = [ps.stem(word) for word in plot 
                if not word in set(stopwords.words('english'))]  
                  
    # rejoin all string array elements 
    # to create back into a string 
    plot = ' '.join(plot)   
      
    # append each string to create 
    # array of clean text  
    corpus.append(plot)  


# Creating the Bag of Words model 
from sklearn.feature_extraction.text import CountVectorizer 
  
# To extract max 1500 feature. 
# "max_features" is attribute to 
# experiment with to get better results 
cv = CountVectorizer(max_features = 1500)  
  
# X contains corpus (dependent variable) 
X = cv.fit_transform(corpus).toarray()  
  
# y contains answers if review 
# is positive or negative 
y = dataset.iloc[:, 1].values 




# Splitting the dataset into 
# the Training set and Test set 
from sklearn.model_selection import train_test_split 
  
# experiment with "test_size" 
# to get better results 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25) 



# Fitting Random Forest Classification 
# to the Training set 
from sklearn.ensemble import RandomForestClassifier 

# n_estimators can be said as number of 
# trees, experiment with n_estimators 
# to get better results 
model = RandomForestClassifier(n_estimators = 501, 
							criterion = 'entropy') 
							
model.fit(X_train, y_train) 

# Predicting the Test set results 
y_pred = model.predict(X_test) 

y_pred 