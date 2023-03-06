from django.test import TestCase
from .models import Category, Product, Wishlist
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


class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Test Category')
        Product.objects.create(
            category=Category.objects.get(id=1),
            name='Test Product',
            description='Test description',
            price=9.99,
        )

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_has_sizes_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('has_sizes').verbose_name
        self.assertEqual(field_label, 'has sizes')

    def test_rating_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('rating').verbose_name
        self.assertEqual(field_label, 'rating')

    def test_sku_blank(self):
        product = Product.objects.get(id=1)
        field_blank = product._meta.get_field('sku').blank
        self.assertEqual(field_blank, True)

    def test_object_name_is_name(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.name}'
        self.assertEqual(expected_object_name, str(product))


class WishlistModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser')
        Category.objects.create(name='Test Category')
        Product.objects.create(
            category=Category.objects.get(id=1),
            name='Test Product',
            description='Test description',
            price=9.99,
        )
        Wishlist.objects.create(
            user=user,
        )

    def test_user_label(self):
        wishlist = Wishlist.objects.get(id=1)
        field_label = wishlist._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_products_label(self):
        wishlist = Wishlist.objects.get(id=1)
        field_label = wishlist._meta.get_field('products').verbose_name
        self.assertEqual(field_label, 'products')

    def test_object_name_is_username(self):
        wishlist = Wishlist.objects.get(id=1)
        expected_object_name = f'{wishlist.user.username}'
        self.assertEqual(expected_object_name, str(wishlist))
