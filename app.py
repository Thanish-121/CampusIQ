import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


# ==================================
# 1. FILE LOCATION
# ==================================

FILE_PATH = "data/raw/student_performance.csv"


# ==================================
# 2. LOAD STUDENT DATA
# ==================================

def load_data():
    return pd.read_csv(FILE_PATH)


# ==================================
# 3. ADD NEW STUDENT
# ==================================

def add_student(name, study_hours, attendance,
                previous_score, assignments, final_score):

    students = load_data()

    new_student = {
        "student_id": int(students["student_id"].max()) + 1,
        "name": name,
        "study_hours": study_hours,
        "attendance": attendance,
        "previous_score": previous_score,
        "assignments_completed": assignments,
        "final_score": final_score
    }

    students.loc[len(students)] = new_student
    students.to_csv(FILE_PATH, index=False)


# ==================================
# 4. LOAD DATA
# ==================================

students = load_data()


# ==================================
# 5. PREPARE MACHINE LEARNING DATA
# ==================================

X = students[
    [
        "study_hours",
        "attendance",
        "previous_score",
        "assignments_completed"
    ]
]

y = students["final_score"]


# ==================================
# 6. SPLIT TRAINING AND TESTING DATA
# ==================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==================================
# 7. TRAIN MACHINE LEARNING MODEL
# ==================================

test_model = LinearRegression()

test_model.fit(X_train, y_train)


# ==================================
# 8. TEST THE MODEL
# ==================================

test_predictions = test_model.predict(X_test)

mae = mean_absolute_error(
    y_test,
    test_predictions
)


# Train final model using all available records
model = LinearRegression()
model.fit(X, y)


# ==================================
# 9. DASHBOARD TITLE
# ==================================

st.title("CampusIQ")

st.subheader("Student Performance Dashboard")

st.write("Welcome to CampusIQ!")

st.write(
    "An AI-powered academic analytics platform."
)


# ==================================
# 10. STUDENT STATISTICS
# ==================================

st.subheader("Student Statistics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Students",
    len(students)
)

col2.metric(
    "Average Marks",
    round(students["final_score"].mean(), 2)
)

col3.metric(
    "Average Attendance",
    str(round(students["attendance"].mean(), 2)) + "%"
)


# ==================================
# 11. STUDENT RECORDS
# ==================================

st.subheader("All Student Records")

st.dataframe(
    students,
    use_container_width=True
)


# ==================================
# 12. STUDENT MARKS CHART
# ==================================

st.subheader("Student Final Marks")

st.bar_chart(
    students,
    x="name",
    y="final_score"
)


# ==================================
# 13. STUDY HOURS CHART
# ==================================

st.subheader("Study Hours vs Final Marks")

st.scatter_chart(
    students,
    x="study_hours",
    y="final_score"
)


# ==================================
# 14. ATTENDANCE CHART
# ==================================

st.subheader("Attendance vs Final Marks")

st.scatter_chart(
    students,
    x="attendance",
    y="final_score"
)


# ==================================
# 15. ADD NEW STUDENT FORM
# ==================================

st.subheader("Add New Student")

with st.form("student_form"):

    name = st.text_input("Student Name")

    study_hours = st.number_input(
        "Study Hours Per Day",
        min_value=0.0,
        max_value=24.0,
        step=0.5
    )

    attendance = st.number_input(
        "Attendance Percentage",
        min_value=0.0,
        max_value=100.0
    )

    previous_score = st.number_input(
        "Previous Score",
        min_value=0.0,
        max_value=100.0
    )

    assignments = st.number_input(
        "Completed Assignments",
        min_value=0,
        step=1
    )

    final_score = st.number_input(
        "Final Score",
        min_value=0.0,
        max_value=100.0
    )

    submit = st.form_submit_button("Add Student")

    if submit:

        if name.strip() == "":
            st.error("Please enter a student name.")

        else:

            add_student(
                name,
                study_hours,
                attendance,
                previous_score,
                assignments,
                final_score
            )

            st.success("Student added successfully!")

            st.rerun()


# ==================================
# 16. MACHINE LEARNING TEST RESULTS
# ==================================

st.subheader("Machine Learning Model Testing")

col1, col2 = st.columns(2)

col1.metric(
    "Training Records",
    len(X_train)
)

col2.metric(
    "Testing Records",
    len(X_test)
)

st.metric(
    "Mean Absolute Error (MAE)",
    f"{mae:.2f} marks"
)

st.write("Actual vs Predicted Marks")

results = pd.DataFrame({
    "Actual Marks": y_test.values,
    "Predicted Marks": test_predictions
})

st.dataframe(
    results,
    use_container_width=True
)

st.caption(
    "Testing uses a held-out portion of the dataset. "
    "The dataset currently contains only fictional sample records, "
    "so these results do not establish real-world model accuracy."
)


# ==================================
# 17. AI STUDENT PERFORMANCE PREDICTION
# ==================================

st.subheader("AI Student Performance Prediction")

st.write(
    "Enter student details to estimate their final marks."
)

with st.form("prediction_form"):

    pred_study_hours = st.number_input(
        "Study Hours",
        min_value=0.0,
        max_value=24.0,
        key="pred_study"
    )

    pred_attendance = st.number_input(
        "Attendance",
        min_value=0.0,
        max_value=100.0,
        key="pred_attendance"
    )

    pred_previous_score = st.number_input(
        "Previous Score",
        min_value=0.0,
        max_value=100.0,
        key="pred_previous"
    )

    pred_assignments = st.number_input(
        "Completed Assignments",
        min_value=0,
        key="pred_assignments"
    )

    predict_button = st.form_submit_button(
        "Predict Final Marks"
    )


if predict_button:

    new_student = pd.DataFrame({
        "study_hours": [pred_study_hours],
        "attendance": [pred_attendance],
        "previous_score": [pred_previous_score],
        "assignments_completed": [pred_assignments]
    })

    prediction = model.predict(new_student)

    st.success(
        f"Estimated Final Marks: {prediction[0]:.2f}"
    )

    st.caption(
        "This is an experimental estimate based on a small "
        "synthetic dataset, not a reliable academic prediction."
    )