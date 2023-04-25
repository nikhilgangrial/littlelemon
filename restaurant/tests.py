import datetime

from django.test import TestCase
from .models import Menu, Booking


class MenuTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(name="Potato", price="20", menu_item_description="Just a harmless Potato")
        Menu.objects.create(name="Creamed Broccoli Soup", price="10", menu_item_description="Healthy vegetable soup")

    def test_menu_item(self):
        potato = Menu.objects.get(name="Potato")
        ice_cream = Menu.objects.get(name="Creamed Broccoli Soup")
        self.assertEqual(str(potato), 'Potato')
        self.assertEqual(potato.menu_item_description, "Just a harmless Potato")
        self.assertEqual(ice_cream.price, 10.0)
        self.assertEqual(ice_cream.price, 10)


class BookingTest(TestCase):
    def setUp(self):
        Booking.objects.create(first_name="Potato", reservation_date="2023-11-22", reservation_slot=19)
        Booking.objects.create(first_name="Creamed Broccoli Soup", reservation_date="2010-01-31", reservation_slot=17)

    def test_booking(self):
        potato = Booking.objects.get(first_name="Potato")
        ice_cream = Booking.objects.get(first_name="Creamed Broccoli Soup")
        self.assertEqual(str(potato), 'Potato')
        self.assertEqual(ice_cream.reservation_date, datetime.date(2010, 1, 31))
        self.assertEqual(potato.reservation_slot, 19)
