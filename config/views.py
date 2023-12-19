from django.contrib import messages, auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import CustomUser


def is_superuser(user):
    return user.is_superuser


def is_staff(user):
    return user.is_staff


# def is_golden_user(user):
#     return user.is_golden


def is_golden_user(user):
    return user.is_authenticated and user.is_golden


def is_silvern_user(user):
    return user.is_authenticated and user.is_silvern


@login_required(login_url='register')
def profile(request):
    user = CustomUser.objects.get(username=request.user.username)
    return render(request, 'auth_system/profile.html', {'user': user})


@user_passes_test(is_superuser, login_url='/')
def is_superuser_check(request):
    return HttpResponse("you are superuser so you can see this page")


@user_passes_test(is_staff, login_url='/')
def is_staff_check(request):
    return HttpResponse("you are staff user so you can see this page")


@user_passes_test(is_golden_user, login_url='/')
def is_golden_check(request):
    return HttpResponse('you are golden user so you can see this page')
    # return redirect('/')


@user_passes_test(is_silvern_user, login_url='/')
def is_silvern_check(request):
    return HttpResponse('you are silvern user so you can see this page')


def home(request):
    user = CustomUser.objects.filter(username=request.user.username).first()
    return render(request, 'auth_system/home.html', {'user': user})


def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request, 'username already exists.')
                return redirect('/')
            else:
                user = CustomUser.objects.create_user(username=username, phone_number=phone_number,
                                                      first_name=first_name, last_name=last_name, email=email,
                                                      password=password, confirm_password=confirm_password)
                user.save()
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                return redirect('/')

        else:
            messages.info(request, 'password does not match')
            return redirect('/')

    else:
        return render(request, 'auth_system/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

        elif CustomUser.objects.filter(username=username).exists():
            messages.info(request, 'Invalid password')
            return redirect('/login/')

        else:
            messages.info(request, 'Invalid username')
            return redirect('/login/')

    else:
        return render(request, 'auth_system/login.html')


def logout_view(request):
    auth.logout(request)
    return redirect('/')
