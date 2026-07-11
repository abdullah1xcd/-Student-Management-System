import streamlit as st
from student import Student

st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# Session State
# -----------------------------
if "students" not in st.session_state:
    st.session_state.students = []

students = st.session_state.students

# -----------------------------
# Title
# -----------------------------
st.title("🎓 Student Management System")

# -----------------------------
# Sidebar Menu
# -----------------------------
menu = st.sidebar.selectbox(
    "Menu",
    [
        "Add Student",
        "Add Grades",
        "Show All Students",
        "Search Student",
        "Delete Student",
        "Statistics"
    ]
)

# ==================================================
# Add Student
# ==================================================
if menu == "Add Student":

    st.header("Add New Student")

    name = st.text_input("Student Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        step=1
    )

    student_id = st.text_input("Student ID")

    if st.button("Add Student"):

        if name == "" or student_id == "":
            st.error("Please fill all fields.")

        else:

            found = False

            for student in students:
                if student.student_id == student_id:
                    found = True

            if found:
                st.error("Student ID already exists.")

            else:

                new_student = Student(
                    name,
                    age,
                    student_id
                )

                students.append(new_student)

                st.success("Student Added Successfully!")

# ==================================================
# Add Grades
# ==================================================
elif menu == "Add Grades":

    st.header("Add Grades")

    student_id = st.text_input("Student ID")

    grade = st.number_input(
        "Grade",
        min_value=0,
        max_value=100,
        step=1
    )

    if st.button("Add Grade"):

        found = False

        for student in students:

            if student.student_id == student_id:

                student.add_grade(grade)

                st.success("Grade Added Successfully.")

                found = True

                break

        if not found:
            st.error("Student Not Found.")

# ==================================================
# Show Students
# ==================================================
elif menu == "Show All Students":

    st.header("All Students")

    if len(students) == 0:
        st.warning("No students available.")

    else:

        for student in students:

            info = student.display_info()

            st.subheader(info["Name"])

            st.write("Student ID:", info["Student ID"])
            st.write("Age:", info["Age"])
            st.write("Grades:", info["Grades"])
            st.write("Average:", info["Average"])
            st.write("Status:", info["Status"])
            st.write("GPA:", info["GPA"])

            st.divider()

# ==================================================
# Search Student
# ==================================================
elif menu == "Search Student":

    st.header("Search Student")

    student_id = st.text_input("Enter Student ID")

    if st.button("Search"):

        found = False

        for student in students:

            if student.student_id == student_id:

                info = student.display_info()

                st.success("Student Found")

                st.write("### Student Information")

                st.write("Name:", info["Name"])
                st.write("Age:", info["Age"])
                st.write("Student ID:", info["Student ID"])
                st.write("Grades:", info["Grades"])
                st.write("Average:", info["Average"])
                st.write("Status:", info["Status"])
                st.write("GPA:", info["GPA"])

                found = True

                break

        if not found:
            st.error("Student Not Found.")

# ==================================================
# Delete Student
# ==================================================
elif menu == "Delete Student":

    st.header("Delete Student")

    student_id = st.text_input("Student ID")

    if st.button("Delete"):

        found = False

        for student in students:

            if student.student_id == student_id:

                students.remove(student)

                st.success("Student Deleted Successfully.")

                found = True

                break

        if not found:
            st.error("Student Not Found.")

# ==================================================
# Statistics
# ==================================================
elif menu == "Statistics":

    st.header("Statistics")

    if len(students) == 0:

        st.warning("No students.")

    else:

        highest = students[0]

        passed = 0
        failed = 0

        for student in students:

            if student.calculate_average() > highest.calculate_average():
                highest = student

            if student.calculate_average() >= 60:
                passed += 1
            else:
                failed += 1

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Students", len(students))

        with col2:
            st.metric("Passed", passed)

        with col3:
            st.metric("Failed", failed)

        st.divider()

        st.subheader("🏆 Highest Average Student")

        info = highest.display_info()

        st.write("Name:", info["Name"])
        st.write("Average:", info["Average"])
        st.write("Status:", info["Status"])
        st.write("GPA:", info["GPA"])