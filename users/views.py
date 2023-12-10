from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login_view(request):
    erro = None

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('gibi_list')
        else:
            login_form = AuthenticationForm()
            erro = 'Usuário ou senha incorretos.'
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form,'erro': erro})

def logout_view(request):
    logout(request)
    return redirect('gibi_list')

def esqueceu_senha_view(request):
    template = loader.get_template("esqueceu_senha.html")
    return HttpResponse(template.render())