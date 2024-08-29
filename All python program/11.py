'''
Write a Python function to insert a string in the middle of a string.
 For odd length of string, remove the middle character and replace with given string.

 '''

def insert_string_middle(original_string, string_to_insert):

    if len(original_string) % 2 == 0:
        middle_index = len(original_string) // 2
    else:
        middle_index = len(original_string) // 2 + 1
        original_string = original_string[:middle_index-1] + original_string[middle_index:]

    return original_string[:middle_index] + string_to_insert + original_string[middle_index:]

if __name__ == '__main__':

    original_string =input("Enter a string:")
    string_to_insert =input("Enter string you want to insert:")
    result = insert_string_middle(original_string, string_to_insert)
    print(result)