from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your vies here


def topic_insert(reqest):
    tn=input('Enter  topic_name')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('Topic is insarted')

def webpage_insert(reqest):
    tn=input("Enter  topic name")
    to=topic.objects.get_or_create(topic_name=tn)[0] 
    to.save()
    na =input("Enter the name")
    urll=input("Enter the url")
    woj=webpage.objects.get_or_create(topic_name=tn,name=na,url=urll)
    woj.save()
    return HttpResponse("webpage is successfully created")

def accessrecords_insert(reqest):
    tn=input('Enter topic_name')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    na =input("Enter the name")
    woj=webpage.objects.get_or_create(topic_name=to,name=na)[0]
    woj.save()
    dt=input("Enter the date")
    at=input("Enter the authername")
    aoj=accessrecords.objects.get_or_create(topic_name=to,name=woj,date=dt,author=at)[0]
    aoj.save()
    return HttpResponse("accessrecords created")
