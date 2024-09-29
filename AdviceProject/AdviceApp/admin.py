from django.contrib import admin
from .models import EntryItem, Advice

# Register your models here.
admin.site.register(EntryItem)
admin.site.register(Advice)