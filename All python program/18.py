'''Create a program to take student information as input. Student will have First Name, Last Name, Roll No. Write a function
to sort the list based on given input parameter.
i.e By First Name or Last Name or Roll No.
'''
def sort_students(students, parameter):
    if parameter == "First Name":
        students.sort(key=lambda x: x[0])
    elif parameter == "Last Name":
        students.sort(key=lambda x: x[1])
    elif parameter == "Roll No":
        students.sort(key=lambda x: x[2])
    else:
        print("Invalid parameter!")
        return

    return students
if __name__ == '__main__':

    num_students = int(input("Enter the number of students: "))
    students = []
    for i in range(num_students):
        first_name = input("Enter the first name of student {}: ".format(i+1))
        last_name = input("Enter the last name of student {}: ".format(i+1))
        roll_no = int(input("Enter the roll no of student {}: ".format(i+1)))

        students.append((first_name, last_name, roll_no))

    parameter = input("Enter the sorting parameter (First Name / Last Name / Roll No): ")
    sorted_students = sort_students(students, parameter)

    if sorted_students:
        print("Sorted list of students:")
        for student in sorted_students:
            print("First Name:", student[0])
            print("Last Name:", student[1])
            print("Roll No:", student[2])
