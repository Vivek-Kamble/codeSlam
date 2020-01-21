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



class CreateMYSQLInstance:
    def __init__(self):
        from sqlalchemy import create_engine
        # create sqlalchemy engine
        self.engine = create_engine("mysql+pymysql://{user}:{pw}@192.168.0.106:3306/{db}"
                       .format(user="root",
                               pw="pass@1234",
                               db="mydatabase"))
        print("CreateMYSQLInstance")
        print(self.engine)

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


@csrf_exempt
def predictmodel(request,modeltouse="",Description=""):
    print("Predict Model")
    print(Description)
    if request.method == 'GET': 
        mydata=  "prdicted genere" 
        print("converting Json")
        print( mydata )
        return JSONResponse(mydata)


