from django.contrib import admin

# Register your models here.

from .models import Podmiot
class PodmiotAdmin(admin.ModelAdmin):
    ordering = ['id']
admin.site.register(Podmiot,PodmiotAdmin)