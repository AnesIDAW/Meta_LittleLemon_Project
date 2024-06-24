from django.test import TestCase
from .models import Menu

# Create your tests here.
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name="IceCream", price="30", inventory="100")
        self.assertEqual(item, "IceCream : 80")