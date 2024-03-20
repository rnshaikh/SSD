
import conf

from src.product import Product
from src.cart import Cart
from src.coupon import Coupon
from src.membership import Membership



class GeekAcademy:


    def __init__(self):
        self.cart = Cart()
        self.coupons = {}
        self.memberships = {}
        self.programmes = {}


    def load_coupons(self):

        self.coupons[conf.B4G1] = Coupon(conf.B4G1, conf.ZERO, conf.FOUR, conf.ZERO)
        self.coupons[conf.DEAL_G20] = Coupon(conf.DEAL_G20, conf.TWENTY, conf.ZERO, conf.TEN_THOUSAND)
        self.coupons[conf.DEAL_G5] = Coupon(conf.DEAL_G5, conf.FIVE, conf.TWO, conf.ZERO)


    def load_programmes(self):  

        self.programmes[conf.CERTIFICATION] = Product(conf.CERTIFICATION, conf.THREE_THOUSAND)
        self.programmes[conf.DEGREE] = Product(conf.DEGREE, conf.FIVE_THOUSAND)
        self.programmes[conf.DIPLOMA] = Product(conf.DIPLOMA, conf.TWO_FIVE_HUNDRED)


    def load_membership(self):
        self.memberships[conf.PRO_MEMBERSHIP] = Membership(conf.PRO_MEMBERSHIP, conf.PRO_MEMBERSHIP_FEE)
        self.memberships[conf.PRO_MEMBERSHIP].add_discounts(self.programmes[conf.CERTIFICATION], conf.TWO)
        self.memberships[conf.PRO_MEMBERSHIP].add_discounts(self.programmes[conf.DEGREE], conf.THREE)
        self.memberships[conf.PRO_MEMBERSHIP].add_discounts(self.programmes[conf.DIPLOMA], conf.ONE)
