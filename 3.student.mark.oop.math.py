import curses
import math
import os
import zipfile

import numpy as np


class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0


class Course:
    def __init__(self, course_id, course_name, credit):
        self.course_id = course_id
        self.course_name = course_name
        self.credit = credit
        self.students = []


class UniversityManagement:
    def __init__(self):
        self.courses = []
        self.students = []

    def add_student(self, stdscreen):
        stdscreen.clear()
        stdscreen.addstr("Enter number of students: ")
        curses.echo()
        try:
            n = int(stdscreen.getstr().decode("utf-8"))
            for i in range(n):
                stdscreen.clear()
                stdscreen.addstr(f"Student {i + 1}\n")
                stdscreen.addstr("Enter Student ID: ")
                student_id = stdscreen.getstr().decode("utf-8")
                stdscreen.addstr("Enter Student Name: ")
                name = stdscreen.getstr().decode("utf-8")
                stdscreen.addstr("Enter Student Date of Birth (YYYY-MM-DD): ")
                dob = stdscreen.getstr().decode("utf-8")
                self.students.append(Student(student_id, name, dob))
        except ValueError:
            pass
        curses.noecho()

    def add_courses(self, stdscreen):
        stdscreen.clear()
        stdscreen.addstr("Enter number of courses: ")
        curses.echo()
        try:
            n = int(stdscreen.getstr().decode("utf-8"))
            for i in range(n):
                stdscreen.clear()
                stdscreen.addstr(f"Course {i + 1}\nCourse ID: ")
                cid = stdscreen.getstr().decode("utf-8")
                stdscreen.addstr("Enter Course Name: ")
                name = stdscreen.getstr().decode("utf-8")
                stdscreen.addstr("Enter Credits: ")
                credit = int(stdscreen.getstr().decode("utf-8"))
                self.courses.append(Course(cid, name, credit))
        except ValueError:
            pass
        curses.noecho()

    def show_students(self, stdscreen):
        stdscreen.clear()
        stdscreen.addstr("List of Students:\n", curses.A_BOLD)
        for student in self.students:
            stdscreen.addstr(f"ID: {student.id}, Name: {student.name}, DoB: {student.dob}\n")
        stdscreen.addstr("\nPress any key to continue...")
        stdscreen.getch()

    def add_marks(self, stdscreen):
        stdscreen.clear()
        stdscreen.addstr("Enter Course ID to input marks: ")
        curses.echo()
        course_id = stdscreen.getstr().decode("utf-8")
        curses.noecho()

        if not any(course.course_id == course_id for course in self.courses):
            stdscreen.addstr("\nCourse not found!")
            stdscreen.getch()
            return

        for student in self.students:
            stdscreen.clear()
            stdscreen.addstr(f"Enter mark for {student.name}: ")
            curses.echo()
            try:
                score = float(stdscreen.getstr().decode("utf-8"))
                student.marks[course_id] = math.floor(score * 10) / 10.0
            except ValueError:
                pass
            curses.noecho()

    def show_courses(self, stdscreen):
        stdscreen.clear()
        stdscreen.addstr("List of Courses:\n", curses.A_BOLD)
        for course in self.courses:
            stdscreen.addstr(f"ID: {course.course_id}, Name: {course.course_name}, Credit: {course.credit}\n")
        stdscreen.addstr("\nPress any key to continue...")
        stdscreen.getch()

    def show_marks(self, stdscreen):
        stdscreen.clear()
        stdscreen.addstr("Enter Course ID: ")
        curses.echo()
        course_id = stdscreen.getstr().decode("utf-8")
        curses.noecho()

        stdscreen.addstr("\nMarks:\n", curses.A_BOLD)
        found_marks = False
        for student in self.students:
            if course_id in student.marks:
                stdscreen.addstr(
                    f"Student ID: {student.id}, Name: {student.name}, Mark: {student.marks[course_id]}\n"
                )
                found_marks = True

        if not found_marks:
            stdscreen.addstr("No marks found for the specified course.\n")

        stdscreen.addstr("\nPress any key to continue...")
        stdscreen.getch()

    def calculate_GPA_and_short(self, stdscreen):
        stdscreen.clear()
        for student in self.students:
            student_marks = []
            student_credits = []
            for course in self.courses:
                if course.course_id in student.marks:
                    student_marks.append(student.marks[course.course_id])
                    student_credits.append(course.credit)
            if sum(student_credits) > 0:
                marks_array = np.array(student_marks, dtype=float)
                credits_array = np.array(student_credits, dtype=float)
                student.gpa = float(np.average(marks_array, weights=credits_array))
            else:
                student.gpa = 0.0

        self.students.sort(key=lambda student: student.gpa, reverse=True)
        stdscreen.addstr("Calculated GPA and sorted students successfully.\n", curses.A_BOLD)
        stdscreen.addstr("Sorted Student List (by GPA):\n", curses.A_UNDERLINE)
        for student in self.students:
            stdscreen.addstr(f"ID: {student.id}, Name: {student.name}, GPA: {student.gpa:.2f}\n")
        stdscreen.addstr("\nPress any key to continue...")
        stdscreen.getch()

    def save_data(self):
        with open("data.txt", "w", encoding="utf-8") as file:
            for student in self.students:
                file.write(f"student|{student.id}|{student.name}|{student.dob}|{student.marks}\n")
            for course in self.courses:
                file.write(f"course|{course.course_id}|{course.course_name}|{course.credit}\n")

        with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as archive:
            archive.write("data.txt")

        if os.path.exists("data.txt"):
            os.remove("data.txt")

    def run(self, stdscreen):
        while True:
            stdscreen.clear()
            stdscreen.addstr("University Management System\n", curses.A_BOLD)
            stdscreen.addstr("1. Add Students\n")
            stdscreen.addstr("2. Add Courses\n")
            stdscreen.addstr("3. Enter the marks\n")
            stdscreen.addstr("4. Show students\n")
            stdscreen.addstr("5. Show courses\n")
            stdscreen.addstr("6. Show marks\n")
            stdscreen.addstr("7. Calculate GPA and sort students\n")
            stdscreen.addstr("8. Exit\n")
            stdscreen.addstr("Enter your choice: ")
            curses.echo()
            choice = stdscreen.getstr().decode("utf-8")
            curses.noecho()

            if choice == "1":
                self.add_student(stdscreen)
            elif choice == "2":
                self.add_courses(stdscreen)
            elif choice == "3":
                self.add_marks(stdscreen)
            elif choice == "4":
                self.show_students(stdscreen)
            elif choice == "5":
                self.show_courses(stdscreen)
            elif choice == "6":
                self.show_marks(stdscreen)
            elif choice == "7":
                self.calculate_GPA_and_short(stdscreen)
            elif choice == "8":
                self.save_data()
                stdscreen.addstr("\nData saved to students.dat. Exiting...")
                stdscreen.refresh()
                curses.napms(1000)
                break
            else:
                stdscreen.addstr("Invalid choice. Press any key to continue...")
                stdscreen.getch()


def main(stdscreen):
    app = UniversityManagement()
    app.run(stdscreen)


if __name__ == "__main__":
    curses.wrapper(main)