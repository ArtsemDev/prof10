from django.contrib import admin

from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name', )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('category', 'author')
    search_fields = ('title', 'body')
    date_hierarchy = 'date_created'
    prepopulated_fields = {'slug': ('title', )}
    readonly_fields = ('date_created', )

# admin.site.register(Category)
# admin.site.register(Post)
