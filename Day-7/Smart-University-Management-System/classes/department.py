class Department:
    def __init__(self, dept_code: str, dept_name: str):
        self.dept_code = dept_code
        self.dept_name = dept_name
        self.students = []
        self.faculty_members = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_faculty(self, faculty):
        self.faculty_members.append(faculty)

    def add_course(self, course):
        self.courses.append(course)

    def get_department_summary(self):
        return {
            "Department Code": self.dept_code,
            "Department Name": self.dept_name,
            "Total Students": len(self.students),
            "Total Faculty": len(self.faculty_members),
            "Total Courses": len(self.courses)
        }

    def __str__(self):
        return f"{self.dept_name} ({self.dept_code})"
