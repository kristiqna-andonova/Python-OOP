from typing import List
from books import Book


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def registrate_book(self, book: Book):
        if book not in self.books:
            self.books.append(book)

    def find_book(self, title: str):
        for book in self.books:
            if book.title == title:
                return book.get_info()


