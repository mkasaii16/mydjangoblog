from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    #return HttpResponse('hi there iam moein')
    return render(request, 'about.html')

def home(request):
    #return HttpResponse('wellcome ... !')
    return render(request, 'home.html')
