from django.shortcuts import render,HttpResponse
from datetime import datetime
from app.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def development(request):
    return render(request,'development.html')

def business(request):
    return render(request,'business.html')

def marketing(request):
    return  render(request,'marketing.html')
def ai(request):
    return  render(request,'ai.html')

def ml(request):
    return  render(request,'ml.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent') 
    return  render(request,'contact.html')