from classes.person import Person
from utils.descriptors import SalaryDescriptor

class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, faculty_id, name, department, salary):
        super().__init__(faculty_id, name, department)
        self.salary = salary
        department.add_faculty(self)

    def get_details(self):
        return (
            f"Name: {self.name}\n"
            f"Role: Faculty\n"
            f"Department: {self.department.dept_name}"
        )
