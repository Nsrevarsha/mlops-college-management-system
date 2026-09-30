students = []
def add_student(name):
    student = {"name": name}
    students.append(student)
    return student

def display_students():
    return students

def search_student(name):
    for student in students:
        if student["name"] == name:
            return student
    return None
