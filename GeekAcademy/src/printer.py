import conf

from abc import ABC, abstractmethod



class Printer(ABC):

    @abstractmethod
    def print():
        pass


class InvoicePrinter(Printer):


    def __init__(self, invoice):
        self.invoice = invoice

    def print(self):
        
        price = self.invoice.cart.get_total_price()
        membership_discount, membership = self.invoice.get_total_membership_discount()
        enrollment_fee = 0
        membership_fee = 0

        if price < conf.ENROLLMENT_FEE_LIMIT:
            enrollment_fee = conf.ENROLLMENT_FEE

        if membership:
            membership_fee = membership.cost

        sub_total = price + membership_fee - membership_discount
        coupons_discount, coupon = self.invoice.get_total_coupons_discount(sub_total)
        
        print("SUB_TOTAL %.2f" %(sub_total))
        print("COUPON_DISCOUNT %s %.2f" %(coupon.name if coupon else "NONE", coupons_discount))
        print("TOTAL_PRO_DISCOUNT %.2f" %membership_discount)
        print("PRO_MEMBERSHIP_FEE %.2f" %membership_fee)
        print("ENROLLMENT_FEE %.2f" %enrollment_fee)
        print("TOTAL %.2f" %(sub_total-coupons_discount+enrollment_fee))


        

