
from src.command_invoker import CommandInvoker
from src.command import AddSource, AddDestination, Print
from src.game import Game

class AppConfig:

    def __init__(self):
        self._game_obj = Game()

    def get_command_invoker(self):

        command_invoker_obj = CommandInvoker()
        command_invoker_obj.register_command("SOURCE", AddSource(self._game_obj))
        command_invoker_obj.register_command("DESTINATION", AddDestination(self._game_obj))
        command_invoker_obj.register_command("PRINT_POWER", Print(self._game_obj))
        return command_invoker_obj
