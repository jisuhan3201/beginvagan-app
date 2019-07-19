from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

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
    
    readonly_fields = ('image', 'title')

    def image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
            )
    )