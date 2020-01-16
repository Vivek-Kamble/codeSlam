from django.conf.urls import url
from games import views

urlpatterns = [
    url(r'^createmodel/(?P<modeltopredict>[A-Za-z]+)/$', views.createmodel),
    url(r'^predictmodel/(?P<modeltouse>[A-Za-z]+)/(?P<Description>.+)/$', views.predictmodel),
]
