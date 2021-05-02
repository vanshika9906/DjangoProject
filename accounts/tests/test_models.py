"""
    Unit test file for models
"""
from django.contrib.auth.models import User
from django.test import TestCase

from accounts.models import Customer, Product, Order, Tag


class UserModelTest(TestCase):
    """
    Test Model class
    """
    print("Running User Model Test")

    def setUp(self):
        """
        :return: None
        """
        # Setting up objects which can be use for all test methods
        self.user = User.objects.create(username="testUser", password="1q2w3e4r5tA", email="test@user.com",
                                        first_name="test", last_name="test")
        self.user.save()

    def test_username(self):
        """
        :return: None
        """
        user = User.objects.get(id=1)
        username = user.username
        self.assertEqual(username, 'testUser')

    def test_user_email(self):
        """
        :return: None
        """
        user = User.objects.get(id=1)
        email = user.email
        self.assertEqual(email, 'test@user.com')

    def test_user_first_name(self):
        """
        :return: None
        """
        user = User.objects.get(id=1)
        first_name = user.first_name
        self.assertEqual(first_name, 'test')

    def test_user_last_name(self):
        """
        :return: None
        """
        user = User.objects.get(id=1)
        last_name = user.last_name
        self.assertEqual(last_name, 'test')

    def tearDown(self):
        self.user.delete()


class CustomerModelTest(TestCase):
    """
    Test Model class
    """
    print("Running Customer Model Test")

    def setUp(self):
        """
        :return: None
        """
        # Setting up objects which can be use for all test methods
        self.user = Customer.objects.create(name="testUser", phone="0070070077", email="test@user.com")
        self.user.save()

    def test_name(self):
        """
        :return: None
        """
        customer = Customer.objects.get(id=1)
        name = customer.name
        self.assertEqual(name, 'testUser')

    def test_user_email(self):
        """
        :return: None
        """
        customer = Customer.objects.get(id=1)
        email = customer.email
        self.assertEqual(email, 'test@user.com')

    def test_user_phone(self):
        """
        :return: None
        """
        customer = Customer.objects.get(id=1)
        phone = customer.phone
        self.assertEqual(phone, '0070070077')

    def tearDown(self):
        self.user.delete()


class TagModelTest(TestCase):
    """
    Test Model class
    """
    print("Running Tag Model Test")

    def setUp(self):
        """
        :return: None
        """
        # Setting up objects which can be use for all test methods
        self.user = Tag.objects.create(name="testUser")
        self.user.save()

    def test_tag(self):
        """
        :return: None
        """
        tag = Tag.objects.get(id=1)
        name = tag.name
        self.assertEqual(name, 'testUser')

    def tearDown(self):
        self.user.delete()


class ProductModelTest(TestCase):
    """
    Test Model class
    """
    print("Running Product Model Test")

    def setUp(self):
        """
        :return: None
        """
        # Setting up objects which can be use for all test methods
        self.user = Product.objects.create(name="testUser", price="46", category="Fruits",
                                           description="test user description")
        self.user.save()

    def test_name(self):
        """
        :return: None
        """
        product = Product.objects.get(id=1)
        name = product.name
        self.assertEqual(name, 'testUser')

    def test_price(self):
        """
        :return: None
        """
        product = Product.objects.get(id=1)
        price = product.price
        self.assertEqual(price, 46.0)

    def test_category(self):
        """
        :return: None
        """
        product = Product.objects.get(id=1)
        category = product.category
        self.assertEqual(category, 'Fruits')

    def test_description(self):
        """
        :return: None
        """
        product = Product.objects.get(id=1)
        description = product.description
        self.assertEqual(description, 'test user description')

    def tearDown(self):
        self.user.delete()


class OrderModelTest(TestCase):
    """
    Test Model class
    """
    print("Running Order Model Test")

    def setUp(self):
        """
        :return: None
        """
        # Setting up objects which can be use for all test methods
        self.user = Order.objects.create(status="Crates loaded on Truck", note="Its being delivered")
        self.user.save()

    def test_status(self):
        """
        :return: None
        """
        order = Order.objects.get(id=1)
        status = order.status
        self.assertEqual(status, 'Crates loaded on Truck')

    def test_note(self):
        """
        :return: None
        """
        order = Order.objects.get(id=1)
        note = order.note
        self.assertEqual(note, 'Its being delivered')

    def tearDown(self):
        self.user.delete()
