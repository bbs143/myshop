from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'slug', 'price', 'created_at']
    list_filter = ['category', 'price', 'created_at']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)
