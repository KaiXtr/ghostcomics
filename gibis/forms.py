from typing import Any
from django import forms
from .models import *
from datetime import datetime

class GibiModelForm(forms.ModelForm):
    class Meta:
        model = Gibi
        fields = '__all__'

    def clean_year(self):
        data_atual = datetime.now().date()
        ano_atual = int(data_atual.strftime("%Y"))
        
        year = self.cleaned_data.get('year')
        if year > ano_atual:
            self.add_error('year','Não é possível adicionar um ano de publicação posterior ao ano atual.')
        return year
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            self.add_error('price','Não pode conter valores negativos')
        return price


