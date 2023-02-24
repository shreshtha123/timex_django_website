"""timedash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from timex import views

urlpatterns = [
    path('',views.home,name='home'),
    path('newsletter',views.newsletter,name='newsletter'),
    path('admin/', admin.site.urls),
    path('contacts',views.contact, name='contact'),
    path('verification',views.verification,name='verification'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('logoutuser',views.logoutuser,name='logoutuser'),
    path('signupuser',views.signupuser,name='signupuser'),
    path('about',views.about,name='about'),

    
]
