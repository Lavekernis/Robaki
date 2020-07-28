class Team:
    def __init__(self, worms, idx):
        """Worms is an array of worms belonging to given team."""
        self._worms = worms
        self._recentPickIndex = 0 # Last worm being active in a turn.
        self.teamIndex = idx
        