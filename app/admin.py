from django.contrib import admin

# Register your models here.
from app.models import *

class CustomWebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url','email']
    list_display_links=['name','url']
    list_editable=['email']
    search_fields=['name']
    #list_filter=['name']
    list_filter=('name',)
    list_per_page=2

class CustomAccessrecord(admin.ModelAdmin):
    list_display=['name','author','date']
    list_display_links=['name','author']
    list_editable=['date']
    search_fields=['author']
    list_filter=['name']
    #list_per_page=1

admin.site.register(Topic)
admin.site.register(Webpage,CustomWebpage)
admin.site.register(Accessrecord,CustomAccessrecord)

