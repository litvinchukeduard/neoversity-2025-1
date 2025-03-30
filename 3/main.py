'''
Потрібно написати систему, яка буде керувати бібліотекою
'''

# Назва книги, Автор, Кількість сторінок

my_dict ={
    "title": "Lord of the Rings",
    "author": "J.R.R Tolkien",
    "number_of_pages": 400
}

# boilerplate code
class Book:
    def __init__(self, title: str, author: str, number_of_pages: int):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.days_to_loan = None

    # def __init__(self, args: dict):
        # {name,surname,age}=self.args
        # self.title, self.author, self.number_of_pages = args
        # self.title = args['title']
        # self.author = author
        # self.number_of_pages = number_of_pages
        # self.days_to_loan = 
        
# my_dict = {'name': 'John', 'surname': 'Smith'}
# name, surname = **my_dict

my_book = Book("Lord of the Rings", "J.R.R Tolkien", 400)
my_book_two = Book("Lord of the Rings", "J.R.R Tolkien", 400)

print(dir(my_book))

# print(my_book)
# print(my_book_two)

# print(my_book == my_book_two)

my_book_list = [Book("Lord of the Rings", "J.R.R Tolkien", 400), Book("Lord of the Rings", "J.R.R Tolkien", 400)]
# ==

searched_book = None
for book in my_book_list:
    if book.title == "Lord of the Rings" and book.author == "J.R.R Tolkien":
        searched_book = book
        break

print(searched_book)

my_book_list.remove(searched_book)

print(my_book_list)
# str_list = ["hello", "world"]

# str_list.remove("hello")

# print(str_list)

# str, int

# print(name, surname)