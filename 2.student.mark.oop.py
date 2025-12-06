class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}"

class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

class ManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        print("Enter number of students: ")
        n = int(input())
        for i in range(n):
            print(f"--- Entering info for student {i+1} ---")
            s_id = input("Enter student ID: ")
            s_name = input("Enter student name: ")
            s_dob = input("Enter student DoB: ")
            new_student = Student(s_id, s_name, s_dob)
            self.students.append(new_student)

    def input_courses(self):
        print("Enter number of courses: ")
        n = int(input())
        for i in range(n):
            print(f"--- Entering info for course {i+1} ---")
            c_id = input("Enter course ID: ")
            c_name = input("Enter course name: ")
            new_course = Course(c_id, c_name)
            self.courses.append(new_course)

    def list_items(self):
        for student in self.students:
            print(student)
        for course in self.courses:
            print(course)

    def input_marks(self):
        course_id = input("\nEnter course ID to input marks for: ")
        for student in self.students:
            print(f"Enter mark for student: {student.name}")
            mark_value = float(input())
            student.marks[course_id] = mark_value

    def show_marks(self):
        course_id = input("\nEnter course ID to show marks: ")
        print(f"Marks for course ID {course_id}:")
        for student in self.students:
            score = student.marks.get(course_id, "Not graded")
            print(f"Student: {satudent.name}, Mark: {score}")

    def run(self):
        self.input_students()
        self.input_courses()
        self.list_items()
        self.input_marks()
        self.show_marks()

if __name__ == "__main__":
    system = ManagementSystem()
    system.run()