from django.conf.urls  import url
from new_app import views

urlpatterns = [
    url(r'^$', views.users,name='users'),
]
