import pandas as pd 
import matplotlib.pyplot as plt

FILE_PATH = "data/raw/student_performance.csv"

def show_marks_chart():

    students = pd.read_csv(FILE_PATH)
    plt.figure(figsize=(10,5))
    plt.bar(students["name"],students["final_score"])
    plt.title("Student Final Marks")
    plt.xlabel("Student Name")
    plt.ylabel("Final score")
    plt.xticks(rotation=45)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def show_study_vs_marks():
    students = pd.read_csv(FILE_PATH)
    plt.figure(figsize=(8,5))
    plt.scatter(students["study_hours"],students["final_score"])
    import numpy as np
    x = students["study_hours"]
    y = students["final_score"]
    m, b = np.polyfit(x,y,1)
    plt.plot(x,m*x + b, color="red")
    plt.title("Study Hours vs Final Marks")
    plt.xlabel("Study Hours per day")
    plt.ylabel("final score")
    plt.grid(True)
    plt.show()
def show__attendance_vs_marks():
    students = pd.read_csv(FILE_PATH)
    plt.figure(figsize=(8,5))
    plt.scatter(students["attendance"],students["final_score"])
    import numpy as np
    x = students["attendance"]
    y = students["final_score"]
    m, b = np.polyfit(x,y,1)
    plt.plot(x,m*x + b, color="red")
    plt.title("Attendance vs Final Marks")
    plt.xlabel("Attendance")
    plt.ylabel("final score")
    plt.grid(True)
    plt.show()
if __name__ == "__main__":
    show_study_vs_marks()
    show_marks_chart()
    show__attendance_vs_marks()