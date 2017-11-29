from django import forms
from .validation import validate_url, validate_first_essential_part

class CreateShortenURLForm(forms.Form):
    origin_url = forms.CharField(
        label="submit URL", 
        validators=[validate_url, validate_first_essential_part]
        )