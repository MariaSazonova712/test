from unittest import skip
from django.test import TransactionTestCase
from main.models import Product


@skip('Пропускаю тест транзакции')
class WidgetTransactionTestCase(TransactionTestCase):
    def test_widget_creation(self):
        Product.objects.create(name='Наменования 1')
        Product.objects.create(name='Наменования 2')
        self.assertEqual(Product.objects.count(), 2)