from django.contrib import admin

# Register your models here.
from django.contrib import admin
from viewbooks.models import *

class AdminSearch(admin.ModelAdmin):
    list_display = ('id', 'title', 'barcode')
    list_display_links = ('id', 'title')
    search_fields = ('barcode',)
    list_filter = ('id',)

admin.site.register(UzbBooksModel, AdminSearch)
admin.site.register(RusBooksModel, AdminSearch)
admin.site.register(EngBooksModel, AdminSearch)
admin.site.register(UzBuyModel)
admin.site.register(RusBuyModel)
admin.site.register(EngBuyModel)