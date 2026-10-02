import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
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
        n_str = stdscreen.getstr().decode('utf-8')
        if not n_str.isdigit(): return
        for i in range (int(n_str)):
           stdscreen.clear()
           stdscreen.addstr(f" Student {i + 1}\n")
           stdscreen.addstr("Enter Student ID: ")
           student_id = stdscreen.getstr().decode('utf-8')
           stdscreen.addstr("Enter Student Name: ")
           name = stdscreen.getstr().decode('utf-8')
           stdscreen.addstr("Enter Student Date of Birth (YYYY-MM-DD): ")
           dob = stdscreen.getstr().decode('utf-8')
           
           self.students.append(Student(student_id, name, dob))
        curses.noecho()
    def add_course(self, stdscreen):
        stdscreen.clear()
        stdscreen.addstr("Enter Course ID: ")
        curses.echo()
        n_str = stdscreen.getstr().decode('utf-8')
        if not n_str.isdigit(): return
        for i in range (int(n_str)):
           stdscreen.clear()
           stdscreen.addstr(f" Course {i + 1}\n")
           stdscreen.addstr("Enter Course ID: ")
           course_id = stdscreen.getstr().decode('utf-8')
           stdscreen.addstr("Enter Course Name: ")
           course_name = stdscreen.getstr().decode('utf-8')
           stdscreen.addstr("Enter Course Credit: ")
           credit_str = stdscreen.getstr().decode('utf-8')
           credit =  int(credit_str) if credit_str.isdigit() else 0
           
           self.courses.append(Course(course_id, course_name, credit))
        curses.noecho()
    def show_students(self, stdscreen):
        stdscreen.clear()
        stdscreen.addstr("List of Students:\n", curses.A_BOLD)
        for student in self.students:
            stdscreen.addstr(f"ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}\n")
        stdscreen.addstr("\nPress any key to continue...")
        stdscreen.getch()
    def add_marks(self, stdscreen):
        stdscreen.clear()
        stdscreen.addstr("Enter Course ID to add marks: ")
        curses.echo()
        course_id = stdscreen.getstr().decode('utf-8')
        course_exists = any(c.course_id == course_id for c in self.courses)
        if not course_exists:
            stdscreen.addstr("\nCourse not found. Press any key to continue...")
            stdscreen.getch()
            curses.noecho()
            return
        for student in self.students:
            stdscreen.clear()
            stdscreen.addstr(f"Enter marks for Student ID: {student.student_id}, Name: {student.name}: ")
            mark_str = stdscreen.getstr().decode('utf-8')
            mark = float(mark_str) if mark_str.replace('.', '', 1).isdigit() else 0.0
            student.marks[course_id] = mark
        curses.noecho()
    def show_courses(self, stdscreen):
        stdscreen.clear()
        stdscreen.addstr("Enter ID of course: ")
        curses.echo()
        course_id = stdscreen.getstr().decode('utf-8')
        curses.noecho()
        
        stdscreen.addstr("\nScroce:\n", curses.A_BOLD)
        found_course = False
        found_marks = False
        for student in self.students:
            if course_id in student.marks:
                stdscreen.addstr(f"Student ID: {student.student_id}, Name: {student.name}, Mark: {student.marks[course_id]}\n")
                found_marks = True
                found_course = True
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
                student.gpa = np.average(marks_array, weights=credits_array)
            else:
                student.gpa = 0.0
        self.students.sort(key=lambda x: x.gpa, reverse=True)
        stdscreen.addstr("Calculated GPA and sorted students successfully.\n", curses.A_BOLD)
        stdscreen.addstr("\nPress any key to continue...")
        stdscreen.getch()

    @staticmethod
    def main(stdscreen):
        app = UniversityManagement()
        while True:
            stdscreen.clear()
            stdscreen.addstr("University Management System\n", curses.A_BOLD)
            stdscreen.addstr("1. Add Students\n")
            stdscreen.addstr("2. Enter the course ID\n")
            stdscreen.addstr("3. Enter the marks\n")
            stdscreen.addstr("4. Show students\n")
            stdscreen.addstr("5. show courses\n")
            stdscreen.addstr("6. show marks\n")
            stdscreen.addstr("7. calculate GPA and sort students\n")
            stdscreen.addstr("8. Exit\n")
            stdscreen.addstr("Enter your choice: ")
            curses.echo()
            choice = stdscreen.getstr().decode('utf-8')
            curses.noecho()

            if choice == '1':
                app.add_student(stdscreen)
            elif choice == '2':
                app.add_course(stdscreen)
            elif choice == '3':
                app.add_marks(stdscreen)
            elif choice == '4':
                app.show_students(stdscreen)
            elif choice == '5':
                app.show_courses(stdscreen)
            elif choice == '6':
                app.show_courses(stdscreen)
            elif choice == '7':
                app.calculate_GPA_and_short(stdscreen)
            elif choice == '8':
                break
            else:
                stdscreen.addstr("Invalid choice. Press any key to continue...")
                stdscreen.getch()

if __name__ == "__main__":
    curses.wrapper(UniversityManagement.main)
                
                    