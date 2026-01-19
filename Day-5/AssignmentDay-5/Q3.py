import json
import csv
import time
from abc import ABC, abstractmethod
from typing import List



# Here Implementation of DECORATOR


def log_execution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper


def admin_only(func):
    def wrapper(*args, **kwargs):
        user_role = kwargs.get("role", "user")
        if user_role != "admin":
            print("Access Denied: Admin privileges required")
            return None
        return func(*args, **kwargs)
    return wrapper


def performance_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution Time: {end - start:.4f} seconds")
        return result
    return wrapper


# Implemention of Descriptor

class MarksValidator:
    def __get__(self, instance, owner):
        return instance._marks

    def __set__(self, instance, value):
        if not all(0 <= mark <= 100 for mark in value):
            raise ValueError("Marks should be between 0 and 100")
        instance._marks = value


class SalaryProtector:
    def __get__(self, instance, owner):
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, instance, value):
        instance._salary = value


#Abstract Base Class

class Person(ABC):
    def __init__(self, person_id: str, name: str, department: str):
        self.person_id = person_id
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def calculate_performance(self):
        pass

    def __del__(self):
        print(f"[CLEANUP] Resources released for {self.name}")

# Class for Student
class Student(Person):
    marks = MarksValidator()

    def __init__(self, student_id, name, department, semester, marks):
        super().__init__(student_id, name, department)
        self.semester = semester
        self.marks = marks

    def get_details(self):
        print("Student Details")
        print("--------------------------------")
        print(f"Name      : {self.name}")
        print("Role      : Student")
        print(f"Department: {self.department}")

    @log_execution
    @performance_timer
    def calculate_performance(self):
        average = sum(mark for mark in self.marks) / len(self.marks)
        grade = "A" if average >= 85 else "B" if average >= 70 else "C"
        return average, grade

    def __gt__(self, other):
        return sum(self.marks) > sum(other.marks)

# Class for Faculty

class Faculty(Person):
    salary = SalaryProtector()

    def __init__(self, faculty_id, name, department, salary):
        super().__init__(faculty_id, name, department)
        self.salary = salary

    def get_details(self):
        print("Faculty Details")
        print("--------------------------------")
        print(f"Name      : {self.name}")
        print("Role      : Faculty")
        print(f"Department: {self.department}")

    def calculate_performance(self):
        return "Faculty performance evaluated annually"



# class for course


class Course:
    def __init__(self, course_code, course_name, credits, faculty):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits
        self.faculty = faculty
        self.enrolled_students: List[Student] = []

    def enroll_student(self, student: Student):
        self.enrolled_students.append(student)
        print("Enrollment Successful")
        print("--------------------------------")
        print(f"Student Name : {student.name}")
        print(f"Course       : {self.course_name}")

    def __add__(self, other):
        return self.credits + other.credits

    def __iter__(self):
        return iter(self.enrolled_students)



# Implementation of Generator Here

def student_record_generator(students: List[Student]):
    print("Fetching Student Records...")
    print("--------------------------------")
    for student in students:
        yield f"{student.person_id} - {student.name}"


# Here File Handling process is taking place

class FileManager:

    @staticmethod
    def save_students_to_json(students: List[Student], filename="students.json"):
        try:
            data = []
            for student in students:
                avg, grade = student.calculate_performance()
                data.append({
                    "id": student.person_id,
                    "name": student.name,
                    "department": student.department,
                    "average": round(avg, 2),
                    "grade": grade
                })
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            print("Student data successfully saved to students.json")
        except FileNotFoundError:
            print("Error: File not found")

    @staticmethod
    def generate_csv_report(students: List[Student], filename="students_report.csv"):
        try:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
                for student in students:
                    avg, grade = student.calculate_performance()
                    writer.writerow([student.person_id, student.name,
                                     student.department, round(avg, 2), grade])
            print("CSV Report Generated")
        except IOError:
            print("Error: Unable to write CSV file")


# Main Simulation

if __name__ == "__main__":

    try:
        student1 = Student("S101", "Ananya Sharma", "Computer Science", 4,
                           [78, 85, 90, 88, 92])
        student2 = Student("S102", "Rohan Verma", "Computer Science", 4,
                           [70, 75, 80, 78, 72])

        faculty1 = Faculty("F201", "Dr. Rajesh Kumar",
                           "Computer Science", 85000)

        course1 = Course("CS401", "Data Structures", 4, faculty1)
        course2 = Course("CS402", "Algorithms", 3, faculty1)

        student1.get_details()
        faculty1.get_details()

        course1.enroll_student(student1)

        avg, grade = student1.calculate_performance()
        print("\nStudent Performance Report")
        print("--------------------------------")
        print(f"Student Name : {student1.name}")
        print(f"Marks        : {student1.marks}")
        print(f"Average      : {round(avg, 2)}")
        print(f"Grade        : {grade}")

        print("\nComparing Students Performance")
        print("--------------------------------")
        print(f"Ananya Sharma > Rohan Verma : {student1 > student2}")

        print("\nMerge Course Credits")
        print("Total Credits After Merge :", course1 + course2)

        print("\nStudent Record Generator")
        for record in student_record_generator([student1, student2]):
            print(record)

        FileManager.generate_csv_report([student1, student2])
        FileManager.save_students_to_json([student1, student2])

    except ValueError as ve:
        print("Error:", ve)
    except PermissionError as pe:
        print(pe)
    except Exception as e:
        print("Unexpected Error:", e)
    finally:
        print("\nThank you for using Smart University Management System")
