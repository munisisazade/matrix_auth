from time import sleep

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.forms import all_valid
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from account.forms import LoginForm, RegisterForm, ArticleForm, Pictureformset
from django.contrib.auth import login as login_user
from django.contrib.auth import authenticate
# from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, JsonResponse
from faker import Faker
from django.db.models import Q
from .generic import View, TemplateView
from django.views import generic

# Create your views here.
from account.models import Workers, Company, Job, Tester, Todo


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
    today = timezone.now()
    # fake = Faker()
    # a = 50
    # for index, worker in enumerate(Workers.objects.all().order_by("?")):
    #     worker.tester_list.add(Tester.objects.all().order_by("?").last())
    #     worker.save()
    #     if a == index:
    #         break
    if query:
        context['result'] = Workers.objects.filter(
            tester_list__name__icontains=query
        )
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


def article_form(request):
    context = {}
    if request.method == 'POST':
        article = ArticleForm(request.POST)
        picture_forms = Pictureformset(request.POST, request.FILES)
        article_instance = ""
        if article.is_valid():
            article_instance = article.save()
        if all_valid(picture_forms):
            for pictureform in picture_forms:
                picture = pictureform.save(commit=False)
                picture.article = article_instance
                picture.save()
    context["form"] = ArticleForm()
    context["formset"] = Pictureformset()
    return render(request, "article_form.html", context)


class MyView(generic.ListView):
    model = Job
    template_name = "test.html"
    paginate_by = 5

    # queryset =

    def get_queryset(self):
        qs = super(MyView, self).get_queryset()
        query = self.request.GET.get('q', False)
        if query and query != "":
            return qs.filter(name__icontains=query)
        else:
            return qs


class DetailView(generic.CreateView):
    template_name = "test.html"
    model = Job
    context_object_name = "job"


def testview(request):
    # code
    return JsonResponse({
        "message": "It works"
    })


class AjaxView(generic.TemplateView):
    template_name = "ajax-test.html"
    ajax_template = "partials/list.html"

    def get_context_data(self, **kwargs):
        context = {}
        context['todo_list'] = Todo.objects.all()
        # Todo.objects.all().delete()
        return context

    def post(self, request,*args, **kwargs):
        if request.is_ajax():
            text = request.POST.get('text')
            if text != "":
                context = {}
                obj = Todo.objects.create(
                    name=text
                )
                context['todo_list'] = Todo.objects.all().order_by('name')
                return render(request, self.ajax_template, context)
            else:
                return JsonResponse({
                    "message": "FAIL"
                })
        else:
            return JsonResponse({
                "status": "ok"
            })


class TestingListView(generic.ListView):
    model = Workers
    template_name = "example.html"