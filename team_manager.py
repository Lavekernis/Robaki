from worm import Worm


class TeamManager:
    instance = None

    def __init__(self):
        if TeamManager.instance == None:
            TeamManager.instance = self
        self.teams = {}
        self._recent_team_index = -1

    def move_turn(self):
        self._recent_team_index = (
            self._recent_team_index + 1) % len(self.teams)

    def add_worm(self, worm: Worm, team: int):
        self.teams[team] = worm
