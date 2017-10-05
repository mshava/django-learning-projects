from django.conf.urls import url
from myapplication import views

urlpatterns = [
    url(r'^$', views.users, name='users'),

]
