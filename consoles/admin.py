from django.contrib import admin
from consoles.models import Brand, Console

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ConsoleAdmin(admin.ModelAdmin):
    list_display = ('name','brand','year',)
    search_fields = ('name','brand','year',)

admin.site.register(Brand, BrandAdmin)
admin.site.register(Console, ConsoleAdmin)