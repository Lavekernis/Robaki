
class PhysicsObject():
    _position = None
    _velocity = None
    _acceleration = None


    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self,pos):
        self._position = pos