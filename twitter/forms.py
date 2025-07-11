from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nome de usuário'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }
        help_texts = {
            'username': '',
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['imagem']

