from enum import Enum
from team import Team
from over import Over
from ball import Ball
from player import Player


class Status(Enum):

	NOT_STARTED = "Not Started"
	STARTED = "Started"
	COMPLETED = "Completed" 


class Result(Enum):

	WIN = "Win"
	DRAW = "Draw"


class Match:

	def __init__(self, team1, team2):
		self.team1 = team1 
		self.team2 = team2
		self.total_wickets = 0
		self.total_overs = 0
		self.overs = []
		self.previous_batting_team = None
		self.current_batting_team = None
		self.winning_team = None
		self.match_status = Status.NOT_STARTED.value
		self.match_result = None


	def add_total_overs(self, overs):
		self.total_overs = overs 

	def add_players_to_team(self, team, players):

		team =  team1 if self.team1 == team else self.team2
		for player in players:
			team.add_player(player)

	def switch_batting(self):

		if self.current_batting_team == self.team1:
			self.current_batting_team = self.team2
			self.previous_batting_team = self.team1
			self.current_batting_team.initialized_batsman()
		else:
			self.current_batting_team = self.team1
			self.previous_batting_team = self.team2
			self.current_batting_team.initialized_batsman()


	def set_current_batting_team(self, team):
		self.current_batting_team = team
		self.current_batting_team.change_batting()
		self.current_batting_team.initialized_batsman()


	def start_match_helper(self):

		self.match_status = Status.STARTED.value
		self.start_match()
		self.switch_batting()
		print("Current batting team", self.current_batting_team.name)
		self.overs = []
		self.start_match()
		self.check_winning_team()
		self.display_result()

	def append_over_to_player(self, over):

		team = None
		if self.current_batting_team == self.team1:
			team = self.team2
		else:
			team = self.team1

		player = team.get_player()
		over.add_player(player)


	def start_match(self):
		for i in range(0, self.total_overs):
			j = 0
			over = Over()
			all_wicket = False
			win = False
			self.append_over_to_player(over)
			print("Over: %i" %(i))
			while j < 6:
				run = input("")
				over.add_ball(run)

				if run in ["Wd", "N"]:
					self.current_batting_team.update_score(1)
					if self.previous_batting_team and self.current_batting_team.total_score > self.previous_batting_team.total_score:
						win = True
						break

				elif run not in ["Wd", "N"] and run != "W":
					self.current_batting_team.update_score(int(run))
					self.current_batting_team.strike_batsman.add_score(int(run))
					if int(run) % 2 != 0:
						self.current_batting_team.change_strike_after_over()

					if self.previous_batting_team and self.current_batting_team.total_score > self.previous_batting_team.total_score:
						win = True
						break
					j +=1
					
				elif run  == "W":

					self.current_batting_team.update_wicket_fallen()
					if self.current_batting_team.is_batsman_available():
						self.current_batting_team.change_strike_after_wicket_fallen(True)
					else:
						all_wicket = True
						break 
					j = j+1

			if all_wicket or win:
				self.overs.append(over)
				self.display_score_card()
				break
				
			self.overs.append(over)
			self.current_batting_team.change_strike_after_over()
			self.display_score_card()			


	def check_winning_team(self):


		if self.team1.total_score > self.team2.total_score:
			self.winning_team = self.team1
			self.match_result = Result.WIN.value
		elif self.team1.total_score < self.team2.total_score:
			self.winning_team = self.team2
			self.match_result = Result.WIN.value	
		else:
			self.winning_team = None
			self.match_result = Result.DRAW.value

	def print_overs_stat(self):

		ballers = {}
		for over in self.overs:
			if not over.player.name in ballers:
				ballers[over.player.name] = []
			ballers[over.player.name].append(over)

		print("name overs runs wickets")

		for baller in ballers:
			total_run = 0
			total_wicket = 0
			total_overs = 0
			for over in ballers[baller]:
				total_run += over.total_run
				total_wicket += over.total_wickets
				total_overs += over.total_ball_bowled

			temp = total_overs//6
			rem = total_overs%6

			print("{name} {overs} {runs} {wickets}".format(name=baller, overs=str(temp)+'.'+str(rem),
														   runs=total_run, wickets=total_wicket))



	def display_score_card(self):
		
		print("ScoreCard For Team:", self.current_batting_team.name)

		for player in self.current_batting_team.players:
			star = ""
			if player == self.current_batting_team.current_batsman or player == self.current_batting_team.strike_batsman:
				star = "*"

			print("{name} {star} {runs} {fours} {sixes} {ball_faced}".format(name=player.name, star=star, 
																   runs=player.score, fours=player.no_fours,
																   sixes=player.no_sixes,
																   ball_faced=player.ball_faced,
																   ))

		print("Overs: ")
		self.print_overs_stat()

		print("total : {total}/ {wicket_fallen} - {overs}/{total_overs}".format(
						total=self.current_batting_team.total_score, 
						wicket_fallen=self.current_batting_team.total_wicket_fallen,
						total_overs =self.total_overs,
						overs= len(self.overs)
						))



	def display_result(self):
		

		if self.winning_team:

			if self.current_batting_team == self.winning_team:
				print("team {team} won by {wickets} wickets".format(team=self.current_batting_team.name,
															 wickets=self.current_batting_team.total_wickets-
															 		 self.current_batting_team.total_wicket_fallen))
			else:
				team = self.current_batting_team
				if self.current_batting_team == self.team1:
					team = self.team2
				else:
					team = self.team1
				print("team {team} won by {run}".format(team=team.name, 
														run=(team.total_score-self.current_batting_team.total_score)+1))

