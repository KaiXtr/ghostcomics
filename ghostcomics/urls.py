"""
URL configuration for ghostcomics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from gibis.serializer import GibiSerializer, GibiViewSet
from gibis.views import *
from users.views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'gibis', GibiViewSet, basename="Gibi")

urlpatterns = [
    #path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('',GibiMainView.as_view(),name='main'),
    path('gibis/',GibiListView.as_view(),name='gibi_list'),
    path('addgibi/',GibiAddView.as_view(),name='gibi_add'),
    path('gibi/<int:pk>/',GibiDetailView.as_view(),name='gibi_detail'),
    path('gibi/<int:pk>/update/',GibiUpdateView.as_view(),name='gibi_update'),
    path('gibi/<int:pk>/delete/',GibiDeleteView.as_view(),name='gibi_delete'), 
    path('api/', include('rest_framework.urls')),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('esqueceu-senha/', esqueceu_senha_view, name='esqueceu-senha'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)