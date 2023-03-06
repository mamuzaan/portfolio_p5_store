from django.test import TestCase
from .models import Category
from django.contrib.auth.models import User


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Test Category')

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_friendly_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('friendly_name').verbose_name
        self.assertEqual(field_label, 'friendly name')

    def test_get_friendly_name(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.get_friendly_name(), None)
