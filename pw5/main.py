import curses
import os
import zipfile
from input import add_students, add_courses, add_marks
from output import show_marks, show_students, show_courses, calculate_GPA_and_short

def save_data(students, courses):
    with open("data.txt", "w", encoding="utf-8") as f:
        for student in students:
            marks_str = str(student.marks)
            f.write(f"student|{student.id}|{student.name}|{student.dob}|{marks_str}\n")
        for course in courses:
            f.write(f"course|{course.course_id}|{course.course_name}|{course.credit}\n")

    with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write("data.txt")

    if os.path.exists("data.txt"):
        os.remove("data.txt")
        
def main(stdscreen):
    students = []
    courses = []
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