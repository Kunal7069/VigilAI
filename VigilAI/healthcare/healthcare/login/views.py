from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from signup.models import Signup
from video.models import Video
import os
from django.core.files import File
from   video.models import vid,Video
import csv
import pandas as pd
import numpy as np
# Create your views here.

def loginaction(request):
    # if request.method=='POST':
    #     name=request.POST.get('name')
    #     password=request.POST.get('password')
    # signup=Signup.objects.all()
    # for x in signup:
    #     if x.name==name:
    #         return render(request,"play.html")    
    # return HttpResponse("login.html")
    return render(request,"login.html")  
def open(request):
    video=Video.objects.filter(status='verify')
    return render(request,"open.html",{'video':video})  
def analysis(request):
    fighting_active=0
    shooting_active=0
    road_active=0
    robbery_active=0
    abuse_active=0
    arrest_active=0
    arson_active=0
    assault_active=0
    burglary_active=0
    explosion_active=0
    fighting_close=0
    shooting_close=0
    road_close=0
    robbery_close=0
    abuse_close=0
    arrest_close=0
    arson_close=0
    assault_close=0
    burglary_close=0
    explosion_close=0
    return render(request,"analysis.html",{'fighting_active':fighting_active,'fighting_close':fighting_close,'explosion_active':explosion_active,'explosion_close':explosion_close,
                                           'burglary_active':burglary_active,'burglary_close':burglary_close,'assault_active':assault_active,'assault_close':assault_close,
                                           'shooting_active':shooting_active,'shooting_close':shooting_close,'arson_active':arson_active,'arson_close':arson_close,
                                           'arrest_active':arrest_active,'arrest_close':arrest_close,'abuse_active':abuse_active,'abuse_close':abuse_close,
                                           'robbery_active':robbery_active,'robbery_close':robbery_close,'road_active':road_active,'road_close':road_close})
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def filter1(request):
    if request.method=='POST':
        location=request.POST.get('location')
        date=request.POST.get('date')
    #     time=request.POST.get('time') 
        video=Video.objects.filter(date=date,location=location)    
    return render(request,"play.html",{'video':video})
def filter3(request):
    if request.method=='POST':
        location=request.POST.get('location')
        video=Video.objects.filter(location=location,status='verify') 
        fighting_active=0
        shooting_active=0
        road_active=0
        robbery_active=0
        abuse_active=0
        arrest_active=0
        arson_active=0
        assault_active=0
        burglary_active=0
        explosion_active=0
        fighting_close=0
        shooting_close=0
        road_close=0
        robbery_close=0
        abuse_close=0
        arrest_close=0
        arson_close=0
        assault_close=0
        burglary_close=0
        explosion_close=0
        for x in video:
            if x.status=='verify' and x.caption=='Fighting' and x.description=='ACTIVE':
                fighting_active=fighting_active+1    
            elif x.status=='verify' and x.caption=='Fighting' and x.description=='CLOSED':
                fighting_close=fighting_close+1 
            elif x.status=='verify' and x.caption=='Shooting' and x.description=='ACTIVE':
                shooting_active=shooting_active+1    
            elif x.status=='verify' and x.caption=='Shooting' and x.description=='CLOSED':
                shooting_close=shooting_close+1 
            elif x.status=='verify' and x.caption=='RoadAccidents' and x.description=='ACTIVE':
                road_active=road_active+1    
            elif x.status=='verify' and x.caption=='RoadAccidents' and x.description=='CLOSED':
                road_close=road_close+1 
            elif x.status=='verify' and x.caption=='Robbery' and x.description=='ACTIVE':
                robbery_active=robbery_active+1    
            elif x.status=='verify' and x.caption=='Robbery' and x.description=='CLOSED':
                robbery_close=robbery_close+1 
            elif x.status=='verify' and x.caption=='Abuse' and x.description=='ACTIVE':
                abuse_active=abuse_active+1    
            elif x.status=='verify' and x.caption=='Abuse' and x.description=='CLOSED':
                abuse_close=abuse_close+1 
            elif x.status=='verify' and x.caption=='Arrest' and x.description=='ACTIVE':
                arrest_active=arrest_active+1    
            elif x.status=='verify' and x.caption=='Arrest' and x.description=='CLOSED':
                arrest_close=arrest_close+1 
            elif x.status=='verify' and x.caption=='Arson' and x.description=='ACTIVE':
                arson_active=arson_active+1    
            elif x.status=='verify' and x.caption=='Arson' and x.description=='CLOSED':
                arson_close=arson_close+1 
            elif x.status=='verify' and x.caption=='Assault' and x.description=='ACTIVE':
                assault_active=assault_active+1    
            elif x.status=='verify' and x.caption=='Assault' and x.description=='CLOSED':
                assault_close=assault_close+1 
            elif x.status=='verify' and x.caption=='Burglary' and x.description=='ACTIVE':
                burglary_active=burglary_active+1    
            elif x.status=='verify' and x.caption=='Burglary' and x.description=='CLOSED':
                burglary_close=burglary_close+1 
            elif x.status=='verify' and x.caption=='Explosion' and x.description=='ACTIVE':
                explosion_active=explosion_active+1    
            elif x.status=='verify' and x.caption=='Explosion' and x.description=='CLOSED':
                explosion_close=explosion_close+1     
    return render(request,"analysis.html",{'fighting_active':fighting_active,'fighting_close':fighting_close,'explosion_active':explosion_active,'explosion_close':explosion_close,
                                           'burglary_active':burglary_active,'burglary_close':burglary_close,'assault_active':assault_active,'assault_close':assault_close,
                                           'shooting_active':shooting_active,'shooting_close':shooting_close,'arson_active':arson_active,'arson_close':arson_close,
                                           'arrest_active':arrest_active,'arrest_close':arrest_close,'abuse_active':abuse_active,'abuse_close':abuse_close,
                                           'robbery_active':robbery_active,'robbery_close':robbery_close,'road_active':road_active,'road_close':road_close})
def filter2(request):
    if request.method=='POST':
        location=request.POST.get('location')
        date=request.POST.get('date')
        if date=='Default' and location!='Default':
            video=Video.objects.filter(location=location,description='ACTIVE')
        elif date!='Default' and location=='Default':
            video=Video.objects.filter(date=date,description='ACTIVE')
        elif date=='Default' and location=='Default':
            video=Video.objects.filter(status='verify')
        else:
            video=Video.objects.filter(date=date,location=location,description='ACTIVE')    
    return render(request,"play2.html",{'video':video})
def register(request):
    # if request.method=='POST':
    #     name=request.POST.get('name') 
    #     token=request.POST.get('token') 
    #     signup=Signup.objects.all()
    #     return HttpResponse("kkkkkk")
        # for x in signup:
        #     if name== x.name:
        #         return render(request,"play.html")
    
        # return HttpResponse("INCORRECT INFO")  
  
    # if request.method=='POST':
    #     name=request.POST.get('name') 
    #     token=request.POST.get('token') 
    #     signup=Signup.authenticate(name=name,token=token) 
    #     if signup is not None:
    #         # login(request,signup)  
    #         return redirect('video')
    #     else:
    #         return HttpResponse("INCORRECT INFO")
    # return render(request,"play.html")
    # return redirect('video')  
     return render(request,"play.html")