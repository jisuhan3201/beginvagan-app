from django.db import models

# Create your models here.

class MaterialCategory(models.Model):

    name = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = 'material_categories'


class MetarialSubCategory(models.Model):

    name = models.CharField(max_length=100, null=True, blank=True)
    parent_category = models.ForeignKey(MaterialCategory, on_delete=models.SET_NULL, null=True, related_name="parent_category")
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = 'material_subcategories'


class Material(models.Model):

    name = models.CharField(max_length=100, null=True, blank=True)
    eng_name = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=100, null=True, blank=True)
    code_name = models.CharField(max_length=100, null=True, blank=True)
    is_use = models.BooleanField(default=False)
    last_update = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(MaterialCategory, on_delete=models.SET_NULL, null=True, related_name="category")
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = 'materials'


class VegetarianStage(models.Model):

    stage = models.CharField(max_length=100, null=True, blank=True)
    materials = models.ManyToManyField(Material)
    
    def __str__(self):
        return "{}".format(self.stage)

    class Meta:
        db_table = 'vegetarian_stage'
