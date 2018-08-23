from django import forms
from django.forms import TextInput,Select, PasswordInput, Textarea
from .models import Caixa, Preco
from django.contrib.auth.models import User

class PrecoForm(forms.ModelForm):

    class Meta:
        model = Preco
        fields = ('__all__')



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'name':'username'}),
            'password': PasswordInput(attrs={'class': 'form-control', 'name':'password'}),

        }

class CaixaForm(forms.ModelForm):

    class Meta:
        model = Caixa
        fields = ('quantidade', 'preco')

        widgets = {
            'quantidade': TextInput(attrs={'type':'number', 'class': 'form-control', 'name':'quantidade', 'min':'1'}),
            'preco': Select(attrs={'type':'text', 'class': 'form-control', 'name':'preco'}),


        }
