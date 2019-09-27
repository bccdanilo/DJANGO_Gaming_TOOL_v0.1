from django import forms

from .models import Player

class RawProductForm(forms.Form):
    name = forms.CharField()
    nick = forms.CharField()