from django.contrib import admin
from . import models
from django.utils.html import format_html

def get_picture_preview(obj):

    return format_html('<img src="{}" height="300"/>'.format(obj.image.url))


# @admin.register(models.ProductImage)
class ProductImageAdmin(admin.StackedInline):
    model = models.ProductImage
    extra = 0
    fields = [get_picture_preview]
    readonly_fields = [get_picture_preview]
    # list_display = (
    #     "image_tag",
    #     'id',
    #     "title",
    #     "image",
    # )

    # def image_tag(self, obj):
    #     return format_html('<img src="{}" height="300"/>'.format(obj.image.url))

# @admin.register(models.ProductMaterial)
class ProductMaterialAdmin(admin.StackedInline):
    model = models.ProductMaterial
    # list_display = (
    #     "id",
    #     "product",
    #     "material",
    #     "updated_at",

    # )

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "category",
        "company",
        "updated_at",
        "created_at"
    )
    search_fields = ['materials_set__name']
    inlines = [ProductImageAdmin, ProductMaterialAdmin]


@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "sub_category",
        "updated_at",
        "created_at"
    )


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "updated_at",
        "created_at"
    )

