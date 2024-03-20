

class CommandInvoker:

    def __init__(self):
        self.commands = {}

    def register(self, command_name, command):
        self.commands[command_name] = command

    def execute_command(self, command, *args):
        self.commands[command].process(*args)
