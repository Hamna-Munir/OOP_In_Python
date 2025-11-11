import streamlit as st
import pandas as pd
from datetime import date
import os

# ---------------------------
#  Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="wide"
)

DATA_FILE = "students_data.csv"

# ---------------------------
#  Student Class
# ---------------------------
class Student:
    def __init__(self, roll_no, name, department, dob, email):
        self.roll_no = roll_no
        self.name = name
        self.department = department
        self.dob = dob
        self.email = email

    def get_info(self):
        return {
            "Roll No": self.roll_no,
            "Name": self.name,
            "Department": self.department,
            "Date of Birth": str(self.dob),
            "Email": self.email
        }

# ---------------------------
#  Student Management System
# ---------------------------
class StudentManagementSystem:
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.students = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            df = pd.read_csv(self.data_file)
            for _, row in df.iterrows():
                student = Student(
                    row["Roll No"],
                    row["Name"],
                    row["Department"],
                    row["Date of Birth"],
                    row["Email"]
                )
                self.students[student.roll_no] = student

    def save_data(self):
        data = [s.get_info() for s in self.students.values()]
        pd.DataFrame(data).to_csv(self.data_file, index=False)

    def add_student(self, student: Student):
        if student.roll_no in self.students:
            return False
        self.students[student.roll_no] = student
        self.save_data()
        return True

    def view_students(self):
        return [s.get_info() for s in self.students.values()]

    def get_student(self, roll_no):
        return self.students.get(roll_no)

    def delete_student(self, roll_no):
        if roll_no in self.students:
            del self.students[roll_no]
            self.save_data()
            return True
        return False

    def update_student(self, roll_no, **kwargs):
        student = self.students.get(roll_no)
        if not student:
            return False
        for key, value in kwargs.items():
            if hasattr(student, key):
                setattr(student, key, value)
        self.save_data()
        return True


# ---------------------------
#  Initialize Session
# ---------------------------
if "system" not in st.session_state:
    st.session_state.system = StudentManagementSystem()

system = st.session_state.system

# ---------------------------
#  Sidebar Developer Info
# ---------------------------
st.sidebar.markdown("### 👩‍💻 Developer Information")
st.sidebar.markdown("""
**Hamna Munir**  
[🌐 LinkedIn](https://www.linkedin.com/in/hamna-munir-6891a72a0/)  
[💻 GitHub](https://github.com/Hamna-Munir)  
[📁 OOP Repository](https://github.com/Hamna-Munir/OOP_In_Python/tree/main/11_OOP_Project_Practice)
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📋 Navigation")

menu = st.sidebar.radio(
    "",
    ["Add Student", "View Students", "Update Student", "Delete Student"]
)

# ---------------------------
#  Main Page
# ---------------------------
st.title("🎓 Student Management System")
st.markdown("""
This application is built using **Python OOP (Object-Oriented Programming)** principles  
and **Streamlit** for the user interface.

It demonstrates modular, reusable, and persistent student management functionality.
""")

# ---------------------------
#  Add Student
# ---------------------------
if menu == "Add Student":
    st.header("➕ Add New Student")

    with st.form("add_student_form"):
        roll_no = st.text_input("Roll Number")
        name = st.text_input("Full Name")
        department = st.selectbox(
            "Department",
            ["Software Engineering", "Computer Science", "Information Technology", "Artificial Intelligence", "Data Science"]
        )
        dob = st.date_input("Date of Birth", date(2000, 1, 1))
        email = st.text_input("Email Address")

        submit = st.form_submit_button("Add Student")

        if submit:
            if not roll_no or not name or not email:
                st.warning("⚠️ Please fill in all required fields.")
            else:
                student = Student(roll_no, name, department, dob, email)
                if system.add_student(student):
                    st.success(f"✅ Student **{name}** added successfully!")
                else:
                    st.error(f"🚫 Roll No **{roll_no}** already exists!")

# ---------------------------
#  View Students
# ---------------------------
elif menu == "View Students":
    st.header("📖 View All Students")
    students = system.view_students()

    if students:
        df = pd.DataFrame(students)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No student records found. Please add some students first.")

# ---------------------------
#  Update Student
# ---------------------------
elif menu == "Update Student":
    st.header("✏️ Update Student Information")
    roll_no = st.text_input("Enter Roll No to Update")

    if st.button("Fetch Student"):
        student = system.get_student(roll_no)
        if student:
            st.success(f"🎯 Student found: {student.name}")
            with st.form("update_form"):
                new_name = st.text_input("Full Name", student.name)
                new_department = st.selectbox(
                    "Department",
                    ["Software Engineering", "Computer Science", "Information Technology", "Artificial Intelligence", "Data Science"],
                    index=0
                )
                new_dob = st.date_input("Date of Birth", date.fromisoformat(str(student.dob)))
                new_email = st.text_input("Email Address", student.email)
                update_btn = st.form_submit_button("Update")

                if update_btn:
                    system.update_student(
                        roll_no,
                        name=new_name,
                        department=new_department,
                        dob=new_dob,
                        email=new_email
                    )
                    st.success("✅ Student information updated successfully!")
        else:
            st.error("❌ No student found with this Roll No.")

# ---------------------------
#  Delete Student
# ---------------------------
elif menu == "Delete Student":
    st.header("🗑️ Delete Student Record")
    roll_no = st.text_input("Enter Roll No to Delete")

    if st.button("Delete"):
        if system.delete_student(roll_no):
            st.success(f"✅ Student with Roll No **{roll_no}** deleted successfully.")
        else:
            st.error("❌ No student found with this Roll No.")
