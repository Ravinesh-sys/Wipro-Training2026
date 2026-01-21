def student_generator(students: List[Student]):
    for student in students:
        yield f"{student.person_id} - {student.name}"