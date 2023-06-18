class Screen:

    def __init__(self, msg=None):
        self.msg = msg

    def print_(self, msg):
        print(msg)

    def print_msg_input(self, msg):
        ch = input(msg)
        return ch
