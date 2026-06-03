class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.speed = speed
        self.radius = radius
        self.color = color
        self.on = on

    def speed(self):
        return self.__speed

    def speed(self, value):
        self.__speed = value

    def radius(self):
        return self.__radius

    def radius(self, value):
        self.__radius = value

    def color(self):
        return self.__color

    def color(self, value):
        self.__color = value

    def on(self):
        return self.__on

    def on(self, value):
        self.__on = value

    def __str__(self):
        status = "On" if self.on else "Off"
        return "Fan Speed: {}, Radius: {}, Color: {}".format(self.speed, self.radius, self.color)