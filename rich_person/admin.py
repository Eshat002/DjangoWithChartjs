# Assuming this is within your app's admin.py file

from django.contrib import admin
from .models import RichPerson

admin.site.register(RichPerson)
