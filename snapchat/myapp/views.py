from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def register(request):
    if request.method=='POST':
        form = CafestoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cafe_list')
    else:
        form=CafestoreForm()
    return render(request,'register.html',{'form':form})
def cafe_list(request):
    cafestore=Cafestore.objects.all()
    return render(request,'cafe_list.html',{'cafestore':cafestore})
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def login(request):
    return render(request,'login.html')

def contact(request):
    return render(request,'contact.html')

