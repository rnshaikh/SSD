from command import Command


class CommandInterface(Command):

    def __init__(self, receiver, operator, operand):
        self.receiver = receiver
        self.operator = operator
        self.operand = operand

    def execute(self):
        self.receiver.execute(self.operator, self.operand)

    def undo(self):
        self.receiver.undo(self.operator, self.operand)




