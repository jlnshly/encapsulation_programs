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
        return self.speed_