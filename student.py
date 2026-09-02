students = {"200": {"name": "Auth User", "course": "IT"}}

def add_student(id, name, course):
    students[id] = {
        "name": name,
        "course": course
    }

def display_students():
    for id, details in students.items():
        print(id, details["name"], details["course"])

def search_student(id):
    if id in students:
        print(students[id])
    else:
        print("Student not found")

add_student(101, "Rahul", "CSE")
add_student(102, "Anu", "ECE")

display_students()
search_student(101)
