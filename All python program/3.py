'''Write a function to find larger of two numbers'''
# def large(n1,n2):
#     print("large is ",n1 if n1>n2 else n2)

large=lambda n1,n2:n1 if n1>n2 else n2

if __name__ == '__main__':
    # large(10,20)
    print(large(10,20))
