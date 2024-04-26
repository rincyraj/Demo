from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def say_hello(request):
    #pull data from DB
    #Send email
    # return HttpResponse('Hello Rincy')
    return render(request=request,template_name='hello.html',context={'name':'Rincy'}) 

def home_page(request):
    # return HttpResponse('Welcome to Home Page')
    person = {'name':'Haron' ,'age':10 ,'place':'tvm','fruit_list':['banana','apple','orange']}
    return render(request,'home.html',person)

def index(request):
    return render(request,'index.html')

def about_page(request):
    return render(request,'about.html')

def contact_page(request):
    return render(request,'contact.html')

def doctors_page(request):
   return render(request,'doctors.html')

def booking(request):
    return render(request,'booking.html')

def department(request):
    return render(request,'department.html')