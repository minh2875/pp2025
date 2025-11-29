import math 
def input_number_of_students():
    n = int(input("Enter number of students: "))
    return n
def input_student_information(n):
    students = []
    for _ in range(n):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth (DoB): ")
        students.append({'id': student_id, 'name': name, 'dob': dob})
    return students
def input_number_of_courses():
    m = int(input("Enter number of courses: "))
    return m
def input_course_information(m):
    courses = []
    for _ in range(m):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append({'id': course_id, 'name': course_name})
    return courses
def input_marks_for_course(courses, students):
    course_id = input("Enter course ID to input marks for: ")
    selected_course = next((course for course in courses if course['id'] == course_id), None)
    if not selected_course:
        print("Course not found!")
        return {}
    marks = {}
    for student in students:
        mark = float(input(f"Enter mark for student {student['name']} (ID: {student['id']}): "))
        marks[student['id']] = mark
    return {course_id: marks}
def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")
def list_students(students):
    print("Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")
def show_student_marks_for_course(marks, courses):
    course_id = input("Enter course ID to show marks for: ")
    if course_id not in marks:
        print("No marks found for this course!")
        return
    print(f"Marks for course ID {course_id}:")
    for student_id, mark in marks[course_id].items():
        print(f"Student ID: {student_id}, Mark: {mark}")
def main():
    n = input_number_of_students()
    students = input_student_information(n)
    m = input_number_of_courses()
    courses = input_course_information(m)
    marks = input_marks_for_course(courses, students)
    list_courses(courses)
    list_students(students)
    show_student_marks_for_course(marks, courses)
if __name__ == "__main__":
    main()
