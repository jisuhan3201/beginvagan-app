from django.contrib import admin
from . import models
from django.utils.html import format_html

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "image",
        "category",
        "company",
        "updated_at",
        "created_at"
    )


@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "sub_category",
        "updated_at",
        "created_at"
    )

@admin.register(models.ProductMaterial)
class ProductMaterialAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "product",
        "material",
        "updated_at",

    )

@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "updated_at",
        "created_at"
    )

@admin.register(models.RawImage)
class RawImageAdmin(admin.ModelAdmin):

    list_display = (
        "image_tag",
        'id',
        "title",
        "image",
    )

    def image_tag(self, obj):
        return format_html('<img src="{}" height="300"/>'.format(obj.image.url))
