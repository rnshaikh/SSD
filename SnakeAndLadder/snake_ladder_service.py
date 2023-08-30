from board import Board
from dice import Dice


class SnakeLadderService:

    def __init__(self):
        self.board = None
        self.players = []
        self.dice = Dice()

    def initialize_board(self, size):
        self.board = Board(size)

    def add_player(self, player):

        self.players.append(player)
        self.board.add_player_piece(player.name, 0)

    def add_snakes(self, start, end):
        self.board.add_snakes(start, end)

    def add_ladders(self, start, end):
        self.board.add_ladders(start, end)

    def check_for_ladder_snakes(self, new_pos):

        if new_pos in self.board.snakes:
            print("Got Snake")
            return self.board.snakes[new_pos]

        if new_pos in self.board.ladders:
            print("Got Ladder")
            return self.board.ladders[new_pos]

        return new_pos

    def current_standing(self):

        for k in self.players:
            print("{player_name} -- {pos}".format(player_name=k.name,
                                                  pos=self.board.get_player_piece(k.name)))

    def play_game(self):

        flag = False
        while True:
            i = 0
            for i in range(len(self.players)):
                player = self.players[i]
                num = self.dice.roll()
                curr_pos = self.board.get_player_piece(player.name)
                new = curr_pos + num

                if new > self.board.size:
                    continue
                else:
                    new = self.check_for_ladder_snakes(new)

                if new == self.board.size:
                    self.board.add_player_piece(player.name, new)
                    print("Player {player_name} won the game".format(player_name=player.name))
                    flag = True
                    break

                self.board.add_player_piece(player.name, new)

            self.current_standing()
            if flag:
                break










