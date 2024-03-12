import django_filters
from .models import Product


class PostFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name')
    price = django_filters.CharFilter(field_name='price')
    manufacturer = django_filters.CharFilter(field_name='manufacturer')

    class Meta:
        model = Product
        fields = ['name','price', 'manufacturer']
