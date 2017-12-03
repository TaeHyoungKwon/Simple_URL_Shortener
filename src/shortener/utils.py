import random
import string

def random_generate_additional_url(instance):
    '''
    1. Generate additional_url using radom and string are python built-in function
    2. Confirm additional_url is duplicated or not 
    3. If duplicated, re-call random_generate_additional_url, else return additional_url is not duplicated value
    '''
    charaters = string.ascii_lowercase + string.digits + string.ascii_uppercase
    additional_url = "".join([random.choice(charaters) for _ in range(8)])

    instance_ShortenURL = instance.__class__
    additional_url_exists = instance_ShortenURL.objects.filter(additional_url=additional_url).exists()

    if additional_url_exists:
        return random_generate_additional_url(instance)
    else:
        return additional_url
    