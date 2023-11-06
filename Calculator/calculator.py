from invoker import Invoker
from command_interface import CommandInterface
from receiver import Receiver


if __name__ == "__main__":

    receiver = Receiver()
    user = Invoker()

    command_int1 = CommandInterface(receiver, "+", 10)
    user.execute(command_int1)

    command_int2 = CommandInterface(receiver, "*", 10)
    user.execute(command_int2)

    command_int3 = CommandInterface(receiver, "-", 10)
    user.execute(command_int3)
    user.undo()
    print(receiver.get_value())
