'''
Write a program to find index of given input parameter in the list.
'''
if __name__ == '__main__':
    l = [1 ,2 ,3 ,4 ,5]
    value = int(input("enter one element in this list [1,2,3,4,5] "))
    if value in l:
        print("index of list is ",l.index(value))
    else:
        print("invalid")

