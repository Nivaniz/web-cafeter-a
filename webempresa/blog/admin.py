from django.contrib import admin
from .models import Category, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated', 'image_tag')
    list_display = ('title', 'author', 'published', 'post_categories',)
    ordering = ('author', 'published')
    search_fields = ('title', 'content',)
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"

    def image_tag(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 200px; max-width: 200px;" />'
        return ''

    image_tag.allow_tags = True
    image_tag.short_description = 'Imagen'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
