from pygame.math import Vector2


class PhysicsObject():
    _position = Vector2(0)
    _velocity = Vector2(0)
    _acceleration = Vector2(0)
    _equalibrium = False

    def update(self, frame_time):
        pass

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        self._position = pos
