from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    EFTO=Topicform()
    d={'EFTO':EFTO}
    if request.method=='POST':
        TFDO=Topicform(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('Topic is added')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EFWO=Webpagefom()
    d={'EFWO':EFWO}
    if request.method=='POST':
        WFDO=Webpagefom(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('Webpage is added')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    EFAO=Accessrecordform()
    d={'EFAO':EFAO}
    if request.method=='POST':
        AFDO=Accessrecordform(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('Accessrecord is added')
    return render(request,'insert_accessrecord.html',d)