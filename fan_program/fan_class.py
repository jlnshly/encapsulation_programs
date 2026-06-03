class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed, radius, color, on):
        self.speed = speed
        self.radius = radius
        self.color = color
        self.on = on

    def speed(self):
        return self._speed

    def speed(self, value):
        self._speed = value

    def radius(self):
        return self._radius

    def radius(self, value):
        self._radius = value

    def color(self):
        return self._color

    def color(self, value):
        self._color = value

    def on(self):
        return self._on

    def on(self, value):
        self._on = value