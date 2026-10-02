import curses
import math
from domains.student import Student
from domains.course import Course

def add_students(stdscr, students):
    stdscr.clear()
    stdscr.addstr("Enter number of students: ")
    curses.echo()
    try:
        n = int(stdscr.getstr().decode('utf-8'))
        for i in range(n):
            stdscr.clear()
            stdscr.addstr(f"Student {i + 1}\nID: ")
            sid = stdscr.getstr().decode('utf-8')
            stdscr.addstr("Name: ")
            name = stdscr.getstr().decode('utf-8')
            stdscr.addstr("DOB: ")
            dob = stdscr.getstr().decode('utf-8')
            students.append(Student(sid, name, dob))
    except ValueError:
        pass
    curses.noecho()

def add_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr("Enter number of courses: ")
    curses.echo()
    try:
        n = int(stdscr.getstr().decode('utf-8'))
        for i in range(n):
            stdscr.clear()
            stdscr.addstr(f"Course {i + 1}\nID: ")
            cid = stdscr.getstr().decode('utf-8')
            stdscr.addstr("Name: ")
            name = stdscr.getstr().decode('utf-8')
            stdscr.addstr("Credits: ")
            credit = int(stdscr.getstr().decode('utf-8'))
            courses.append(Course(cid, name, credit))
    except ValueError:
        pass
    curses.noecho()

def add_marks(stdscr, students, courses):
    stdscr.clear()
    stdscr.addstr("Enter Course ID to input marks: ")
    curses.echo()
    course_id = stdscr.getstr().decode('utf-8')
    
    if not any(c.id == course_id for c in courses):
        stdscr.addstr("\nCourse not found!")
        stdscr.getch()
        return

    for student in students:
        stdscr.clear()
        stdscr.addstr(f"Enter mark for {student.name}: ")
        try:
            score = float(stdscr.getstr().decode('utf-8'))
            student.marks[course_id] = math.floor(score * 10) / 10.0
        except ValueError:
            pass
    curses.noecho()