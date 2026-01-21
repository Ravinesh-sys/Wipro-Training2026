from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, person_id: str, name: str, department: "Department"):
        self.person_id = person_id
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass

