from django.contrib import admin
from .models import Post
# from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Category
# from .models Tag, Comment

admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

# admin.site.register(Category, CategoryAdmin)

# class TagAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name',)}

# admin.site.register(Tag, TagAdmin)


