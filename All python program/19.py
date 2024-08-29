'''Write a function that given a string it returns true if the string is a number. As there might be several definitions of what is
the number create several solutions one for each definition:
 Non negative integer.
 Integer.
 Real number.
 In scientific notation. (something like this: 2.123e4 )
 '''
def is_non_negative_integer(s: str) -> bool:
    return s.isdigit()
def is_integer(s: str) -> bool:
    if s.startswith('-'):
        return s[1:].isdigit()
    return s.isdigit()
def is_real_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False
def is_scientific_notation(s: str) -> bool:
    try:
        float(s)
        return 'e' in s.lower()
    except ValueError:
        return False

if __name__ == '__main__':
    test_strings = [
        '123', '0', '-123', '3.14', '0.001', '1e10', '-1.23e-4', 'abc', '1.2.3'
    ]

    for s in test_strings:
        print(f"Testing '{s}':")
        print(f"  Non-negative integer: {is_non_negative_integer(s)}")
        print(f"  Integer: {is_integer(s)}")
        print(f"  Real number: {is_real_number(s)}")
        print(f"  Scientific notation: {is_scientific_notation(s)}")

