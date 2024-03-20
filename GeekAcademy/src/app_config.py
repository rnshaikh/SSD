from src.command import (AddProgrammeCommand, ApplyCouponCommand, AddProMembershipCommand,
                         PrintCommand)

from src.command_invoker import CommandInvoker

from src.geek_academy import GeekAcademy


class AppConfig:

    def __init__(self):
        self.geek_academy = GeekAcademy()
        self.geek_academy.load_coupons()
        self.geek_academy.load_programmes()
        self.geek_academy.load_membership()
        
    def get_command_invoker(self):

        command_invoker_obj = CommandInvoker()
        command_invoker_obj.register("ADD_PROGRAMME", AddProgrammeCommand(self.geek_academy))
        command_invoker_obj.register("APPLY_COUPON", ApplyCouponCommand(self.geek_academy))
        command_invoker_obj.register("ADD_PRO_MEMBERSHIP", AddProMembershipCommand(self.geek_academy))
        command_invoker_obj.register("PRINT_BILL", PrintCommand(self.geek_academy))
        return command_invoker_obj
