from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
    '''
    If you user input invalid url, return Error Message.
    '''
    url_validator = URLValidator()
    try:
        url_validator(value)
    except:
        raise ValidationError("Invalid URL for this field")
    return value


def validate_first_essential_part(value):
    '''
    If you user input url without "http://", return Error Message.
    '''
    if not "http://" in value:
        raise ValidationError("You have to Add 'http://' front of your origin_url!")   