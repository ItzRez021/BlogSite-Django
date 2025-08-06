from django.contrib import admin
from .models import *

class TableTitleInline(admin.TabularInline):
    model = TableTitle
    extra = 1

class TableTitleInfoInline(admin.TabularInline):
    model = TableTitleInfo
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title']
    readonly_fields = ['created']
    inlines = [TableTitleInline,TableTitleInfoInline]

admin.site.register(Blog,BlogAdmin)