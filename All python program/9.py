'''
Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
 If the given string already ends with 'ing' then add 'ly' instead.
 If the string length of the given string is less than 3, leave it unchanged.
 '''
def check(str):
    if len(str)<=3:
        return "length should be at least 3"
    elif str[-3:] == 'ing':
        return  str + 'ly'
    else:
        return str + 'ing'

    # elif str[-1] + str[-2] + str[-3]=="ing":
    #     return str+"ly"
    # else:
    #     return str+"ing"

if __name__ == '__main__':
    print(check("dhaing"))
