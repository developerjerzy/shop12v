from django.contrib import admin
from .models import Category, Product, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Класс отвечает за регистрацию в административной части
    категорий товара.
    """

    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Класс отвечает за регистрацию в администранивной части
    продукта. Заполнение информации о продукте.
    """
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Класс отвечает за регистрацию в административной части сайта
    информации о комментариях товара
    """
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')