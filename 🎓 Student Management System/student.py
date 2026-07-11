class Student:

    # Constructor
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []

    # Add grade
    def add_grade(self, score):
        self.grades.append(score)

    # Calculate average
    def calculate_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    # Student status
    def get_status(self):
        avg = self.calculate_average()

        if avg >= 90:
            return "Excellent"
        elif avg >= 80:
            return "Very Good"
        elif avg >= 70:
            return "Good"
        elif avg >= 60:
            return "Pass"
        else:
            return "Fail"

    # GPA
    def get_gpa(self):
        avg = self.calculate_average()

        if avg >= 90:
            return 4.0
        elif avg >= 80:
            return 3.5
        elif avg >= 70:
            return 3.0
        elif avg >= 60:
            return 2.0
        else:
            return 0.0

    # Display student information
    def display_info(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Student ID": self.student_id,
            "Grades": self.grades,
            "Average": round(self.calculate_average(), 2),
            "Status": self.get_status(),
            "GPA": self.get_gpa()
        }