from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import *

class YotAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')# Редактирыемые поля!
    readonly_fields = ('time_create', 'time_update', 'get_html_photo') #Не редактируемые поля!
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>") #mark_safe не экранирует тэги

    get_html_photo.short_description = "Миниатюра" #Замена имени на Мениатюра!

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(tablica, YotAdmin)
admin.site.register(Category, CategoryAdmin)
