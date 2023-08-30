
class MoveCache:

    def __init__(self):
        self.moves = []

    def insert_move(self, move):
        self.moves.append(move)

    def remove_move(self):

        if not len(self.moves):
            raise Exception("Invalid Undo")

        move = self.moves.pop()
        return move
