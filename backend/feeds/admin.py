from django.contrib import admin
from .models import  Feed, Item

@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'url','created_at']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'link','pub_date','feed']

