
from src.app_config import AppConfig



class Driver:

    def __init__(self, path):
        self._path = path
        self._app_config = AppConfig()

    def process_file(self):
        with open(self._path, 'r') as fobj:
            for row in fobj:
                row = row.strip()
                commands = row.split(" ")
                command_invoker_obj = self._app_config.get_command_invoker()
                command_invoker_obj.execute_command(commands[0], *commands[1:])
