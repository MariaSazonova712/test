from unittest import skip
from django.test import TestCase
from models import Product


class MyModelTest(TestCase):
    def setUp(self):
        self.object = Product.objects.create(name="Наименование")

    def test_str_representation(self):
        self.assertEqual(str(self.object), 'Пельмени')

    def tearDown(self):
        pass