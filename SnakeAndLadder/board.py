

class Board:

    def __init__(self, size):

        self.size = size
        self.snakes = {}
        self.ladders = {}
        self.player_pieces = {}

    def add_snakes(self, start, end):

        if start in self.snakes or start in self.ladders:
            raise Exception("snake/ladder is already there")

        if end > self.size or end <= 0:
            raise Exception("invalid end point")

        if start > self.size or start <= 0:
            raise Exception("invalid start point")

        if end > start:
            raise Exception("snake should end below start point")

        self.snakes[start] = end

    def add_ladders(self, start, end):

        if start in self.snakes or start in self.ladders:
            raise Exception("snake/ladder is already there")

        if end > self.size or end <= 0:
            raise Exception("invalid end point")

        if start > self.size or start <= 0:
            raise Exception("invalid start point")

        if end < start:
            raise Exception("ladder should start below end point")

        self.ladders[start] = end

    def add_player_piece(self, name, pos):

        self.player_pieces[name] = pos

    def get_player_piece(self, name):

        if name not in self.player_pieces:
            raise Exception("player does not exist")
        return self.player_pieces[name]






