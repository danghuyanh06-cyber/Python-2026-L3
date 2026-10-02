students = []
courses = []
marks = {}


def add_students():
    n = int(input("Enter number of students: "))
    for i in range(n):
        print("Student", i + 1)
        student_id = input("ID: ")
        name = input("Name: ")
        dob = input("Date of birth: ")
        student = {
            "id": student_id,
            "name": name,
            "dob": dob,
        }
        students.append(student)


def add_courses():
    n = int(input("Enter number of courses: "))
    for i in range(n):
        print("Course", i + 1)
        course_id = input("Course ID: ")
        name = input("Course name: ")
        course = {
            "id": course_id,
            "name": name,
        }
        courses.append(course)


def show_students():
    print("List of students")
    if not students:
        print("No students available.")
        return
    for student in students:
        print(student["id"], "-", student["name"], "-", student["dob"])


def show_courses():
    print("List of courses")
    if not courses:
        print("No courses available.")
        return
    for course in courses:
        print(course["id"], "-", course["name"])


def add_marks():
    if not students:
        print("No students available.")
        return
    if not courses:
        print("No courses available.")
        return

    course_id = input("Enter course ID: ")
    if not any(course["id"] == course_id for course in courses):
        print("Course not found.")
        return

    marks.setdefault(course_id, {})
    for student in students:
        score = float(input("Enter mark for " + student["name"] + ": "))
        marks[course_id][student["id"]] = score


def show_marks():
    course_id = input("Enter course ID: ")
    if course_id not in marks:
        print("No marks for this course.")
        return
    print("Scores")
    for student_id in marks[course_id]:
        score = marks[course_id][student_id]
        print(student_id, "-", score)


def main():
    while True:
        print("\n     Title     ")
        print("1. Enter students")
        print("2. Enter the courses")
        print("3. Enter the mark")
        print("4. Show students")
        print("5. Show courses")
        print("6. Show marks")
        print("7. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_students()
        elif choice == "2":
            add_courses()
        elif choice == "3":
            add_marks()
        elif choice == "4":
            show_students()
        elif choice == "5":
            show_courses()
        elif choice == "6":
            show_marks()
        elif choice == "7":
            print("Exit")
            break
        else:
            print("Page not found")


if __name__ == "__main__":
    main()
