
class Invoker:

    def __init__(self):
        self.stack = []

    def execute(self, cmd):
        cmd.execute()
        self.stack.append(cmd)

    def undo(self):
        cmd = self.stack.pop()
        cmd.undo()
