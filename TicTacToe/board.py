
class Board:

    def __init__(self, size):

        self.size = size
        self.board = [["#" for _ in range(size)] for _ in range(size)]

    def clear_board(self, size):

        self.board = [["#" for _ in range(size)] for _ in range(size)]

    def print_board(self):

        for i in self.board:
            print(i)

    def insert_move(self, i, j, move):

        if i >= self.size or j >= self.size or self.board[i][j] != "#":
            raise Exception("Invalid Move")
        self.board[i][j] = move

    def remove_move(self, i, j, move):

        if i >= self.size or j >= self.size or self.board[i][j] != move:
            raise Exception("Invalid remove")

        self.board[i][j] = "#"







