from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'abhi'})

def add(request):
    val1 = request.GET["number1"]
    val2 = request.GET["number1"]
    res = val1+val2
    return render(request,'result.html',{"resul":res})