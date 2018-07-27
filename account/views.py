from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from account.forms import LoginForm, RegisterForm
from django.contrib.auth import login as login_user
from django.contrib.auth import authenticate
# from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from faker import Faker
from django.db.models import Q



# Create your views here.
from account.models import Workers


def login(request):
    if request.method == 'GET':
        context = {}
        context['form'] = LoginForm
        return render(request, "login.html", context)
    elif request.method == 'POST':
        context = {}
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login_user(request, user)
                return redirect(reverse('login'))
            else:
                return redirect(reverse('login'))
        else:
            context['valid'] = False
            context['form'] = LoginForm
            context['error_text'] = "false"
        return render(request, "login.html", context)


# @login_required
def register(request):
    if request.method == 'GET':
        context = {}
        context['form'] = RegisterForm
        return render(request, "register.html", context)
    elif request.method == 'POST':
        context = {}
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            login_user(request, user)
            return redirect(reverse('login'))
        else:
            pass
        return render(request, "register.html", context)


def hello(request):
    context = {}
    query = request.GET.get('q', False)
    context['query'] = query
    if query:
        context['result'] = Workers.objects.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
        )
    return render(request, "private.html", context)


def insert_db(request):
    fake = Faker()
    fake.name()
    for x in range(100):
        Workers.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            description=fake.text()
        )
    return HttpResponse("ok")