from django.db import models
from django.db.models import QuerySet


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')
    position = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    svg = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['position']

    def __str__(self) -> str:
        return self.name

    def get_subcategories(self) -> QuerySet['Category']:
        return self.subcategories.filter(is_visible=True).order_by('position')
    #
    # def get_product_count(self):
    #     return self.products.filter(is_active=True).count()  # Tohle upravíme později, až přidáme produkty
