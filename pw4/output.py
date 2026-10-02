import curses
import numpy as np

def show_students(self, stdscreen):
    stdscreen.clear()
    stdscreen.addstr("List of Students:\n", curses.A_BOLD)
    for student in self.students:
        stdscreen.addstr(f"ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}\n")
        stdscreen.addstr("\nPress any key to continue...")
        stdscreen.getch()

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