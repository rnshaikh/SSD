

class Receiver:

    def __init__(self):
        self.val = 0

    def get_value(self):
        return self.val

    def execute(self, operator, operand):

        if operator == "+":
            self.val = self.val + operand
        elif operator == "-":
            self.val = self.val - operand
        elif operator == "*":
            self.val = self.val * operand
        elif operator == "/":
            self.val = self.val / operand
        else:
            raise("Invalid operation")

    def undo(self, operator, operand):

        if operator == "+":
            self.val = self.val - operand
        elif operator == "-":
            self.val = self.val + operand
        elif operator == "*":
            self.val = self.val / operand
        elif operator == "/":
            self.val = self.val * operand

