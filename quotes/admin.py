
from django.contrib import admin
from .models import Quote

admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'mood', 'category')