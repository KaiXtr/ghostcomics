from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','username','email',)
    search_fields = ('name','username','email',)

admin.site.register(User, UserAdmin)