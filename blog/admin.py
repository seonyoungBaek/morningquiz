from django.contrib import admin
from . import models
# Register your models here.




@admin.register(models.Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Articles)
class ArticlesModelAdmin(admin.ModelAdmin):

    """Post Model Admin Definition"""

    list_display = (
        "title",
        "content",
        "category",
    )

    list_filter = ("category",)