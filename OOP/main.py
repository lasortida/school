from Road import Road
from Car import Car
from Pen import Pen
import time
def clear():
    print("\n" * 20)

def sortArray(cars):
    if len(cars) > 0:
        result = []
        minX = 1000000
        minCar = None
        for i in range(len(cars)):
            if cars[i].x < minX:
                minX = cars[i].x
                minCar = cars[i]
        cars.remove(minCar)
        result.append(minCar)
        return result + sortArray(cars)
    else:
        return []


road = Road(60, 3)
cars = []
for i in range(3):
    cars.append(Car(road, i + 1, i + 1 * 3, 2))
pen = Pen(road, cars)

cars_double = []
for i in range(road.width):
    cars_double.append(sortArray(pen.getCarArray(cars, i + 1)))

for i in range(30):
    pen.drawRoad(cars_double)
    time.sleep(0.5)
    clear()



