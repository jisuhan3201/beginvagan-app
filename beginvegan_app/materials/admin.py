from django.contrib import admin
from . import models

@admin.register(models.Material)
class MaterialAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "eng_name",
        "code",
        "code_name",
        "is_use",
        "raw_last_update",
        "category",
        "updated_at",
        "created_at"
    )


@admin.register(models.MaterialCategory)
class MaterialCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "updated_at",
        "created_at"
    )

@admin.register(models.VegetarianStage)
class VegetarianStageAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "stage",
        "updated_at",
        "created_at"
    )