import pandas as pd

df_student = pd.read_csv("students.csv")

print("First five rows:")
print(df_student.head())

rows, columns = df_student.shape
print(f"\nNumber of rows: {rows}, number of columns: {columns}")

print("\nStudent names and GPAs:")
print(df_student[["name", "GPA"]])

print("\nStudents with GPA >= 3.5:")
print(df_student[df_student["GPA"] >= 3.5])

print("\nStudents sorted by GPA:")
print(df_student.sort_values(by="GPA"))

print("\nAverage GPA by major:")
print(df_student.groupby("major")["GPA"].mean())


