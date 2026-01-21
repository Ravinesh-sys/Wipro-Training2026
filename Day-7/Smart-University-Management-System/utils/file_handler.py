import json
import csv

class FileHandler:

    @staticmethod
    def save_students_to_json(students, filename):
        data = []

        for student in students:
            if student.average is None:
                student.calculate_performance()

            data.append({
                "id": student.person_id,
                "name": student.name,
                "department": student.department.dept_name,
                "semester": student.semester,
                "marks": student.marks,
                "average": student.average,
                "grade": student.grade
            })

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def save_students_to_csv(students, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Department", "Average", "Grade"])

            for student in students:
                if student.average is None:
                    student.calculate_performance()

                writer.writerow([
                    student.person_id,
                    student.name,
                    student.department.dept_name,
                    student.average,
                    student.grade
                ])
