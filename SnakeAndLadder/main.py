from snake_ladder_service import SnakeLadderService
from player import Player

if __name__ == "__main__":

    obj = SnakeLadderService()
    size = int(input("Enter Board Size:"))
    obj.initialize_board(size)
    players = []

    n = int(input("Enter no of players:"))
    while n > 0:

        player_name = input("Enter player name:")
        player_obj = Player(player_name)
        obj.add_player(player_obj)
        n = n-1

    n = int(input("Enter How many ladder?"))

    while n > 0:

        inp = input("Enter space sperated start and end of ladder:")
        inp = inp.split(" ")
        obj.add_ladders(int(inp[0]), int(inp[1]))
        n = n-1

    n = int(input("Enter How many snakes?"))

    while n > 0:

        inp = input("Enter space sperated start and end of snakes:")
        inp = inp.split(" ")
        obj.add_snakes(int(inp[0]), int(inp[1]))
        n = n-1

    obj.play_game()

