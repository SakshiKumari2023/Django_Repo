"""
URL configuration for weather_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from weather.views import *

urlpatterns = [
    path("", home, name='home'),
    path("skill", skill_set, name='skill'),
    path('register/',register,name='register'),
    path('login/',login_page,name="login_page"),
    path('logout/',logout_page,name='logout_page'),
    path("help_and_suggestions",help,name='help'),
    path('admin/', admin.site.urls),
    
]
