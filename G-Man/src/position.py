

class Position:

    def __init__(self, x, y, dire=None):
        self._x = int(x)
        self._y = int(y)
        self._dir = dire

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def dir(self):
        return self._dir
    