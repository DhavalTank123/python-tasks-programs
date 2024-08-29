import json
import pickle
import os

class Employee:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Employee(name={self.name}, age={self.age}, gender={self.gender})"

    # Convert object to dictionary
    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }


    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['age'], data['gender'])

def serialize_to_json(employee, filename):
    with open(filename, 'w') as file:
        json.dump(employee.to_dict(), file)

def deserialize_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return Employee.from_dict(data)


def serialize_to_pickle(employee, filename):
    with open(filename, 'wb') as file:
        pickle.dump(employee, file)

def deserialize_from_pickle(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


class ComplexClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def __str__(self):
        return f"ComplexClass(attribute1={self.attribute1}, attribute2={self.attribute2})"


def serialize_complex_class(instance, filename):
    with open(filename, 'wb') as file:
        pickle.dump(instance, file)

def deserialize_complex_class(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

def main():

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")


    emp = Employee(name, age, gender)

    # Serialize to JSON and Pickle
    serialize_to_json(emp, 'employee.json')
    serialize_to_pickle(emp, 'employee.pkl')

    emp_from_json = deserialize_from_json('employee.json')
    emp_from_pickle = deserialize_from_pickle('employee.pkl')

    print("Deserialized from JSON:", emp_from_json)
    print("Deserialized from Pickle:", emp_from_pickle)

    emp_from_json.name = input("Update name: ")
    emp_from_json.age = int(input("Update age: "))
    emp_from_json.gender = input("Update gender: ")

    serialize_to_json(emp_from_json, 'employee.json')
    serialize_to_pickle(emp_from_json, 'employee.pkl')

    # Create and handle complex class
    complex_instance = ComplexClass('value1', 'value2')
    serialize_complex_class(complex_instance, 'complex.pkl')
    deserialized_complex_instance = deserialize_complex_class('complex.pkl')

    print("Deserialized ComplexClass:", deserialized_complex_instance)

  
    try:
        with open('example.txt', 'w') as file:
            pickle.dump(file, open('file_handler.pkl', 'wb'))
    except Exception as e:
        print(f"Failed to serialize file handler: {e}")

if __name__ == "__main__":
    main()
