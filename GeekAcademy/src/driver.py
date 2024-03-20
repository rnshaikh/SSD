from src.app_config import AppConfig


class Driver:


    def __init__(self, path):
        self.config = AppConfig()
        self._path = path


    def process_command(self):

        invoker_obj = self.config.get_command_invoker()
        
        with open(self._path, 'r') as fobj:
            for row in fobj:
                row = row.strip()
                commands = row.split(" ")
                invoker_obj.execute_command(commands[0], *commands[1:])

