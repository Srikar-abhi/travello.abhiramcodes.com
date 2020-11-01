from django.shortcuts import render
from .models import Destination

def index(request):

    dest1 = Destination()
    dest1.name= "vizag"
    dest1.desc ="the city of destiny"
    dest1.price = "10000rs"
    dest1.img = "destination_1.jpg"

    dest2 = Destination()
    dest2.name ='vijayavada'
    dest2.desc = "The city of temples"
    dest2.price = "250000"
    dest2.img = "destination_3.jpg"

    dest3 = Destination()
    dest3.name ="hyderabad"
    dest3.desc = "The polluted city"
    dest3.price = "10000"
    dest3.img = "destination_5.jpg"


    dests = [dest1,dest2,dest3]

    return render(request,'index.html',{'dests':dests})

def home(request):
    return render(request,'home.html') 

def about(request):
    return render(request,'about.html') 

def contact(request):
    return render(request,'contact.html') 

def news(request):
    return render(request,'news.html') 
def elements(request):
    return render(request,'elements.html')
