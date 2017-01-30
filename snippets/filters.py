import django_filters
from snippets.models import Product

class ProductFilter(django_filters.FilterSet):
    likes = django_filters.BooleanFilter(whether_like=True)

    class Meta:
        model = Product
        fields = ['category', 'in_stock', 'min_price', 'max_price']