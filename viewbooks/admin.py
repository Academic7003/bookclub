from django.contrib import admin

# Register your models here.
from django.contrib import admin
from viewbooks.models import *


admin.site.register(UzbBooksModel)
admin.site.register(RusBooksModel)
admin.site.register(EngBooksModel)
admin.site.register(UzBuyModel)
admin.site.register(RusBuyModel)
admin.site.register(EngBuyModel)