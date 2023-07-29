from django.shortcuts import render
from django.http import HttpResponse
from .models import Video
from django.contrib import messages
import os
from django.core.files import File
from   video.models import vid,Video
from   signup.models import Signup
import csv
import pandas as pd
import numpy as np

# Create your views here.
def videoplay(request):
    count1=Video.objects.all().count()
    csv_file="C:/Users/rudra/Downloads/VigilAI (2)/VigilAI/healthcare/healthcare/AIbase.csv"
    reader = pd.read_csv(csv_file)
    reader=np.array(reader)
    # reader = csv.reader(decoded_file)
    def create_csv_file(file_path, data):
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
    for row in reader:
            # Extract data from each row and create a model instance
            model_instance = Video()
            model_instance.caption = row[1] # Assign data to the respective fields
            model_instance.video = row[0]
            model_instance.location = row[2]
            model_instance.time = row[5]
            model_instance.date = row[4]
            model_instance.coordinates = row[3]
            model_instance.save()
    data=[
        ['Name','Crime_Type','Location','Co-ordinates','Date','Time']
    ]

    create_csv_file("C:/Users/rudra/Downloads/VigilAI (2)/VigilAI/healthcare/healthcare/AIbase.csv",data)




   
    count2=Video.objects.all().count()
    video=Video.objects.filter(status='unverify')
    catch=[]
    ct=0
    for x in video:
        if ct==count2-count1:
            break
        catch.append(x)
        ct=ct+1
    catch.reverse()  
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        signup=Signup.objects.all()
        for x in signup:
            if x.name==name and x.token==password:
                return render(request,"play.html",{'video':video,'count':count2-count1,'catch':catch})   
    messages.warning(request,"INCORRECT PASSWORD OR USERNAME")
    return render(request,"login.html")  
def update(request):
    count=request.GET.get('count')
    time=request.GET.get('time')
    if request.method=='POST':
        crime=request.POST.get('crime')
        Video.objects.filter(time=time).update(caption=crime)
    video=Video.objects.filter(status='unverify')
    catch=[]
    ct=0
    for x in video:
        catch.append(x)
        ct=ct+1
        if ct==count:
            break
    
    
    return render(request,"play.html",{'video':video,'count':count,'catch':catch})
def home(request):
    video=Video.objects.filter(status='unverify')
    count=request.GET.get('count')
    catch=[]
    ct=0
    for x in video:
        catch.append(x)
        ct=ct+1
        if ct==count:
            break
    return render(request,"play.html",{'video':video,'count':count,'catch':catch})
def verify(request):
    count=request.GET.get('count')
    time=request.GET.get('time')
    Video.objects.filter(time=time).update(status='verify',description='ACTIVE')
    video=Video.objects.filter(status='unverify')
    catch=Video.objects.filter(status='unverify')
    # ct=0
    # for x in video:
    #     catch.append(x)
    #     ct=ct+1
    #     if ct==count:
    #         break
    return render(request,"play.html",{'video':video,'count':count,'catch':catch})
def unverify(request):
    count=request.GET.get('count')
    time=request.GET.get('time')
    Video.objects.filter(time=time).update(status='not verify',description='ACTIVE')
    video=Video.objects.filter(status='unverify')
    catch=Video.objects.filter(status='unverify')
    # ct=0
    # for x in video:
    #     catch.append(x)
    #     ct=ct+1
    #     if ct==count:
    #         break
    return render(request,"play.html",{'video':video,'count':count,'catch':catch})
def find(request):
    time=request.GET.get('time')
    count=request.GET.get('count')
    # count=1
    v=Video.objects.filter(status='unverify',time=time)
    video=[]
    for x in v:
        video.append(x)
    c=Video.objects.filter(status='unverify')
    ct=0
    catch=[]
    for x in c:
        if x.time!=time:
            video.append(x)
    for x in c:
        catch.append(x)
        ct=ct+1
        if ct==count:
            break
    catch.reverse()
    return render(request,"play.html",{'video':video,'count':count,'catch':catch})        
def submit2(request):
    loc=request.GET.get('location')
    # des=request.GET.get('description')
    Video.objects.filter(location=loc).update(description='CLOSED')
    video=Video.objects.filter(description='ACTIVE')
    return render(request,"play2.html",{'video':video})

def play2(request):
    count=request.GET.get('count')
    video=Video.objects.filter(description='ACTIVE')
    return render(request,"play2.html",{'video':video,'count':count})
def play2_submit(request):
    time=request.GET.get('time')
    # des=request.GET.get('description')
    Video.objects.filter(time=time).update(description='CLOSED')
    video=Video.objects.filter(description='ACTIVE')
    return render(request,"play2.html",{'video':video})
