from django import forms
from .models import ShortenURL
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
    except:
        raise ValidationError("Invalid URL for this field")
    return value

'''
class CreateShortenURLForm(forms.ModelForm):
    origin_url = forms.CharField(label="submit URL", validators=[validate_url])

    class Meta:
        model = ShortenURL
        fields = ['origin_url']
'''

class CreateShortenURLForm(forms.Form):
    origin_url = forms.CharField(label="submit URL")

    def clean(self):
        cleaned_data = super(CreateShortenURLForm, self).clean()
        print(cleaned_data)
        url = cleaned_data.get('origin_url')
        print(url)
        url_validator = URLValidator(url)
        print("Kwon!")
        print(url_validator)

        try:
            url_validator(url)
        except:
            raise forms.ValidationError("Invalid URL!")
        return url
    