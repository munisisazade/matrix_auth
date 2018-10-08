from django.conf.urls import url
from account import views
from django.contrib.auth.views import logout
from django.views.generic import TemplateView

urlpatterns = [
    # url(r'^$', views.login, name="login"),
    url(r'^logout/$', logout, name="logout", kwargs={'next_page': '/'}),
    url(r'^register/$', views.register, name="register"),
    url(r'^search/$', views.hello, name="hello"),
    url(r'^ajax/$', views.AjaxView.as_view(), name="ajax-view"),
    url(r'^$', views.TestingListView.as_view(), name="testing-view"),
    url(r'^test/$', views.test_view, name="test"),
    url(r'^article/$', views.article_form, name="article"),
    url(r'^worker/(?P<slug>.*)/$', views.detail_worker, name="worker-detail"),
    url(r'^data/$', views.insert_db, name="add"),
    url(r'^testing/$', views.TemplateView.as_view(), name="test-view"),
]
