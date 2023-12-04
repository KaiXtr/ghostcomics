from django.contrib import admin
from .models import *

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class GibiAdmin(admin.ModelAdmin):
    list_display = ('name','authors','genre','company','year','price')
    search_fields = ('name','authors','genre','company','year',)

admin.site.register(Genre, GenreAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Gibi, GibiAdmin)