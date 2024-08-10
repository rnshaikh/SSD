from abc import ABC, abstractmethod


class Command(ABC):

    def __init__(self, receiver):
        self._receiver = receiver

    @abstractmethod
    def process(self, *args):
        self.process(*args)


class AddSource(Command):

    def process(self, *args):
        self._receiver.add_source(*args)


class AddDestination(Command):

    def process(self, *args):
        self._receiver.add_destination(*args)


class Print(Command):

    def process(self):
        self._receiver.print_out()