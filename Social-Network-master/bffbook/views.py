from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home_view(request):
    user = request.user
    hello = 'Hello world'

    context = {
        'user': user,
        'hello': hello,
    }
    return render(request, 'main/home.html', context)
    # return HttpResponse('Hello world')


def signup_view(request):
    user = request.user
    signup = 'signup world'

    context = {
        'user': user,
        'signup': login,
    }
    return render(request, 'main/signup_page.html', context)
    # return HttpResponse('login page')


def login_view(request):
    user = request.user
    login = 'login world'

    context = {
        'user': user,
        'login': login,
    }
    return render(request, 'main/login_page.html', context)
    # return HttpResponse('login page')


def handlesignup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        pnumber = request.POST['pnumber']
        state = request.POST['state']
        country = request.POST['country']


        # check for anny error
        if pass1 != pass2:
            messages.error(request, 'your passwords do not match')
            return redirect('/')

        # create the user
        myuser = User.objects.create_user(username=username, email=username, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'your account has been created successfully')

        return redirect('/')

    else:
        return HttpResponse("404 not found")


def handlelogin(request):
    if request.method == 'POST':
        # get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged In!!!')
            return redirect('/')
        else:
            messages.error(request, 'You Have Entered Invalid Credentials, Please Try Again!!!')

        return redirect('/')
    return HttpResponse("404 not found")


def handlelogout(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('/')
