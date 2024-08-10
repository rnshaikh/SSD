

class CommandInvoker:

    def __init__(self):
        self._commands = {}

    def register_command(self, command, obj):
        self._commands[command] = obj

    def execute_command(self, command, *args):
        self._commands[command].process(*args)