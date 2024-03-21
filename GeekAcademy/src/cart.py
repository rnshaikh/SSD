import sys
from heapq import heappush

import conf
from src.product_type import ProductType
from src.coupon import Coupon


class CartUnit:

    def __init__(self, product, quantity):

        self._product = product
        self._quantity = quantity
    
    @property
    def product(self):
        return self._product
    
    @property
    def quantity(self):
        return self._quantity
    
    def get_total_price(self):
        return self.product.cost * self.quantity


class Cart:
    def __init__(self):
        self.units = []
        self.product_heap = []
        self.membership_units = []
        self.membership = None
        self.coupon = None

    def add_units(self, product, quantity):

        cart_unit = CartUnit(product, quantity)
        self.units.append(cart_unit)
        heappush(self.product_heap, (product.cost, product))
        
    def add_membership(self, membership):
        if not self.membership:
            self.membership = membership

    def add_coupon(self, coupon):

        if not self.coupon:
            self.coupon = coupon
            return

        if self.coupon and self.coupon.discount < coupon.discount:
            self.coupon = coupon
    
    def get_total_price(self):

        price = 0
        for cart_unit in self.units:
            price += cart_unit.get_total_price()
        return price

    def get_product_count(self):

        count = 0
        for cart_unit in self.units:
            count += cart_unit.quantity
        return count
