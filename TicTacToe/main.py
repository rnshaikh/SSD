from game import Game
from player import Player
from player_token import Token

if __name__ == "__main__":

    game = Game(3)

    player1 = Player("a")
    token1 = Token("O")
    player1.select_move_token(token1)
    game.add_player(player1)

    player2 = Player("r")
    token2 = Token("X")
    player2.select_move_token(token2)
    game.add_player(player2)

    flag = True

    while True:
        game.board.print_board()
        if flag:
            inp = input("{player_name} play move:".format(player_name=player1.name))
            move = inp.split(",")
            f = game.play_move(int(move[0]), int(move[1]), player1.token.t)
            if f:
                break
            flag = not flag
        else:
            inp = input("{player_name} play move:".format(player_name=player2.name))
            move = inp.split(",")
            f = game.play_move(int(move[0]), int(move[1]), player2.token.t)
            if f:
                break
            flag = not flag



