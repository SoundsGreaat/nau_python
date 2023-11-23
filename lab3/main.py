import postgres


def get_student_count():
    while True:
        student_count = input('Введіть кількість студентів: ')
        if student_count.isdigit():
            student_count = int(student_count)
            if student_count <= 0:
                print('Повинен бути хочаб один студент')
            else:
                return student_count


def get_student_properties(student):
    properties = input(f'Введіть властивості студента {student} через кому: ')
    if properties == '':
        return None
    properties = properties.split(',')
    properties_clean = [prop.strip() for prop in properties if prop.strip()]
    return properties_clean


def get_students_data(student_count):
    students_data = []
    for i in range(student_count):
        student_name = input(f'Введіть ім\'я студента {i + 1}: ')
        dob = input(f'Введіть дату народження студента {student_name}: ')
        properties = get_student_properties(student_name)
        students_data.append((student_name, dob, properties))
    return students_data


def main():
    conn, cursor = postgres.init()
    postgres.create_tables(conn, cursor)

    students_data = get_students_data(get_student_count())
    for student_name, dob, properties in students_data:
        student_id = postgres.add_student(conn, cursor, student_name, dob)
        if properties:
            postgres.add_properties(conn, cursor, student_id, properties, student_name)
    conn.commit()
    postgres.close(conn, cursor)


if __name__ == '__main__':
    main()
