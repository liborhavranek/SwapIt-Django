from django.db.models import QuerySet
from django.views.generic import ListView
from .models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'

    def get_queryset(self) -> QuerySet[Category]:
        return Category.objects.filter(parent__isnull=True, is_visible=True).order_by('position')
