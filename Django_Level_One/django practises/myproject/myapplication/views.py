from django.shortcuts import render
from myapplication.models import User

# Create your views here.

def index(request):
    return render(request, 'myapplication/index.html')

def users(request):

    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'myapplication/users.html')
