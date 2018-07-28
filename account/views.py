from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from account.forms import LoginForm, RegisterForm
from django.contrib.auth import login as login_user
from django.contrib.auth import authenticate
# from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, JsonResponse
from faker import Faker
from django.db.models import Q

# Create your views here.
from account.models import Workers, Company, Job


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
            (Q(first_name__icontains=query) | Q(last_name__icontains=query)) & Q(company__name__icontains=query))
    return render(request, "private.html", context)


def insert_db(request):
    fake = Faker()
    fake.name()
    companies = Company.objects.all()
    for company in companies:
        job = Job.objects.create(
            name=fake.job()
        )
        company.job = job
        company.save()
    return HttpResponse("ok")


def detail_worker(request, slug):
    context = {}
    context['worker'] = get_object_or_404(Workers, slug=slug)
    return render(request, "detail-worker.html", context)


def test_view(request):
    context = {}
    data = serialize("json", Workers.objects.all())
    # if request.is_ajax():
    #     return JsonResponse(data, safe=False)
    return HttpResponse(data, content_type="application/json")