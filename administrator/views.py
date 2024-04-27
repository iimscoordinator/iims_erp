
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages


def admindashboard(request):
    if request.method == 'GET':
        return render(request,'administrator/admindashboard.html',{})
    if request.method == 'POST':
        pass
def admissiondashboard(request):
    if request.method == 'GET':
        return render(request,'administrator/admissiondashboard.html',{})
    if request.method == 'POST':
        pass   
def lmsdashboard(request):
    if request.method == 'GET':
        return render(request,'administrator/lms_dashboard.html',{})
    if request.method == 'POST':
        pass

def feedbackdashboard(request):
    if request.method == 'GET':
        return render(request,'administrator/feedbackdashboard.html',{})
    if request.method == 'POST':
        pass

def librarydashboard(request):
    if request.method == 'GET':
        return render(request,'administrator/librarydashboard.html',{})
    if request.method == 'POST':
        pass

def mcqdashboard(request):
    if request.method == 'GET':
        return render(request,'administrator/mcqdashboard.html',{})
    if request.method == 'POST':
        pass