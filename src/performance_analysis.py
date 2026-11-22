import pandas as pd

FILE_PATH = "data/raw/student_performance.csv"

def analyz_performance():
    student = pd.read_csv(FILE_PATH)
    print("\n==== STUDENT PERFORMANCE ANALYSIS ===")
    average_marks = student["final_score"].mean()
    print("\nAverage marks:", average_marks)
    highest_student = student.loc[student["final_score"].idxmax()]
    print("\nHighest-scoring student:")
    print("Name:", highest_student["name"])
    print("Marks:", highest_student["final_score"])
    lowest_student = student.loc[student["final_score"].idxmin()]
    print("\nLowest-scoring student:")
    print("Name:", lowest_student["name"])
    print("Marks:", lowest_student["final_score"])
    average_attendance = student["attendance"].mean()
    print("\nAverage attendance:", average_attendance, "%")

    # Calculate average study hours
    average_study_hours = student["study_hours"].mean()
    print("Average study hours:", average_study_hours)

if __name__ == "__main__":
    analyz_performance()