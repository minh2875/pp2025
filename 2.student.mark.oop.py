students = []
courses = []
marks = {}
def input_number_of_students():
    n = int(input("Enter number of students: "))
    return n
def input_student_information():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (DD/MM/YYYY): ")
    return (student_id, name, dob)
def input_number_of_courses():
    n = int(input("Enter number of courses: "))
    return n
def input_course_information():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return (course_id, name)
def input_marks_for_course(course_id):
    for student in students:
        mark = float(input(f"Enter mark for student {student[1]} (ID: {student[0]}): "))
        if course_id not in marks:
            marks[course_id] = {}
        marks[course_id][student[0]] = mark
def list_courses():
    print("Courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")
def list_students():
    print("Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")
def show_student_marks_for_course(course_id):
    if course_id in marks:
        print(f"Marks for course ID {course_id}:")
        for student_id, mark in marks[course_id].items():
            print(f"Student ID: {student_id}, Mark: {mark}")
    else:
        print("No marks recorded for this course.")
# Main program
num_students = input_number_of_students()
for _ in range(num_students):
    student_info = input_student_information()
    students.append(student_info)
num_courses = input_number_of_courses()
for _ in range(num_courses):
    course_info = input_course_information()
    courses.append(course_info)
list_students()
list_courses()
selected_course_id = input("Enter course ID to input marks: ")
input_marks_for_course(selected_course_id)
show_student_marks_for_course(selected_course_id)

