from django.contrib import admin
from . import models
# Register your models here.
class MovieAdmin(admin.ModelAdmin):

	fields = ['release_year', 'title', 'length']
	
	search_fields = ['title', 'length']
	
	filter_list = ['rease_year', 'length', 'title']

admin.site.register(models.Customer)
admin.site.register(models.Movie, ModelAdmin)
