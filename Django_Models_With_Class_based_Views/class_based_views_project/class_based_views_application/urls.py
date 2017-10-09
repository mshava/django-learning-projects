from django.conf.urls import url
from class_based_views_application import views

app_name = 'class_based_views_application'

urlpatterns = [
    url(r'^$', views.schoolListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.schoolDetailView.as_view(), name='detail'),
    url(r'^create/$', views.SchoolCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.SchoolUpateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='delete'),
]
