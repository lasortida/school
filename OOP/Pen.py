class Pen:
    def __init__(self, road, cars):
        self.road = road
        self.cars = cars
        self.moment = 0

    def getCarArray(self, cars, p):
        result = []
        for car in cars:
            if car.p == p:
                result.append(car)
        return result
    def drawRoad(self, cars):
        width = self.road.width
        print(f"Прошло время: {self.moment}")
        index = 0
        for i in range(width + width + 1):
            if i % 2 == 0:
                print(u'\u2500' * self.road.length)
            else:
                carsCurr = cars[index]
                if len(carsCurr) == 0:
                    print(" " * self.road.length)
                else:
                    j = 0
                    for cord in range(self.road.length):
                        if cord == carsCurr[j].x:
                            print("*", end="")
                            j += 1
                            if j == len(carsCurr):
                                j = 0
                        else:
                            print(" ", end="")
                index += 1
                print("\n", end="")
        self.moment += 1
        for i in range(len(cars)):
            self.cars[i].move()

