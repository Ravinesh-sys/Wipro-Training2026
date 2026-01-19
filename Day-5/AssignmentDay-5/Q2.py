#1. Create a class Calculator that demonstrates method overriding

class Calculator:
    def operate(self, x, y):
        result = x + y
        print("Basic Calculator Operation: Addition")
        return result


class SmartCalculator(Calculator):
    def operate(self, x, y):
        result = x * y
        print("Smart Calculator Operation: Multiplication")
        return result


# Object of parent class
basic_calc = Calculator()
print("Result:", basic_calc.operate(4, 6))

print("-" * 30)

# Object of child class
smart_calc = SmartCalculator()
print("Result:", smart_calc.operate(4, 6))


#2. Create another class AdvancedCalculator that overrides a method from Calculator
class Calculator:
    def calculate(self, a, b):
        print("Calculator is adding two numbers")
        return a + b


class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        print("AdvancedCalculator is finding the power")
        return a ** b


# Parent class object
simple_calc = Calculator()
print("Result:", simple_calc.calculate(2, 3))

print("-" * 40)

# Child class object
advanced_calc = AdvancedCalculator()
print("Result:", advanced_calc.calculate(2, 3))

#3. Implement operator overloading by overloading the + operator to add two objects of a custom class

class Score:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        print("Adding two Score objects")
        return Score(self.value + other.value)

    def display(self):
        print("Total Score:", self.value)


# Create objects
s1 = Score(45)
s2 = Score(55)

# Use + operator
s3 = s1 + s2


#4. Demonstrate polymorphism using the same method name with different behaviors
class Shape:
    def draw(self):
        print("Drawing a generic shape")


class Circle(Shape):
    def draw(self):
        print("Drawing a circle")


class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")


# Polymorphism in action
shapes = [Shape(), Circle(), Rectangle()]

for obj in shapes:
    obj.draw()

s3.display()