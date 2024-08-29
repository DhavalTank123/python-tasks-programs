'''Write a program to read names and grades of each student in class of N student. Store these details into nested list.
Write a function to find student with second highest marks.'''

def read_students(n):
    students = []
    for _ in range(n):
        name = input("Enter your name: ")
        grade = float(input("Enter your grade: "))
        students.append([name, grade])
    return students

def find_second_highest(students):
    if not students:
        return []

    highest_grade = float('-inf')
    second_highest_grade = float('-inf')

    for student in students:
        grade = student[1]
        if grade > highest_grade:
            highest_grade = grade

    for student in students:
        grade = student[1]
        if highest_grade > grade > second_highest_grade:
            second_highest_grade = grade

    second_highest_students = []
    for student in students:
        if student[1] == second_highest_grade:
            second_highest_students.append(student)

    return second_highest_students

if __name__ == '__main__':
    n = int(input("Enter the number of students: "))
    students = read_students(n)

    for _ in range(n):
        name = input("Enter your name: ")
        grade = float(input("Enter your grade: "))
        students.append([name, grade])
        
    second_highest_students = find_second_highest(students)
    print("Students with the second highest marks:")
    for student in second_highest_students:
        print(student[0], "with grade", student[1])
