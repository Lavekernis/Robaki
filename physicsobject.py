from pygame.math import Vector2
import variables as var

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
    def position(self,pos):
        self._position = pos

    def draw(self,screen,pos):
        print("Nie możesz narysować klasy abstrakcji")

    def update(self,frame_time):
        print("Nie możesz odświeżyć kasy abstrakcji")

    def camera_cord_converter(self):
        return Vector2(round(self._position[0] - var.camera_vector[0]),round(self._position[1] - var.camera_vector[1]))
