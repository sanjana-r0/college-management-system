# college-management-system
1. Clone the project
git clone <GitHub-repository-url>
cd college-management-system
2. Get latest code and create branch
git checkout develop
git pull origin develop
git checkout -b feature/student
3. Create student.py
students = {}

def add_student(id, name, course):
    students[id] = {"name": name, "course": course}

def display_students():
    for id, details in students.items():
        print(id, details)

def search_student(id):
    if id in students:
        print(students[id])
    else:
        print("Student not found")

# Sample
add_student(101, "Rahul", "CSE")
add_student(102, "Anu", "ECE")

display_students()
search_student(101)

students = {}

def add_student(id, name, course):
    students[id] = {"name": name, "course": course}

def display_students():
    for id, details in students.items():
        print(id, details)

def search_student(id):
    if id in students:
        print(students[id])
    else:
        print("Student not found")

# Sample
add_student(101, "Rahul", "CSE")
add_student(102, "Anu", "ECE")

display_students()
search_student(101)

7. Create Pull Request

On GitHub:

Pull Requests → New Pull Request

Base: develop
Compare: feature/student
Create Pull Request
Merge the PR


Part B — GitFlow + Merge Conflict

Create the required branches:

git checkout main
git pull origin main

git checkout -b develop
git push -u origin develop

git checkout -b feature/user-auth
git push -u origin feature/user-auth

Create release branch:

git checkout develop
git checkout -b release/1.0
git push -u origin release/1.0

Create hotfix:

git checkout main
git checkout -b hotfix/login-bug
git push -u origin hotfix/login-bug


Deliberate merge conflict

Edit the same line in a file differently on two branches.

For example:

develop:

message = "Welcome to College Management System"

feature/user-auth:

message = "Welcome User"

Then merge:

git checkout develop
git merge feature/user-auth

Keep the desired version, remove the conflict markers, then:

git add .
git commit -m "Resolve merge conflict"
Tag the release
git checkout release/1.0
git tag v1.0
git push origin v1.0

Push all branches
git push origin main
git push origin develop
git push origin feature/user-auth
git push origin release/1.0
git push origin hotfix/login-bug
