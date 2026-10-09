import curses
import os
import zipfile
from domains.student import Student
from domains.course import Course
from input import add_students, add_courses, add_marks
from output import show_marks, show_students, show_courses, calculate_GPA_and_short

def save_data(students, courses):
    with open("students.txt", "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s.id}|{s.name}|{s.dob}\n")
    with open("courses.txt", "w", encoding="utf-8") as f:
        for c in courses:
            f.write(f"{c.course_id}|{c.course_name}|{c.credit}\n")
            
    with open("marks.txt", "w", encoding="utf-8") as f:
        for s in students:
            for cid, mark in s.marks.items():
                f.write(f"{s.id}|{cid}|{mark}\n")
    with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write("students.txt")
        zipf.write("courses.txt")
        zipf.write("marks.txt")
    for file in ["students.txt", "courses.txt", "marks.txt"]:
        if os.path.exists(file):
            os.remove(file)

def load_data():
    students = []
    courses = []
    if os.path.exists("students.dat"):
        try:
            with zipfile.ZipFile("students.dat", "r") as zipf:
                zipf.extractall()
            if os.path.exists("students.txt"):
                with open("students.txt", "r", encoding="utf-8") as f:
                    for line in f:
                        parts = line.strip().split('|')
                        if len(parts) == 3:
                            students.append(Student(parts[0], parts[1], parts[2]))                           
            if os.path.exists("courses.txt"):
                with open("courses.txt", "r", encoding="utf-8") as f:
                    for line in f:
                        parts = line.strip().split('|')
                        if len(parts) == 3:
                            courses.append(Course(parts[0], parts[1], int(parts[2])))             
            if os.path.exists("marks.txt"):
                with open("marks.txt", "r", encoding="utf-8") as f:
                    for line in f:
                        parts = line.strip().split('|')
                        if len(parts) == 3:
                            sid, cid, mark = parts[0], parts[1], float(parts[2])
                            for s in students:
                                if s.id == sid:
                                    s.marks[cid] = mark
            for file in ["students.txt", "courses.txt", "marks.txt"]:
                if os.path.exists(file):
                    os.remove(file)
        except Exception:
            pass
            
    return students, courses
        
def main(stdscreen):
    students, courses = load_data()
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
            add_students(stdscreen, students)
        elif choice == '2':
            add_courses(stdscreen, courses)
        elif choice == '3':
            add_marks(stdscreen, students, courses)
        elif choice == '4':
            show_students(stdscreen, students)
        elif choice == '5':
            show_courses(stdscreen, courses)
        elif choice == '6':
            show_marks(stdscreen, students)
        elif choice == '7':
            calculate_GPA_and_short(students, courses, stdscreen)
        elif choice == '8':
            save_data(students, courses)
            stdscreen.addstr("\nData saved to students.dat. Exiting...")
            stdscreen.refresh()
            curses.napms(1000)
            break
        else:
            stdscreen.addstr("Invalid choice. Press any key to continue...")
            stdscreen.getch()


if __name__ == "__main__":
    curses.wrapper(main)