from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as user_login,logout as lg
from django.contrib.auth.decorators import login_required
from login.models import *
# Create your views here.

def home(request):
    return render(request,'index.html')

def about_page(request):
    return render(request,'about.html')

def register(request):
    if request.method == "POST" :
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        my_user=User.objects.create_user(name,email,password)
        my_user.save()
        return redirect('login')
    return render(request,'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            user_login(request,user)
            return redirect('report')
        else:
            return HttpResponse("<h1>invalid user</h1>")
    return render(request,'login.html')

def logout(request):
    lg(request)
    return redirect('login')

@login_required(login_url='login')
def report_fill(request):
    if request.method == "POST":
        data = request.POST

        user_name   = request.POST.get("user_name")
        email       = request.POST.get("email")
        location    = request.POST.get("location")
        date_time   = request.POST.get("date_time")
        discription = request.POST.get("discription")
        image       = request.FILES.get("image")

        report.objects.create(
            user_name   = user_name,
            email       = email,
            location    = location,
            date_time   = date_time,
            discription = discription,
            image       = image,
        )
        return redirect('report')
    
    queryset = report.objects.all()
    context  = {'reports':queryset}
    return render(request,'report.html',context)

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')

def delete_report(request , id):
    queryset = report.objects.get(id = id)
    queryset.delete()
    return redirect('report')

def update_report(request ,id):
    queryset = report.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        user_name = data.get("user_name")
        email = data.get("email")
        location = data.get("location")
        image = request.FILES.get('image')
        date_time = data.get("date_time")
        discription = data.get("discription")
        queryset.user_name = user_name
        queryset.date_time = date_time
        queryset.discription = discription 
        queryset.location = location
        queryset.email = email
        if image:
            queryset.image = image

        queryset.save()
        return redirect('report')

    context = {'reports':queryset}
    return render(request , 'update_report.html' , context)
