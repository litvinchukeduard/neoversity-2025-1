from dataclasses import dataclass
from collections import UserList
'''
Потрібно написати систему, яка буде керувати бібліотекою
'''

# Назва книги, Автор, Кількість сторінок

my_dict ={
    "title": "Lord of the Rings",
    "author": "J.R.R Tolkien",
    "number_of_pages": 400
}


class Human:
    def __init__(self, name: str):
        self.name = name


# @dataclass(frozen=True)
@dataclass
class Person(Human):
    first_name: str
    last_name: str
    age: int = 18

    def __post_init__(self):
        super().__init__(self.first_name + " " + self.last_name)
        self.__check_date__()
        if self.age <= 0:
            raise ValueError('Can not create a person with age less than zero')
        
    def __check_date__(self):
        ...

    # def __init__(self)


# boilerplate code
class Book:
    def __init__(self, title: str, author: str, number_of_pages: int):
        self.title = title
        self.author = author
        if number_of_pages <= 0:
            raise ValueError("Number of pages should be greater than 0")
        self.number_of_pages = number_of_pages
        self.days_to_loan = None

    # def __init__(self, args: dict):
        # {name,surname,age}=self.args
        # self.title, self.author, self.number_of_pages = args
        # self.title = args['title']
        # self.author = author
        # self.number_of_pages = number_of_pages
        # self.days_to_loan = 


class Library(UserList):
    def append(self, element: Book):
        # if not isinstance(element, Book):
        #     raise ValueError
        self.data.append(element)


# my_dict = {'name': 'John', 'surname': 'Smith'}
# name, surname = **my_dict

# my_book = Book("Lord of the Rings", "J.R.R Tolkien", -10)
# my_book_two = Book("Lord of the Rings", "J.R.R Tolkien", 400)

# print(dir(my_book))

# print(my_book)
# print(my_book_two)

# print(my_book == my_book_two)

# my_book_list = [Book("Lord of the Rings", "J.R.R Tolkien", 400), Book("Lord of the Rings", "J.R.R Tolkien", 400)]
# # ==

# searched_book = None
# for book in my_book_list:
#     if book.title == "Lord of the Rings" and book.author == "J.R.R Tolkien":
#         searched_book = book
#         break

# print(searched_book)

# my_book_list.remove(searched_book)

# print(my_book_list)
# str_list = ["hello", "world"]

# str_list.remove("hello")

# print(str_list)

# str, int

# print(name, surname)

# person = Person("John", "Smith", 18)
# person.last_name = "Jake"
# print(dir(person))

lib = Library()
lib.append(Book("Lord of the Rings", "J.R.R Tolkien", 400))
lib.append(1)
lib.append("hello")
print(lib[1:2])

my_list = [1, 2, 3]
my_list[1]
my_list.append(1)
my_list[1:2]
