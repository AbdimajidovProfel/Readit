from django.contrib import admin
from .models import *


admin.site.register(User)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'created']


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['tag', ]


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created']

@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ['message']



