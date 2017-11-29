from django import forms
from .models import ShortenURL


class CreateShortenURLForm(forms.ModelForm):
    class Meta:
        model = ShortenURL
        fields = ['origin_url']