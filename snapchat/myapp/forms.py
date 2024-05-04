from django import forms
from .models import Cafestore

class CafestoreForm(forms.ModelForm):
    class Meta:
        model=Cafestore 
        fields=['item','cost','time','quantity',]