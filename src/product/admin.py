from django.contrib import admin
from .models import Variant, Product, ProductImage, ProductVariant, ProductVariantPrice

@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'created_at', 'updated_at']
    search_fields = ['title']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'sku', 'created_at', 'updated_at']
    search_fields = ['title', 'sku']

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'file_path', 'created_at', 'updated_at']
    search_fields = ['product__title']

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['variant_title', 'variant', 'product', 'created_at', 'updated_at']
    search_fields = ['variant_title', 'variant__title', 'product__title']

@admin.register(ProductVariantPrice)
class ProductVariantPriceAdmin(admin.ModelAdmin):
    list_display = ['product_variant_one', 'product_variant_two', 'product_variant_three', 'price', 'stock', 'product', 'created_at', 'updated_at']
    search_fields = ['product_variant_one__variant_title', 'product_variant_two__variant_title', 'product_variant_three__variant_title', 'product__title']
