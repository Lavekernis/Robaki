import worm


class Team:
    def __init__(self, worms: list[worm.Worm], idx: int):
        """Worms is an array of worms belonging to given team."""
        self._worms = worms
        self._recent_pick_index = -1  # Last worm being active in a turn.
        self.team_index = idx

    def move_turn(self):
        self._recent_pick_index = (
            self._recent_pick_index + 1) % len(self._worms)

    def set_active(self):
        self._worms[self._recent_pick_index]._is_selected
