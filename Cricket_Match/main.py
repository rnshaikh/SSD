from match import Match 
from team import Team
from player import Player 


if __name__ == "__main__":



	no_of_players = int(input("Number of Players in each team: "))
	no_of_overs = int(input("No of Overs: "))

	team1 = Team("team1")
	team2 = Team("team2")

	team1.add_total_no_player(no_of_players)
	team2.add_total_no_player(no_of_players)

	print("Batting order for team1: ")
	for i in range(no_of_players):

		player = input("")
		player = Player(player)
		team1.add_player(player)


	print("Batting order for team2: ")
	for i in range(no_of_players):

		player = input("")
		player = Player(player)
		team2.add_player(player)

	match = Match(team1, team2)
	match.add_total_overs(no_of_overs)
	match.set_current_batting_team(team1)
	print("current batting team", match.current_batting_team)
	match.start_match_helper()



