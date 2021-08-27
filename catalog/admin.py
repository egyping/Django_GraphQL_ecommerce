from django.contrib import admin
from .models import Category, Brand, Product, ProductVariant, ProductImages
from mptt.admin import MPTTModelAdmin




admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Brand)

admin.site.register(ProductVariant)
admin.site.register(ProductImages)


class ProductImagesInLine(admin.TabularInline):
    model = ProductImages


class ProductVariantInLine(admin.TabularInline):
    model = ProductVariant


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductVariantInLine,
        ProductImagesInLine,
    ]