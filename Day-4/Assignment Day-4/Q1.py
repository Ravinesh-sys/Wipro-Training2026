class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number



student1 = Student("Ravinesh", 101)

# Access attributes
print("Name:", student1.name)
print("Roll Number:", student1.roll_number)

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_number)



student1 = Student("Ravinesh", 101)


student1.display_details()

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("--------------------")



student1 = Student("Ravinesh", 101)
student2 = Student("Amit", 102)


student1.display_details()
student2.display_details()