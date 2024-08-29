'''
Write a program to take two numbers as input parameter and then ask for the arithmetic parameter to be performed.
i.e “Enter Two numbers”
10 45
“Operations to perform “ +
Sum is 55
5.
'''
def runmatch():
    print("Enter Two numbers",end="")
    a = int(input())
    b = int(input())
    print("Operations to perform ")
    option=input()

    match option:
        case'+':
            print(f"sum is {a + b}")
        case '-':
            print(f"subtraction is {a - b}")
        case '*':
            print(f"multiplication is {a * b}")
        case '/':
            print(f"division is {a / b}")
        case '//':
            print(f"floar division is {a // b}")
        case '%':
            print(f"modulo is {a % b}")

if __name__ == '__main__':
    runmatch()