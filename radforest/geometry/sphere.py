from ..primitive import Primitive

class Sphere(Primitive):

    def __init__(self, modifier, primitive_type, name, center= None, radius = None):
        self.center = center or (0,0,0)
        self.radius = radius

        ln_3 = [self.center[0], self.center[1], self.center[2], radius]
        Primitive.__init__(self, modifier, ln_3 = ln_3)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        assert isinstance(value, float), 'radius must be number'
        self._radius = value if value else 10