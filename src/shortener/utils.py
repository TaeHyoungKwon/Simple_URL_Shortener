import random
import string

def random_generate_additional_url():
    charaters = string.ascii_lowercase + string.digits
    random_word = "".join([random.choice(charaters) for _ in range(8)])

    return random_word
    