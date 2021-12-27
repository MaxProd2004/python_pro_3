import datetime

class Person:
    """Class, which describe people"""
    def __init__(self, name: str, surname: str, date_of_birth: str):
        """Initialization instance's attributes"""
        if not isinstance(name, str) or not isinstance(surname, str):
            raise TypeError("Errors with data type")
        if not name or not surname:
            raise ValueError("Name and Surname must contain at least one character")
        if not name.istitle() or not surname.istitle():
            raise ValueError("Name and Surname must be in title notation")


        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth

    def __str__(self):
        age = datetime.datetime.now().year - datetime.date(*map(int, self.date_of_birth.split('/'))).year
        return f'{self.surname} {self.name}, {age} years'

if __name__ == "__main__":
    try:
        x = Person('Ivan', 'Ivanov', '2000/12/12')
        print(x)
    except Exception as error:
        print(error)