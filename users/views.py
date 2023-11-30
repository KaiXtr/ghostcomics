from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import *
from .forms import *

def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())

class UserAddView(CreateView):
    model = User
    form_class = UserModelForm
    template_name = 'signin.html'
    success_url = '/'