from django.tests import TestCase
from main.models import Product


class CustomersModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name='Пельмени', place='100', price='7900', square='5')

    def test_first_name_label(self):
        models = Product.objects.get(id=1)
        field_label = models._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Наименование')

    def test_phone_label(self):
        models = Product.objects.get(id=1)
        field_label = models._meta.get_field('quantity').verbose_name
        self.assertEquals(field_label, 'Масса')

    def test_surname_max_length(self):
        models = Product.objects.get(id=1)
        max_length = models._meta.get_field('price').max_length
        self.assertEquals(max_length, 100)

    def test_get_absolute_url(self):
        models = Product.objects.get(id=1)
        self.assertEquals(models.get_absolute_url(), 'myproject/1')