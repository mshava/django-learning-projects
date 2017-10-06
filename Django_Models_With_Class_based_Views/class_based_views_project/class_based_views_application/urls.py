from django.conf.urls import url
from class_based_views_application import views

app_name = 'class_based_views_application'

urlpatterns = [
    url(r'^$', views.schoolListView.as_view(), name='list'),
    url(r'^(?P<pk>[-\w]+)/$', views.schoolDetailView.as_view(), name='detail'),
]
