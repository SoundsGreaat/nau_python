from postgres import init, close


def get_student_count():
    while True:
        student_count = input('Введіть кількість студентів:')
        if student_count.isdigit():
            student_count = int(student_count)
            if student_count <= 0:
                print('Повинен бути хочаб один студент')
            else:
                return student_count


def get_student_properties():
    while True:
        ...


def get_student_properties():
    pass


def main():
    # conn, cursor = init()
    # close(conn, cursor)
    student_count = get_student_count()
    students_dict = {}
    for i in range(student_count):
        student_name = input('Введіть ім\'я студента ' + str(i + 1) + ':')
        student_dob = input('Введіть дату народження студента ' + str(i + 1) + ':')
        students_dict[student_name] = student_dob
        return students_dict


if __name__ == '__main__':
    main()
