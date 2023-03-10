from django.contrib import admin
from .models import Product, Category, Wishlist, Comment


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'user',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'text',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Comment, CommentAdmin)
