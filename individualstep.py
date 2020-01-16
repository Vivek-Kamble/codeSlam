# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:36:08 2019

@author: PANKAJ
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Restaurant_Reviews.tsv', 
                      delimiter = '\t')
review = dataset['Review'][0]
import re
review = re.sub('[^a-zA-Z]', ' ',review)
import nltk
nltk.download('stopwords')


review = review.lower()
review = review.split()
notstopwords = ['not']

from nltk.corpus import stopwords

corpus = []
mybag= []    
for data in review:
    if(data not in stopwords.words('english')):
        mybag.append(data)

mystembag = []
from nltk.stem.porter import PorterStemmer

for data in mybag:
    ps = PorterStemmer()
    stemdata = ps.stem(data)
    if stemdata not in mystembag:
        mystembag.append(stemdata)


review = ' '.join(mystembag)   
corpus.append(review)




#corups is collection of all steem revies...
from sklearn.feature_extraction.text  import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values


#classification
#randomforest
#dt
#logi