class Car:
    no_of_wheels, no_of_doors = 4, 4

    def __init__(self, color, producer, model, fuel):
        self.color = color
        self.producer = producer
        self.model = model
        self.fuel = fuel

    def turn(self, direction: str):
        print(self.model + ':' + 'Turning ' + direction + '...')

    def accelerate(self, factor: float):
        print(self.model + ':' + 'Accelerating its speed by ' + str(factor) + 'x...')

    def __str__(self):
        return self.producer + ' ' + self.color + ' ' + self.model + ' ' + self.fuel


def main():
    toyota = Car('Red', 'Toyota', 'Prius', 'Electricity')

    print('Car:', toyota)
    print('Total wheels:' + str(toyota.no_of_wheels))
    print('Color: ' + toyota.color)
    toyota.accelerate(2.5)
    toyota.turn('left')


if __name__ == '__main__':
    main()

"""
NOTE:
    - the variable 'color', 'producer, 'model' are not declared in class boy - which you have to do in java
    - if you do no use any of the class properties in the method say - turn(), pyCharm code inspector suggest you to 
    make a 'function' from this method.
"""
