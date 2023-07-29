from django.shortcuts import render
from signup.models import Signup
# Create your views here.
def signaction(request):
    return render(request,"signup.html")
# def register(request):
#     if request.method=="POST":
        # name=request.POST.get('name')
#         token=request.POST.get('token')
#         en=Signup(name=name,token=token)
#         en.save()
#     return render(request,"login.html")