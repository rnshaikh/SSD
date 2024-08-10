import io
import sys

from unittest import TestCase

from src.app_config import AppConfig


class GManTest(TestCase):

    @classmethod
    def setUp(self):
        self._app_config = AppConfig()
        self._command_invoker = self._app_config.get_command_invoker()
        

    def test_power(self):

        self._command_invoker.execute_command("SOURCE", "2", "1", "E")
        self._command_invoker.execute_command("DESTINATION", "4", "3")

        output = io.StringIO()
        sys.stdout = output
        self._command_invoker.execute_command("PRINT_POWER")
        sys.stdout = sys.__stdout__
        ans = output.getvalue().strip()
        self.assertTrue("POWER  150" in ans)

    def test_power_negative(self):

        self._command_invoker.execute_command("SOURCE", "0", "5", "W")
        self._command_invoker.execute_command("DESTINATION", "6", "1")

        output = io.StringIO()
        sys.stdout = output
        self._command_invoker.execute_command("PRINT_POWER")
        sys.stdout = sys.__stdout__
        ans = output.getvalue().strip()

        self.assertFalse("POWER  160" in ans)
