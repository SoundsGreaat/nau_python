from datetime import datetime, timedelta


class Student:
    def __init__(self, name, dob, properties=None):
        if properties is None:
            properties = []

        self.name = name

        day, month, year = map(int, dob.split('.'))
        self.dob = datetime(year, month, day).strftime('%d.%m.%Y')

        self.properties = properties

    def __iadd__(self, days):
        if isinstance(days, int):
            self.dob = (datetime.strptime(self.dob, '%d.%m.%Y') + timedelta(days=days)).strftime('%d.%m.%Y')
        else:
            raise ValueError('Invalid data type, int expected')
        return self

    def add_properties(self, *args):
        self.properties.extend(args)

    def __str__(self):
        if self.properties:
            return f'Name: {self.name}, Date of Birth: {self.dob}, Properties: {", ".join(self.properties)}'
        return f'Name: {self.name}, Date of Birth: {self.dob}'


def example():
    student1 = Student('Kyryl', '20.04.2003')
    student1.add_properties('example1', 'example2', 'example3', 'example4')
    print(student1)
    student1 += 365
    print(student1)

    print('')

    student2 = Student('Anastasia', '28.11.2003', ['example1', 'example2'])
    print(student2)


if __name__ == '__main__':
    example()
