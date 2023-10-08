from models.Team import Team
from models.User import User

from .UserManager import UserManager


class TeamManager:

    def __new__(cls):
        if hasattr(cls, "instance"):
            return cls.instance
        cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.teams = {}
        self.user_manager = UserManager()

    def create_team(self, name, users):

        team = Team(name)
        for user in users:
            user_obj = self.user_manager.get_user(user)

            if not user_obj:
                raise Exception("User does not exists")

            if user_obj.team:
                raise Exception("User is already a part of other team")
            else:
                team.add_member(user_obj)
                user_obj.set_team(team)

        self.teams[name] = team

    def get_team(self, name):

        return self.teams.get(name, None)








