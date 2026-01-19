class Vehicle:
    def start(self):
        print("The vehicle has started.")


v = Vehicle()
v.start()

class Vehicle:
    def start(self):
        print("The vehicle has started.")


class Car(Vehicle):
    def drive(self):
        print("The car is now driving.")


c = Car()
c.start()
c.drive()

class Vehicle:
    vehicle_count = 0   # class variable

    def __init__(self, brand, model):
        self.brand = brand      # instance variable
        self.model = model
        Vehicle.vehicle_count += 1

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


# Object Creation
v1 = Vehicle("Honda", "City")
v2 = Vehicle("Tata", "Nexon")
v3 = Vehicle("Hyundai", "Creta")

# vehicle details
v1.display()
print()

v2.display()
print()

v3.display()
print()

# Here is total number of vehicle created
print("Total vehicles created:", Vehicle.vehicle_count)

#Single level Inheritance
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):   # Car inherits from Vehicle
    def drive(self):
        print("Car is being driven")

# Object Creation of Car
my_car = Car()

my_car.start()   # Method of Parent class
my_car.drive()   # Method of Child Class


#Multilevel Inheritance with class

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Puppy(Dog):
    def play(self):
        print("Puppy is playing")

# Creation of Object puppy
my_puppy = Puppy()

my_puppy.eat()    # From Animal
my_puppy.bark()   # From Dog
my_puppy.play()   # From Pupp