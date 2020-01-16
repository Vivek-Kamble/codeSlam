from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from games.models import Game
from games.models import MyModel
from games.serializers import GameSerializer
from games.serializers import DataSerializer
import pandas as pd

def home(request):
    response = requests.get('http://code-slam.herokuapp.com/movies')
    data = response.json()
    return render(request, 'core/home.html', {
        'plot': data['Plot'],
        'genre': data['Genre']
    })
dataset = pd.read_csv('wiki_movie_plots_deduped.csv')


plot = dataset['Plot']
genre = dataset['Genre']
# class CreateMYSQLInstance:
#     def __init__(self):
        # from sqlalchemy import create_engine
        # # create sqlalchemy engine
        # self.engine = create_engine("mysql+pymysql://{user}:{pw}@192.168.0.106:3306/{db}"
        #                .format(user="root",
        #                        pw="pass@1234",
        #                        db="mydatabase"))
        # print("CreateMYSQLInstance")
        # print(self.engine)

       

import re
plot = re.sub('[^a-zA-Z]',' ',plot)

import nltk
nltk.download('stopwords')

plot = plot.lower()
plot = plot.split()


notstopwords = ['not']
from nltk.corpus import stopwords
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

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'           
        super(JSONResponse, self).__init__(content, **kwargs)



@csrf_exempt
def createmodel(request,modeltopredict=""):
    print("create Model")
    if request.method == 'GET': 
        mydata=  "model created" 
        print("converting Json")
        print( mydata )
        return JSONResponse(mydata)
from sklearn.ensemble import RandomForestClassifier
dictionary = make_Dictionary(plot)
def make_Dictionary(root_dir):
   all_words = []
   emails = [os.path.join(root_dir,f) for f in os.listdir(root_dir)]
   for mail in emails:
        with open(mail) as m:
            for line in m:
                words = line.split()
                all_words += words
   dictionary = Counter(all_words)
# if you have python version 3.x use commented version.

@csrf_exempt
def predictmodel(request,modeltouse="",Description=""):
    print("Predict Model")
    print(Description)
    if request.method == 'GET': 
        mydata=  "prdicted genere" 
        print("converting Json")
        print( mydata )
        return JSONResponse(mydata)


