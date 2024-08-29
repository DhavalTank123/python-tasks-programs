'''Read a sentence from the standard input. Find out how many times each word appear in given string.

1. i.e Input : “This is a Python learning”

2. Ouptput :
This 1
Is 1
a 1
Python 1
Learning 1
'''
def count_words(sentence):
    words = sentence.split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

if __name__ == '__main__':
    print("enter string : ")
    s = input()
    print(count_words(s))