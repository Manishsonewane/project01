from django.shortcuts import render,redirect
from .models import*
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,'index.html') 

def about(request):
    return render(request,'about.html') 

def companys(request):
    return render(request,'companys.html')  

def contact(request):
    
    
    if request.method == 'POST':
        Name=request.POST["Name"]
        phone=request.POST["phone"]
        
        email=request.POST["email"]
        message=request.POST["message"]
        

        
        data=company(Name=Name,phone=phone,email=email,message=message)
        data.save() 
        return render(request,'contact.html')
    else:
        return render(request,'contact.html')

  

def steel(request):
    return render(request,'steel.html')              

def sendmail(request):
    if request.method == 'POST':
        Name=request.POST["Name"]
        phone=request.POST["phone"]
        
        email=request.POST["email"]
        message=request.POST["message"]
        send_mail(
        'Name',
        'phone',
        'email',
        'message',
        'pintusonewane2016@gmail.com',
        ['harishdhengre786@gmail.com'],
        fail_silently=False,
        )
        return render(request,'contact.html')
    else:
        return render(request,'contact.html')





