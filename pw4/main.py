import curses
from input import add_students, add_courses, add_marks
from output import show_students, show_courses, calculate_GPA_and_short

@staticmethod
def main(stdscreen):
    student = []
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
    curses.wrapper(main)