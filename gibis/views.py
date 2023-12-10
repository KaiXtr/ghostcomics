from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def main(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

@method_decorator(login_required(login_url='login'), name='dispatch')
class GibiAddView(CreateView):
    model = Gibi
    form_class = GibiModelForm
    template_name = 'gibi_add.html'
    success_url = '/gibis/'

class GibiListView(ListView):
    model = Gibi
    template_name = 'gibi_list.html'
    context_object_name = 'gibis'

class GibiDetailView(DetailView):
    model = Gibi
    template_name = 'gibi_detail.html'

class GibiUpdateView(UpdateView):
    model = Gibi
    form_class = GibiModelForm
    template_name = 'gibi_update.html'
    success_url = '/gibis/'

class GibiDeleteView(DeleteView):
    model = Gibi
    template_name = 'gibi_delete.html'
    success_url = '/gibis/'

'''
def gibis(request):
    dados = Gibi.objects.all()
    search = request.GET.get('search')
    if search:
        dados = Gibi.objects.filter(name = search)
    
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
'''

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")