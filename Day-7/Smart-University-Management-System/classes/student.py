from classes.person import Person
from utils.descriptors import MarksDescriptor
from utils.decorators import log_execution, performance_timer

class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, student_id, name, department, semester, marks):
        super().__init__(student_id, name, department)
        self.semester = semester
        self.marks = marks
        self.courses = []

        self.average = None
        self.grade = None

        department.add_student(self)

    def get_details(self):
        return (
            f"Name: {self.name}\n"
            f"Role: Student\n"
            f"Department: {self.department.dept_name}"
        )

    @log_execution
    @performance_timer
    def calculate_performance(self):
        self.average = sum(self.marks) / len(self.marks)
        self.grade = (
            "A" if self.average >= 85 else
            "B" if self.average >= 70 else
            "C"
        )
        return self.average, self.grade

    def __gt__(self, other):
        if self.average is None:
            self.calculate_performance()
        if other.average is None:
            other.calculate_performance()

        return self.average > other.average
