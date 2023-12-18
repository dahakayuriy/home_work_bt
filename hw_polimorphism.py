#1
class Animal:
    def talk(self):
        pass 

class Dog(Animal):
    def talk(self):
        return "gav-gav"

class Cat(Animal):
    def talk(self):
        return "meow-meow"

def animal_talk(animal_instance):
    if isinstance(animal_instance, Animal):
        return animal_instance.talk()
    else:
        raise ValueError("Input must be an instance of Animal class or its subclass.")


dog_instance = Dog()
cat_instance = Cat()

print(animal_talk(dog_instance))  
print(animal_talk(cat_instance)) 
###########################################
#2
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library({self.name})"

    def __str__(self):
        return f"Library: {self.name}"


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        author.books.append(self)
        Book.total_books += 1

    def __repr__(self):
        return f"Book({self.name}, {self.year}, {self.author})"

    def __str__(self):
        return f"Book: {self.name}, {self.year}, Author: {self.author.name}"


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author({self.name}, {self.country}, {self.birthday})"

    def __str__(self):
        return f"Author: {self.name}, {self.country}, Birthday: {self.birthday}"

author1 = Author("John Doe", "USA", "1990-01-01")


library1 = Library("Public Library")

book1 = library1.new_book("The Book", 2022, author1)

books_by_author = library1.group_by_author(author1)

books_by_year = library1.group_by_year(2022)

print(books_by_author)
print(books_by_year)