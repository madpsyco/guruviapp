from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            # return redirect('/class/classvideo/')
            return render(request,'/class/classvideo/',{'username':username})
        else:
            messages.success(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['firstname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['cpassword']

        if password == confirm_password:
            user = User.objects.create_user(username=username, first_name=name, password=password, email=email)
            user.save()

    return render(request, "register.html")