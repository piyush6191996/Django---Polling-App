from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.login_view, name='login'),
    url(r'^index/$', views.index, name='index'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.RegistrationView.as_view(),name='register'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
