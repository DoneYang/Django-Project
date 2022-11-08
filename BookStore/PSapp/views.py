from django.shortcuts import render
from django.http import HttpResponse 

def base(reqiest):
    return render(reqiest, 'layout/base.html')

def hello(request, id):
    return HttpResponse('Hello World'+ str(id))

def article(request, year, slug):
    return HttpResponse('Article = ' + str(year) +'slug = '+ slug)
