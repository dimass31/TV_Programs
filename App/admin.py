from django.contrib import admin
from .models import Broadcast, SearchResults

class BroadcastAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class SearchResultsAdmin(admin.ModelAdmin):
    list_display = ('word',)
    filter_horizontal = ('search',)

admin.site.register(Broadcast, BroadcastAdmin)
admin.site.register(SearchResults, SearchResultsAdmin)