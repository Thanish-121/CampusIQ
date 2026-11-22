import pandas as pd 
#Loading student data
students = pd.read_csv("data/raw/student_performance.csv")
#displying the students
print("WELCOME TO CAMPUSIQ")
print("----------------")
print(students)
#disply total number of students
print("\nTotal students:", len(students))