'''Write a program to take size of the list as input. Then read as many values as input. Store these details into list and print
out list.'''
def fun(size):
    l = []
    for i in range(size):
        print("Enter value")
        value = input()
        l.append(value)
    return l

if __name__ == '__main__':
    print("Enter size")
    size =int(input())
    print(fun(size))