"""
URL configuration for recipe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from myrecipe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipelist', views.Recipelist.as_view()),
    path('recipecreate', views.Recipecreate.as_view()),
    path('reciperetrieve/<int:id>/', views.Reciperetrieve.as_view()),
    path('recipefullupdate/<int:id>/', views.Recipefullupdate.as_view()),  
    path('recipepartialupdate/<int:id>/', views.Recipepartialupdate.as_view()), 
    path('recipedelete/<int:id>/', views.Recipedelete.as_view(), name='recipe-delete'),
]