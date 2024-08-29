'''Write a program to find average of the list. List should not contain non arithmetic values.'''
# from functools import reduce
#
# def avg(size):
#     l = []
#     for i in range(size):
#         print("Enter value")
#         value = input()
#         l.append(value)
#     a = reduce(lambda a, b: a + b, l) / int((len(l)/2))
#     if a is not None:
#         print(a)
#     else:
#         print("non arithmetic values")
#
# if __name__ == '__main__':
#     avg(6)

def calculate_average(lst):
    total = 0
    count = 0
    for num in lst:
        if isinstance(num, (int, float)):
            total += num
            count += 1
    if count > 0:
        average = total / count
        return average
    else:
        return None

if __name__ == '__main__':
    size = int(input("Enter the size of the list: "))
    values = []
    for i in range(size):
        value = input("Enter a value: ")
        try:
            numeric_value = float(value) if '.' in value else int(value)
            values.append(numeric_value)
        except ValueError:
            values.append(value)

    average = calculate_average(values)
    if average is not None:
        print("Average of the list:", average)
    else:
        print("List contains non-arithmetic values.")