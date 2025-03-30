from dataclasses import dataclass
'''
Написати клас Person, в якого будуть імʼя, прізвище та рік народження.

Але обмежити рік народження лише минулими роками
'''

class Person:
    def __init__(self, name, surname, year):
        self.name = name
        self.surname = surname
        self.__year = None
        self.year = year # to be done

    @property
    def year(self):
        return f'{self.__year}'
    
    @year.setter
    def year(self, new_value: int):
        if new_value > 2025:
            raise ValueError('Year can not be greater than 2025')
        self.__year = new_value

# @dataclass
# class Person:
#     name: str
#     surname: str
#     year: int


# Person('John', 'Smith', 2027) # невірно

person = Person("Jake", "Smith", 2000)

print(type(person.year))
person.year = 2028 # невірно