from django.contrib import admin
from .models import Files, Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('c00', 'c06',  'c03', 'c07', 'c05',)

class FileAdmin(admin.ModelAdmin):
    pass # date_hierarchy = 'dateadded'

admin.site.register(Movie, MovieAdmin)
admin.site.register(Files, FileAdmin)
