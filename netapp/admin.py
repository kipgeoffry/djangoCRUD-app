from django.contrib import admin
#import the models that we just created under models.py
from .models import Nerecords, PErecords 

# Register your models here.
admin.site.register(Nerecords)
admin.site.register(PErecords)
