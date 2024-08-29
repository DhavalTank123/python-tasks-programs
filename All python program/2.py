'''
Write python script to take one integer argument and then print as follows:
 - If Value >0 and Value < 10 — Small
 - If Value > 10 and Value <100 — Medium
 - If Value <1000 — Large
 - If Value > 1000 — Invalid
 '''
if __name__ == '__main__':
    print('enter any nuber')
    n = int(input())
    if n>0 and n<10:
        print('small')
    elif n>10 and n<100:
        print('medium')
    elif n<1000:
        print('large')
    elif n>1000:
        print('invalid')
    else:
        pass