from django.contrib import admin

# from timedash.timex.forms import NewsLetterForm
from .models import Person, Newsletter

# Register your models here.
admin.site.register(Person)
admin.site.register(Newsletter)
