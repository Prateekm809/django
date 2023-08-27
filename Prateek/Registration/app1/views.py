from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import AdminLoginForm
# Create your views here.

# home page
def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Password are not matched!!")
        else:
            my_user = User.objects.create_user(username=uname, email=email, password=pass1)
            my_user.save()
            return HttpResponseRedirect("login")

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        print(username, pass1)
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('home')
        else:
            return HttpResponse('username and password is incorrect!!')
    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return HttpResponseRedirect('login')


def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the admin panel
                return HttpResponseRedirect('/admin/')
            else:
                # Invalid credentials, display an error
                return render(request, 'admin_login.html', {'form': form, 'error_message': 'Invalid details.'})
    else:
        form = AdminLoginForm()
    return render(request, 'admin_login.html', {'form': form})
