import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
FILE_PATH = "data/raw/student_performance.csv"
students = pd.read_csv(FILE_PATH)
print(students.head())
X = students[
    ["study_hours", "attendance", "previous_score", "assignments_completed"]
]

y = students["final_score"]

print("\nInput Data:")
print(X.head())

print("\nOutput Data:")
print(y.head())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))
model = LinearRegression()
model.fit(X_train,y_train)
print("\nModel training compled!")
print("\nMaking predicition....")
predictions = model.predict(X_test)
print("\nPredicted Marks:")
print(predictions)
mae = mean_absolute_error(y_test,predictions)
print("\nMean Absolute Error:", mae)
new_student = pd.DataFrame({
    "study_hours": [6],
    "attendance": [85],
    "previous_score": [70],
    "assignments_completed": [8]
})

new_prediction = model.predict(new_student)

print("\nNew Student Predicted Marks:", new_prediction[0])
