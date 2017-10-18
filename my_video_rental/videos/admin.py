from django.contrib import admin
from . import models
# Register your models here.
class MovieAdmin(admin.ModelAdmin):

	fields = ['release_year', 'title', 'length']
	
	search_fields = ['title', 'length']
	
	list_filter = ['rease_year', 'length', 'title']
	
	list_desplay = ['title', 'rease_year', 'length']

admin.site.register(models.Customer)
admin.site.register(models.Movie, ModelAdmin)
