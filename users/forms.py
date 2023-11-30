from typing import Any
from django import forms
from .models import *

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            self.add_error('password','A senha deve possuir no mínimo 8 caracteres')
        return password


