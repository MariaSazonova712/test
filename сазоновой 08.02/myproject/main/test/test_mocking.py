from django.tests import TestCase
from .models import Product

class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name='Тестовый товар', place='Объём тестовый', price=100, square=5)

    def test_name_label(self):
        task = Product.objects.get(id=1)
        field_label = task._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название товара')

    def test_place_label(self):
        task = Product.objects.get(id=1)
        field_label = task._meta.get_field('place').verbose_name
        self.assertEquals(field_label, 'Объём')

    def test_price_label(self):
        task = Product.objects.get(id=1)
        field_label = task._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'Цена')

    def test_square_label(self):
        task = Product.objects.get(id=1)
        field_label = task._meta.get_field('square').verbose_name
        self.assertEquals(field_label, 'Количество')