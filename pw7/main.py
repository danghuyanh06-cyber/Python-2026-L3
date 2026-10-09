import curses
import os
import pickle
import zipfile
import csv
import pandas as pd
from input import add_students, add_courses, add_marks
from output import show_marks, show_students, show_courses, calculate_GPA_and_short

def save_data(students, courses):
    with open("data.pkl", "wb") as f:
        pickle.dump((students, courses), f)
    with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write("data.pkl")
    if os.path.exists("data.pkl"):
        os.remove("data.pkl")
def load_data():
    if os.path.exists("students.dat"):
        try:
            with zipfile.ZipFile("students.dat", "r") as zipf:
                zipf.extract("data.pkl")
            with open("data.pkl", "rb") as f:
                students, courses = pickle.load(f)
            if os.path.exists("data.pkl"):
                os.remove("data.pkl")
            return students, courses
        except Exception:
            return [], []
    return [], []
def export_to_csv(stdscreen, students, courses):
    stdscreen.clear()
    try:
        with open("students.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name", "dob", "gpa"])
            for s in students:
                writer.writerow([s.id, s.name, s.dob, s.gpa])  
        with open("courses.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name", "credit"])
            for c in courses:
                writer.writerow([c.id, c.name, c.credit])
        with open("marks.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["student_id", "course_id", "mark"])
            for s in students:
                for cid, mark in s.marks.items():
                    writer.writerow([s.id, cid, mark])                  
        stdscreen.addstr("Exported successfully to CSV files!\n", curses.A_BOLD)
    except Exception as e:
        stdscreen.addstr(f"Error exporting to CSV: {e}\n")   
    stdscreen.addstr("\nPress any key to continue...")
    stdscreen.getch()
def query_students(stdscreen):
    stdscreen.clear()
    try:
        df_students = pd.read_csv("students.csv")
    except FileNotFoundError:
        stdscreen.addstr("students.csv not found! Please Export to CSV first.\n")
        stdscreen.addstr("\nPress any key to continue...")
        stdscreen.getch()
        return
    stdscreen.addstr("Enter query condition:\n")
    curses.echo()
    condition = stdscreen.getstr().decode('utf-8')
    curses.noecho( )
    if condition.count('=') == 1 and ('<' not in condition and '>' not in condition and '!' not in condition):
        condition = condition.replace('=', '==')
    stdscreen.addstr("\nQuery Results:\n", curses.A_BOLD)
    try:
        result = df_students.query(condition)
        if result.empty:
            stdscreen.addstr("No records found.\n")
        else:
            stdscreen.addstr(result.to_string())
    except Exception as e:
        stdscreen.addstr(f"Invalid query syntax. Error: {e}\n")

    stdscreen.addstr("\n\nPress any key to continue...")
    stdscreen.getch()
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
            export_to_csv(stdscreen, students, courses)
        elif choice == '9':
            query_students(stdscreen)
        elif choice == '0':
            save_data(students, courses)
            stdscreen.addstr("\nData compressed and saved to students.dat using Pickle. Exiting...")
            stdscreen.refresh()
            curses.napms(1500)
            break
        else:
            stdscreen.addstr("Invalid choice. Press any key to continue...")
            stdscreen.getch()


if __name__ == "__main__":
    curses.wrapper(main)