'''Create a python class Author. Create a python class for Programming languages which must inherite Author class.
Create a class which should print the details of given programming language as input.'''

class Author:
    def __init__(self):
        self.name = input("ENter name of Author")
class Programming_languages(Author):

    def __init__(self):
        super().__init__()
        self.p_l=input("Enter language name")
    def put(self):
        print(f"name of Author {self.name} and language name{self.p_l}")

if __name__ == '__main__':
    ob = Programming_languages()
    ob.put()