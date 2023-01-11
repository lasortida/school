class Car:
    def __init__(self, road, p, v, x):
        self.road = road
        self.p = p if 0 < p <= road.width else 1
        self.v = v if v > 0 else 1
        self.x = x if x >= 0 else 0

    def move(self):
        self.x += self.v
        if self.x > self.road.length:
            self.x = 0

