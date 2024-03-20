from abc import ABC, abstractmethod
 
import conf
from src.printer import InvoicePrinter
from src.invoice import Invoice


class Command(ABC):

    def __init__(self, reciever):

        self.reciever = reciever

    @abstractmethod 
    def process(self, *args):
        pass


class AddProgrammeCommand(Command):

    def __init__(self, reciever):
        self.reciever = reciever

    def process(self, *args):
        product = self.reciever.programmes[args[conf.ZERO]]
        self.reciever.cart.add_units(product, int(args[conf.ONE]))


class ApplyCouponCommand(Command):

    def __init__(self, reciever):
        self.reciever = reciever

    def process(self, *args):
        coupon = self.reciever.coupons[args[conf.ZERO]]
        self.reciever.cart.add_coupon(coupon)


class AddProMembershipCommand(Command):


    def __init__(self, reciever):
        self.reciever = reciever

    def process(self, *args):

        membership = self.reciever.memberships[conf.PRO_MEMBERSHIP]
        self.reciever.cart.add_membership(membership)


class PrintCommand(Command):

    def __init__(self, reciever):
        self.reciever = reciever

    def process(self, *args):

        invoice_obj = Invoice(self.reciever.cart)
        printer = InvoicePrinter(invoice_obj)
        printer.print()

