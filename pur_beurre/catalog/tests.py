from django.test import TestCase, client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.management import call_command
from io import StringIO
from .models import Product, Category, UserFavorite

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
		Chocolat = str('Chocolat')
		response = self.client.get(reverse('catalog:search'), {
			'query': Chocolat,
		})
		self.assertEqual(response.status_code, 200)

	def test_search_page_redirect_302(self):
		Chocolat = str('invalid name')
		response = self.client.get(reverse('catalog:search'), {
			'query': Chocolat,
		})
		self.assertEqual(response.status_code, 302)