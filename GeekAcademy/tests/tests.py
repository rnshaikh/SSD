import io
import sys
import conf

from unittest import TestCase
from src.app_config import AppConfig


class AcademyTestCase(TestCase):


    @classmethod
    def setUp(cls):
        cls.app_config = AppConfig()
        cls.invoker_obj = cls.app_config.get_command_invoker()

    def test_add_program(self):
        self.invoker_obj.execute_command("ADD_PROGRAMME", "DIPLOMA", 1)
        self.invoker_obj.execute_command("ADD_PROGRAMME", "CERTIFICATION", 1)
        self.assertTrue(2, self.invoker_obj.commands["ADD_PROGRAMME"].reciever.cart.get_product_count())

    def test_add_membership(self):
        self.invoker_obj.execute_command("ADD_PRO_MEMBERSHIP")
        self.assertTrue(True, self.invoker_obj.commands["ADD_PRO_MEMBERSHIP"].reciever.cart.membership)

    def test_add_coupon(self):
        self.invoker_obj.execute_command("APPLY_COUPON", "DEAL_G20")
        self.assertTrue("DEAL_G20", self.invoker_obj.commands["ADD_PRO_MEMBERSHIP"].reciever.cart.coupon.name)

    def test_invoice(self):

        output = io.StringIO()
        sys.stdout = output
        self.invoker_obj.execute_command("ADD_PROGRAMME", "DIPLOMA", 1)
        self.invoker_obj.execute_command("ADD_PROGRAMME", "CERTIFICATION", 1)
        self.invoker_obj.execute_command("ADD_PRO_MEMBERSHIP")
        self.invoker_obj.execute_command("APPLY_COUPON", "DEAL_G20")
        self.invoker_obj.execute_command("PRINT_BILL")
        sys.stdout = sys.__stdout__
        ans = output.getvalue().strip()
        self.assertTrue("TOTAL 6115.00" in ans)
