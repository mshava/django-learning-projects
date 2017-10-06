from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'basic_app/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'post':
        form = forms.FormName(request.post)

        if form.is_valid():
            #Do somethind code
            print('Validation success!')
            print("name: "+ form.cleaned_data['name'])
            print("email: "+ form.cleaned_data['email'])
            print("text: "+ form.cleaned_data['text'])

    return render(request, 'basic_app/forms_page.html', {'form': form})
