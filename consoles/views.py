from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Console

def main(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def consoles(request):
    nomes = []
    for i in Console.objects.all().values():
        nomes.append(i['name'])
    ctxt = {
        'nomes': nomes
    }
    template = loader.get_template("consoles.html")
    return HttpResponse(template.render(ctxt,request))