from classes.department import Department
from classes.student import Student
from classes.faculty import Faculty
from classes.course import Course
from utils.file_handler import FileHandler


def print_header(title):
    print(f"\n{title}")
    print("-" * 40)


def main():
    students = []
    faculties = []
    courses = []

    cs_department = Department("CSE", "Computer Science")

    while True:
        print("\n1.Add Student  2.Add Faculty  3.Add Course")
        print("4.Enroll Student  5.Calculate Performance")
        print("6.Compare Students  7.Generate Reports  8.Exit")

        choice = input("Enter choice: ")

        try:
            # ---------- ADD STUDENT ----------
            if choice == "1":
                sid = input("Student ID: ")
                name = input("Name: ")
                sem = int(input("Semester: "))
                marks = list(map(int, input("Enter 5 marks: ").split()))

                student = Student(sid, name, cs_department, sem, marks)
                students.append(student)

                print_header("Student Created Successfully")
                print(f"ID        : {student.person_id}")
                print(f"Name      : {student.name}")
                print(f"Department: {student.department.dept_name}")
                print(f"Semester  : {student.semester}")

            # ---------- ADD FACULTY ----------
            elif choice == "2":
                fid = input("Faculty ID: ")
                name = input("Name: ")
                salary = float(input("Salary: "))

                faculty = Faculty(fid, name, cs_department, salary)
                faculties.append(faculty)

                print_header("Faculty Created Successfully")
                print(f"ID        : {faculty.person_id}")
                print(f"Name      : {faculty.name}")
                print(f"Department: {faculty.department.dept_name}")

            # ---------- ADD COURSE ----------
            elif choice == "3":
                if not faculties:
                    print("Please add faculty before creating a course")
                    continue

                code = input("Course Code: ")
                cname = input("Course Name: ")
                credits = int(input("Credits: "))
                fid = input("Faculty ID: ")

                faculty = next((f for f in faculties if f.person_id == fid), None)
                if not faculty:
                    print("Error: Faculty ID not found")
                    continue

                course = Course(code, cname, credits, faculty)
                courses.append(course)
                cs_department.add_course(course)

                print_header("Course Added Successfully")
                print(f"Course Code : {course.course_code}")
                print(f"Course Name : {course.course_name}")
                print(f"Credits     : {course.credits}")
                print(f"Faculty     : {faculty.name}")

            # ---------- ENROLL STUDENT ----------
            elif choice == "4":
                sid = input("Student ID: ")
                cid = input("Course Code: ")

                student = next((s for s in students if s.person_id == sid), None)
                course = next((c for c in courses if c.course_code == cid), None)

                if not student or not course:
                    print("Error: Invalid Student ID or Course Code")
                    continue

                student.courses.append(course)

                print_header("Enrollment Successful")
                print(f"Student Name : {student.name}")
                print(f"Course       : {course.course_name}")

            # ---------- CALCULATE PERFORMANCE ----------
            elif choice == "5":
                sid = input("Student ID: ")
                student = next((s for s in students if s.person_id == sid), None)

                if not student:
                    print("Error: Invalid Student ID")
                    continue

                avg, grade = student.calculate_performance()

                print_header("Student Performance Report")
                print(f"Student Name : {student.name}")
                print(f"Marks        : {student.marks}")
                print(f"Average      : {avg:.1f}")
                print(f"Grade        : {grade}")

            # ---------- COMPARE STUDENTS ----------
            elif choice == "6":
                if len(students) < 2:
                    print("At least two students are required for comparison")
                    continue

                sid1 = input("Enter First Student ID: ")
                sid2 = input("Enter Second Student ID: ")

                s1 = next((s for s in students if s.person_id == sid1), None)
                s2 = next((s for s in students if s.person_id == sid2), None)

                if not s1 or not s2:
                    print("Error: Invalid Student ID(s)")
                    continue

                print_header("Comparing Students Performance")
                print(f"{s1.name} > {s2.name} : {s1 > s2}")

            # ---------- GENERATE REPORTS ----------
            elif choice == "7":
                FileHandler.save_students_to_json(students, "data/students.json")
                FileHandler.save_students_to_csv(students, "data/students_report.csv")
                print_header("Reports Generated Successfully")
                print("JSON and CSV reports created successfully")

            # ---------- EXIT ----------
            elif choice == "8":
                print("\nThank you for using Smart University Management System")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()