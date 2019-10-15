from django.shortcuts import render
from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        useremail = request.POST.get('email')
        #username, email=None, password=None, **extra_fields
        user = User.objects.create_user(username=username,password=password,email=useremail)
        user.save()
        if user:
            auth.login(request, user)
            return render(request,'index.html')
        else:
            return render(request,'register.html')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            return render(request, 'index.html')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')

def index(request):
    name = request.user.username
    return render(request, 'index.html', {'name':name})