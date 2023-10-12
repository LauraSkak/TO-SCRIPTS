#Exercise 1
class Vehicle:
    def __init__(self, name, seats, trunk_space):
        self.name = name
        self.seats = seats
        self.trunk_space = trunk_space
        self.fuel = 'gasoline'

    #exercise 2

    def __str__(self):
        return self.name
    
    #Exercise 3

    def at_capacity(self, passengers, suitcases):
        if passengers >= self.seats:
            return True
        elif suitcases >= self.trunk_space + (self.seats-passengers):
            return True
        else:
            return False


#car = Vehicle("Dodge", 2, 1)
#print(f'The {car.name} has {car.seats} seats and {car.trunk_space} units of trunk space')

#car = Vehicle("Jeep", 4, 2)
#print(car)

#car = Vehicle("Volvo", 4, 3)
#print(f'It is {car.at_capacity(3, 3)} that the {car.name} is at/over capacity')

class Bus(Vehicle):
    def __init__(self, name, seats, trunk_space):
        self.name = name
        self.seats = seats
        self.trunk_space = trunk_space
        self.fuel = 'diesel'
    
    def at_capacity(self, passengers, suitcases):
        if passengers > self.seats:
            return True
        elif suitcases >= self.seats:
            return True
        return False
        
#school_bus = Bus("School bus", 22, 10)
#print(f'The {school_bus.name} has {school_bus.seats} seats and {school_bus.trunk_space} units of trunk space')
#print(f'It is {school_bus.at_capacity(22, 11)} that the {school_bus.name} is at/over capacity')

#tour_bus = Bus("Dodge", 30, 20)
#convertible =  Vehicle("Saab", 4, 1)
#print(f'The {tour_bus.name} uses {tour_bus.fuel}')
#print(f'The {convertible.name} uses {convertible.fuel}')

#Exercise 6
class Truck(Vehicle):
    def __init__(self, name, passengers, trunk_units, trailer_units):
        super().__init__(name, passengers, trunk_units)
        self.trailer_units =  trailer_units

#sixteen_wheeler = Truck('Man', 2, 2, 542)
#print(sixteen_wheeler)

#Exercise 7
class AutoTransport(Vehicle):
    def __init__(self, name, passengers, trunk_units):
        super().__init__(name, passengers, trunk_units)
        self.loaded_cars = []

    def __str__(self):
        return f"{self.name} with: {', '.join(map(str, self.loaded_cars))}"
    
    def load(self, car):
        self.loaded_cars.append(car.name)

auto_trans = AutoTransport('Man', 2, 2)
#print(auto_trans)
auto_trans.load(Vehicle('Mustang', 4, 1))
auto_trans.load(Vehicle('Charger', 4, 1))
auto_trans.load(Vehicle('Corvette', 4, 1))
auto_trans.load(Vehicle('Challenger', 4, 1))
print(auto_trans)
