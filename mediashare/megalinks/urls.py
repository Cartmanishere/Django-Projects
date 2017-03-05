from django.conf.urls import url
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    url(r'^$', views.newindex, name='newindex'),
    url(r'^register/', views.register, name="register"),
    url(r'^requests/$', views.requests, name='requests'),
    url(r'^activity/', views.activity, name="activity"),
    url(r'^(?P<tagfilter>[\w|\W]+)/1$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^log_out/', auth_views.logout, name="logout"),
    url(r'^search/', views.search, name="search"),
]