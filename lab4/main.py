from students_class import Student
from datetime import datetime, timedelta
import os


def read_students_from_file(filename):
    students = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='UTF-8') as file:
            for line in file:
                data = line.strip().split(',')
                name, dob = data[0], data[1]
                properties = data[2:] if len(data) > 2 else []
                student = Student(name, dob, properties)
                students.append(student)
    return students


def save_students_to_file(filename, students):
    with open(filename, 'w', encoding='UTF-8') as file:
        for student in students:
            student_data = [student.name, student.dob] + student.properties
            line = ','.join(student_data) + '\n'
            file.write(line)


def main():
    filename = 'students.txt'
    students = read_students_from_file(filename)
    print('List of students:')
    for student in students:
        print(student)

    num_students_to_add = int(input('\nHow many students do you want to add? '))
    for _ in range(num_students_to_add):
        name = input('Enter student\'s name: ')
        dob = input('Enter student\'s date of birth (DD.MM.YYYY): ')
        num_properties = int(input('How many properties do you want to add? '))
        properties = []
        for _ in range(num_properties):
            prop = input('Enter property: ')
            properties.append(prop)

        student = Student(name, dob, properties)
        students.append(student)

    save_students_to_file(filename, students)

    print('\nList of students:')
    for student in students:
        print(student)


if __name__ == '__main__':
    main()
