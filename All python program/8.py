'''
Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
 If the string length is less than 2, return "Empty String"
 '''
def cheack_isempty(str):
    if len(str)<=2:
        print("Empty String")
    else:
        print(str[0])
        print(str[1])
        print(str[-2])
        print(str[-1])
    # for i in str:
    #     if str.index(i) == 0 :
    #         print(str[0])
    #     elif str.index(i) == 1:
    #         print(str[1])
    #     elif str.index(i) == -1:
    #         print(str[-1])
    #     elif str.index(i) == -2 :
    #         print(str[-2])



if __name__ == '__main__':
    print("Enetr a string:")
    str = input()
    cheack_isempty(str)
