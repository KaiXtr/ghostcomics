from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

def main(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def gibis(request):
    dados = Gibi.objects.all()
    search = request.GET.get('search')
    if search:
        gbs = Gibi.objects.filter(model_icontains = search)
    
    genres = {}
    for i in Genre.objects.all().values():
        genres[i['id']] = i['name']
        
    companies = {}
    for i in Company.objects.all().values():
        companies[i['id']] = i['name']
        
    gbs = []
    for i in dados.values():
        i['genre'] = genres[i['genre_id']]
        i['company'] = companies[i['company_id']]
        gbs.append(i)
    
    return render(request,"gibis.html",{'gibis': gbs})

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")