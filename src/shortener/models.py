import random
import string
from django.db import models

# Create your models here.
def code_generator(size=6, chars= string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class KirrURL(models.Model):
    """docstring for KirrURL"""
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True)

    def save(self, *args, **kwargs):
        print('something')
        self.shortcode = code_generator()
        super(KirrURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

'''

After adding a model, do:
python manage.py makemigrations
python manage.py migrate

'''