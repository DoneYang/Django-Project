from django.contrib import admin
from .models import BookComment, Category, Auther, Book

class BookStackinline(admin.StackedInline):
    model = BookComment

class BookTabularinline(admin.TabularInline):
    model = BookComment
    extra = 1



class Bookconfig(admin.ModelAdmin):
    list_display = ['showImage', 'name', 'price', 'level','category', 'published']
    search_fields = ['name', 'category']
    list_filter = ['price']
    prepopulated_fields = {'slug':['name']}
    fieldsets = (
        (None, {'fields': ['code', 'slug', 'name', 'description', 'price', 'level', 'image', 'published']}),
        ('Category', {'fields': ['category', 'author'], 'classes': ['collapse']}),
    )
    inlines = [BookTabularinline]

# Register your models here.
admin.site.register(Category)
admin.site.register(Auther)
admin.site.register(Book, Bookconfig)