from unittest import skip
from django.test import LiveServerTestCase
from selenium import webdriver
from myapp.models import Product
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class NameFunctionalTest(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        super().setUp()

    def tearDown(self):
        self.selenium.quit()
        super().tearDown()

    def test_product_list_functional(self):
        # Create tests data
        Product.objects.create(name='Наименование')
        Product.objects.create(name='Парфюмерия')

        # Simulate user interactions using Selenium
        self.selenium.get(self.live_server_url + '/myproject/')
        self.assertIn('Список Товаров', self.selenium.title)
        names = self.selenium.find_elements(By.TAG_NAME, 'td')
        self.assertEqual(len(names), 2)
        self.assertEqual(names[0].text, 'Наименование')
        self.assertEqual(names[1].text, 'Наименование')