from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
     path('admissiondashboard/', views.admissiondashboard,name='admissiondashboard'),
     path('lmsdashboard/', views.lmsdashboard,name='lmsdashboard'),
     path('feedbackdashboard/', views.feedbackdashboard,name='feedbackdashboard'),
     path('librarydashboard/', views.librarydashboard,name='librarydashboard'),
     path('mcqdashboard/', views.mcqdashboard,name='mcqdashboard'),
     path('admindashboard/', views.admindashboard,name='admindashboard'),
    
] 