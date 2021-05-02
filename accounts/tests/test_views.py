"""
    Unit test file for view
"""
from collections import OrderedDict

from django.contrib.auth.models import User
from django.test import TestCase

from accounts.models import *


class LoginViewTest(TestCase):
    """
    Test View  class
    """
    print("Running Login View Tests")

    def setUp(self):
        """
        :return: None
        """
        self.user = User.objects.create(username="testUser", password="1q2w3e4r5tA", email="test@user.com",
                                        first_name="test", last_name="test")
        self.user.save()

    def test_correct(self):
        """
        :return: None
        """
        self.client.login(username='wrong', password='1q2w3e4r5tA')
        response = self.client.get('/home')
        self.assertTrue(response.status_code, 404)

    def test_wrong_username(self):
        """
        :return: None
        """
        self.client.login(username='wrong', password='1q2w3e4r5tA')
        response = self.client.get('/login')
        # print("response", response)
        self.assertTrue(response.status_code, 302)

    def test_wrong_password(self):
        """
        :return: None
        """
        self.client.login(username='testUser', password='wrong')
        response = self.client.get('/login')
        self.assertTrue(response.status_code, )

    def tearDown(self):
        self.user.delete()


class AllViewTest(TestCase):
    """
    Test View  class
    """
    print("Running Create Order View Tests")

    def setUp(self):
        """
        :return: None
        """
        self.user = User.objects.create(username="testUser", password="1q2w3e4r5tA", email="test@user.com",
                                        first_name="test", last_name="test")
        self.user.save()

        self.client.login(username='testUser', password='1q2w3e4r5tA')

        self.customer = Customer.objects.create(name="Jane", email="jane@doe.com", phone="07927437427")
        self.customer.save()

        self.tag = Tag.objects.create(name="i_dont_know")
        self.tag.save()

        self.product = Product.objects.create(name="Tomato", price=50.0, category="Fruits",
                                              description="I am a juicy red tomato", )
        self.product.save()

    # def test_create_customer(self):
    #     """
    #     :return: None
    #     """
    #     self.client.get('/create_order/1')
    #     self.customer = Customer.objects.create(name="Jane", email="jane@doe.com", phone="07927437427")
    #     self.customer.save()

    # def test_create_tag(self):
    #     """
    #     :return: None
    #     """
    #     # self.client.get('/create_order/1')
    #     self.tag = Tag.objects.create(name="idotknow")
    #     self.tag.save()

    # def test_create_product(self):
    #     """
    #     :return: None
    #     """
    #     # self.client.get('/create_order/1')
    #     self.product = Product.objects.create(name="Tomato", price=50.0, category="Fruits",
    #                                           description="I am a juicy red tomato")
    #     self.product.save()

    def test_create_order(self):
        """
        :return: None
        """

        customer = Customer.objects.all().values()
        customer_value = customer[0]
        # print(customer_value['name'])
        tag = Tag.objects.all().values()
        tag_value = tag[0]
        # print(tag_value['name'])
        products = Product.objects.all().values()
        products_value = products[0]
        # print(products_value['name'])
        self.order = Order.objects.create(product_id=products_value['id'], customer_id=customer_value['id'],
                                          status="In Delivery")
        self.order.save()
        order_all = Order.objects.all().values()
        order_value = order_all[0]
        # print(order_all)
        response = self.client.get('/create_order/' + str(order_value['id']))
        print(response)
        self.assertTrue(order_all, {'order': [OrderedDict([('id', 1),
                                                           ('product_id', 1),
                                                           ('customer_id', 1),
                                                           ('status', "In Delivery")])]})

    def tearDown(self):
        self.user.delete()
