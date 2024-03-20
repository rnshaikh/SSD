import sys
import conf

from heapq import heappop, heappush

from src.coupon import Coupon 
from src.product_type import ProductType


class Invoice:

    def __init__(self, cart):
        self._cart = cart

    @property
    def cart(self):
        return self._cart
    
    def get_total_membership_discount(self):

        discount = 0
        if not self.cart.membership:
            return discount, self.cart.membership

        for cart_unit in self.cart.units:
            temp_price = self.cart.membership.get_discount(cart_unit.product.type)
            discount += (temp_price*cart_unit.quantity)
        return discount, self.cart.membership


    def compare_product_cost(self, price, product):
        if price < product.cost:
            return True

    def get_lowest_value_prodgramme(self):

        price , product = heappop(self.cart.product_heap)
        if self.cart.membership:
            price = price - (price * self.cart.membership.discounts[product.type].discount)
        heappush(self.cart.product_heap, (price, product))
        return price


    def apply_coupon(self, price, no_of_product):

        if (price >= self.cart.coupon.min_purcased_cost 
            and no_of_product >= self.cart.coupon.min_programme):
            return self.cart.coupon

    def get_total_coupons_discount(self, price):

        no_of_product =  self.cart.get_product_count()
        discount = self.get_lowest_value_prodgramme()
        
        if no_of_product >= conf.FOUR:
            coupon = Coupon(conf.B4G1, conf.ZERO, conf.FOUR, conf.ZERO)
            return discount, coupon

        coupon = self.apply_coupon(price, no_of_product)
        discount = 0
        if coupon:
            discount = coupon.discount * price
        return discount, coupon