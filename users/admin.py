from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','username')
    search_fields = ('name','username')

admin.site.register(User, UserAdmin)