from django.contrib import admin

# Register your models here.
from .models import Subject, Deadline

admin.site.register(Subject)
admin.site.register(Deadline)