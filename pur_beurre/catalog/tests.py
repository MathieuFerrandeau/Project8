"""test management"""
from django.test import TestCase
from django.urls import reverse
from .models import Product, Category

# Create your tests here.


class IndexPageTestCase(TestCase):

    def test_index_returns_200(self):
        response = self.client.get(reverse('catalog:index'))
        self.assertEqual(response.status_code, 200)


class DataTests(TestCase):

    def setUp(self):
        chocolat = Category.objects.create(name='chocolat')

        Product.objects.create(name='Chocolat',
                               category=chocolat,
                               brand='casino',
                               nutrition_grade='a',
                               picture='chocolat.jpeg',
                               nutrition_image='chocolatnutrigrade.com',
                               url='www.chocolat.com')

    def test_search_returns_200(self):
        chocolat = str('Chocolat')
        response = self.client.get(reverse('catalog:search'), {
            'query': chocolat,
        })
        self.assertEqual(response.status_code, 200)

    def test_search_page_redirect_302(self):
        chocolat = str('invalid name')
        response = self.client.get(reverse('catalog:search'), {
            'query': chocolat,
        })
        self.assertEqual(response.status_code, 302)
