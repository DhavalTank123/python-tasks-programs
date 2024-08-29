'''
Write a program to take two integers as input. Print those two integers as output and then call a function to swap those
two
integers.
'''
def swap(x,y):
    temp=x
    x=y
    y=temp
    print(f"n1 = {x} n2 = {y}")

if __name__ == '__main__':

    print("Enter n1:")
    x = int(input())

    print("Enter n2:")
    y = int(input())

    swap(x, y)



