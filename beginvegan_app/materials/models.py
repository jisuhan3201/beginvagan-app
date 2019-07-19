from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class MaterialCategory(TimeStampedModel):

    name = models.CharField(max_length=100, null=True, blank=True)
    sub_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = 'material_categories'


# class MeterialSubCategory(TimeStampedModel):

#     name = models.CharField(max_length=100, null=True, blank=True)
#     parent_category = models.ForeignKey(MaterialCategory, on_delete=models.SET_NULL, null=True, related_name="parent_category")

#     def __str__(self):
#         return "{}".format(self.name)

#     class Meta:
#         db_table = 'material_subcategories'


class Material(TimeStampedModel):

    name = models.CharField(max_length=100, null=True, blank=True)
    eng_name = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=100, null=True, blank=True)
    code_name = models.CharField(max_length=100, null=True, blank=True)
    is_use = models.BooleanField(default=False)
    raw_last_update = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(MaterialCategory, on_delete=models.SET_NULL, null=True, related_name="category")
    
    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = 'materials'


class VegetarianStage(TimeStampedModel):

    stage = models.CharField(max_length=100, null=True, blank=True)
    materials = models.ManyToManyField(Material)

    def __str__(self):
        return "{}".format(self.stage)

    class Meta:
        db_table = 'vegetarian_stage'
