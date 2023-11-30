from typing import Any
from django import forms
from .models import *

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 1:
            self.add_error('value','Valor mínimo deve ser R$ 1')
        return value


