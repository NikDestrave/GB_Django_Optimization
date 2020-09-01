from django.core.management.base import BaseCommand

from authapp.models import ShopUser
from mainapp.models import CatalogCategory, Product

import json, os


def load_from_json(file_name):
    with open(os.path.join('static', file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        CatalogCategory.objects.all().delete()
        for category in categories:
            new_category = CatalogCategory(**category)
            new_category.save()

        products = load_from_json('catalog')

        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            _category = CatalogCategory.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        # super_user = ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=33)
