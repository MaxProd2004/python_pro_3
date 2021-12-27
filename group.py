from student import Student
MAX_STUDENTS = 3

class MaxStudentsError(Exception):
    def __init__(self, MAX_NUMBER, message):
        self.MAX_NUMBER = MAX_NUMBER
        self.message = message

    def __str__(self):
        return f'{self.message}, max = {self.MAX_NUMBER}'

class Group:
    def __init__(self, speciality, entrance_year, students = None):
        self.speciaity = speciality
        self.entrance_year = entrance_year
        self.__students = []
        for item in students:
            self.add_student(item)

    def add_student(self, student: Student):
        if len(self.__students) == MAX_STUDENTS:
            raise MaxStudentsError(MAX_STUDENTS, 'A lot of students in the group')
        for item in self.__students:
            if (item.surname, item.name, item.date_of_birth) == (student.surname, student.name, student.date_of_birth):
                return None
        self.__students.append(student)

    def __str__(self):
        res = '\n'.join(map(str, self.__students))
        return f'{self.speciaity}: {self.entrance_year}\nStudents:\n{res}'



if __name__ == '__main__':
    x_1 = Student('Ivan', 'Ivanov', '2020/12/12', 'M')
    x_2 = Student('Ivan2', 'Ivanov2', '2020/12/12', 'M')
    x_3 = Student('Ivan3', 'Ivanov3', '2020/12/12', 'M')
    x_4 = Student('Ivan4', 'Ivanov4', '2020/12/12', 'M')

    try:
        group = Group('CS', '2021', [x_1, x_2, x_3, x_4])
        print(group)
    except Exception as error:
        print(error)
