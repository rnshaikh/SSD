from board import Board
from move_cache import MoveCache
from stratergy import WinningStratergy1


class Game:

    def __init__(self, size):

        self.players = {}
        self.board = Board(size)
        self.move_cache = MoveCache()
        self.wstratergy = WinningStratergy1()

    def add_player(self, player):

        if len(self.players) > 2:
            raise Exception("Already Two Player Exist")

        self.players[player.token.t] = player

    def play_move(self, i, j, move):

        if self.move_cache.moves and self.move_cache.moves[-1][2] == move:
            raise Exception("previous player cant play move")

        player = self.players[move]
        self.board.insert_move(i, j, move)
        flag = self.wstratergy.check_winning(self.board.board, player.token.t)
        if flag:
            print("${player_name} wins".format(player_name=player.name))
            self.board.print_board()
            self.move_cache.insert_move((i, j, move))
            return flag

        flag = self.wstratergy.check_draw(self.board.board)
        if flag:
            print("Game Draws")
            self.board.print_board()
            self.move_cache.insert_move((i, j, move))
            return flag








