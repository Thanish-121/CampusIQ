import pandas as pd
from performance_analysis import analyz_performance

FILE_PATH = "data/raw/student_performance.csv"


def add_student():
    students = pd.read_csv(FILE_PATH)

    print("\n--- ADD NEW STUDENT ---")

    student_id = len(students) + 1
    name = input("Enter student name: ")
    study_hours = float(input("Enter study hours per day: "))
    attendance = float(input("Enter attendance percentage: "))
    previous_score = float(input("Enter previous marks: "))
    assignments = int(input("Enter completed assignments: "))
    final_score = float(input("Enter final score: "))

    new_student = {
        "student_id": student_id,
        "name": name,
        "study_hours": study_hours,
        "attendance": attendance,
        "previous_score": previous_score,
        "assignments_completed": assignments,
        "final_score": final_score
    }

    students.loc[len(students)] = new_student
    students.to_csv(FILE_PATH, index=False)

    print("\nStudent added successfully!")


def view_students():
    students = pd.read_csv(FILE_PATH)

    print("\n--- ALL STUDENTS ---")
    print(students.to_string(index=False))

    print("\nTotal students:", len(students))


def main():
    while True:
        print("\n===== CAMPUSIQ =====")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Performance Analysis")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            analyz_performance()    

        elif choice == "4":
            print("Thank you for using CampusIQ!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()