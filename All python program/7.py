'''
Write a python function which counts the frequency of given character in a given string.
 Inputs - A String
 A Character whose frequency needs to be determined
'''
def count_frequency(str1):
    count=0
    for i in str1:
        count = count + 1
    return count
if __name__ == '__main__':
    print("enter string")
    s = input()
    print(f"the frequncy os given string is {count_frequency(s)} ")
