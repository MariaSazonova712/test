from django.db import models


class Product(models.Model):
    objects = None
    number = models.CharField('Номер', max_length=50)
    name = models.CharField('Наименование', max_length=50)
    price = models.CharField('Цена', max_length=50)
    quantity = models.CharField('Количество', max_length=50)
    manufacturer = models.CharField('Производитель', max_length=50)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
