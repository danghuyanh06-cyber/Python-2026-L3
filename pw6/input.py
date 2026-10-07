import curses
import math
from domains.student import Student
from domains.course import Course

def add_students(stdscreen, students):
    stdscreen.clear()
    stdscreen.addstr("Enter number of students: ")
    curses.echo()
    try:
        n = int(stdscreen.getstr().decode('utf-8'))
        for i in range(n):
            stdscreen.clear()
            stdscreen.addstr(f"Student {i + 1}\nStudent ID: ")
            sid = stdscreen.getstr().decode('utf-8')
            stdscreen.addstr("Enter Student Name: ")
            name = stdscreen.getstr().decode('utf-8')
            stdscreen.addstr("Enter Student Date of Birth (YYYY-MM-DD): ")
            dob = stdscreen.getstr().decode('utf-8')
            students.append(Student(sid, name, dob))
    except ValueError:
        pass
    curses.noecho()

def add_courses(stdscreen, courses):
    stdscreen.clear()
    stdscreen.addstr("Enter number of courses: ")
    curses.echo()
    try:
        n = int(stdscreen.getstr().decode('utf-8'))
        for i in range(n):
            stdscreen.clear()
            stdscreen.addstr(f"Course {i + 1}\nCourse ID: ")
            cid = stdscreen.getstr().decode('utf-8')
            stdscreen.addstr("Enter Course Name: ")
            name = stdscreen.getstr().decode('utf-8')
            stdscreen.addstr("Enter Credits: ")
            credit = int(stdscreen.getstr().decode('utf-8'))
            courses.append(Course(cid, name, credit))
    except ValueError:
        pass
    curses.noecho()

def add_marks(stdscreen, students, courses):
    stdscreen.clear()
    stdscreen.addstr("Enter Course ID to input marks: ")
    curses.echo()
    course_id = stdscreen.getstr().decode('utf-8')

    if not any(c.course_id == course_id for c in courses):
        stdscreen.addstr("\nCourse not found!")
        stdscreen.getch()
        return

    for student in students:
        stdscreen.clear()
        stdscreen.addstr(f"Enter mark for {student.name}: ")
        try:
            score = float(stdscreen.getstr().decode('utf-8'))
            student.marks[course_id] = math.floor(score * 10) / 10.0
        except ValueError:
            pass
    curses.noecho()