from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, primary_key=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField('description')
    price = models.DecimalField(max_digits=100, decimal_places=2)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='pr',
                                 verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'


