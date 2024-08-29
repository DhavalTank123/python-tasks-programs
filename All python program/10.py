'''
Write a Python function to remove the characters which have odd index values of a given string.
'''
def r(str):
    c=""
    for i in range(len(str)):
        if i % 2==0:
            c+=str[i]
    return c

if __name__ == '__main__':
    print(r("dhaval"))