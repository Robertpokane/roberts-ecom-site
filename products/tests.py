from django.test import TestCase
from .models import Product
# Create your tests here.


class ProductTest(TestCase):
    """ Here we'll define the tests that we'll run against our produt models """
    
    def test_str(self):
        test_name = Product(name='A Product')
        self.assertEqual(str(test_name), 'A Product')