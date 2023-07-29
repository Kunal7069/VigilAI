"""healthcare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
# from signup.views import signaction
from video.views import videoplay,verify,unverify,play2,play2_submit,submit2,update,find,home
from login.views import loginaction,register,filter1,filter2,filter3,open,about,contact,analysis
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('video.urls')),
    # path('signup/',signaction),
    path('',loginaction),
    path('video/',videoplay,name="video"),
    path('analysis/',analysis,name="analysis"),
    path('home/',home,name="home"),
    path('about/',about,name="about"),
    path('open/about/',about,name="about"),
    path('contact/',contact,name="contact"),
    path('open/contact/',contact,name="contact"),
    path('open/',open,name="open"),
    path('play2/',play2,name="play2"),
    path('submit/',play2_submit,name="play2_submit"),
    path('filter3/',filter3,name="filter3"),
    path('verify/',verify,name="verify"),
    path('find/',find,name="find"),
    path('unverify/',unverify,name="unverify"),
    path('update/',update,name="update"),
    path('register/',register,name="register"),
    path('register/filter1/',filter1,name="filter1"),
    path('play2/filter2/',filter2,name="filter2"),
    path('play2/filter2/submit/',submit2,name="submit2"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)