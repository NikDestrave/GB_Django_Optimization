from django.db import models


class CatalogCategory(models.Model):
    name = models.CharField(verbose_name="Название", max_length=64, unique=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(CatalogCategory, on_delete=models.CASCADE)
    id_class = models.CharField(verbose_name="id класса", max_length=15)
    src = models.ImageField(upload_to="products_images", blank=True)
    name = models.CharField(verbose_name="Название", max_length=64, unique=True)
    price = models.DecimalField(verbose_name="Цена", max_digits=8, decimal_places=2, default=0)
    id_button = models.CharField(verbose_name="id кнопки", max_length=10)
    is_active = models.BooleanField(verbose_name='активна', default=True)
    quantity = models.DecimalField(verbose_name='количество', max_digits=8, decimal_places=0, default=0)

    def __str__(self):
        return f'{self.name} ({self.category} )'

    @staticmethod
    def get_items():
        return Product.objects.filter(is_active=True).order_by('category', 'name')
