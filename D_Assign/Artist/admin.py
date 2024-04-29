from django.contrib import admin
from .models import Work, Artist_t
# Register your models here.

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['link', 'work_type']

@admin.register(Artist_t)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']