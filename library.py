from books import Book
from datetime import date

"""
A class that acts like the foundation of the system by having a list of all the books using the book class to easily checkout, and return books. 
It also allows the user to search books up based on author and genre. 
Overall helps the code become more clear and creates a central hub that allows multiple functions to be used with a library object.
"""
class Library:
    def __init__(self, list_of_books: Book):
        self.list_of_books = list_of_books

    def list_of_available_books(self):
        """
        Prints out all the available books.
        :return: None
        """
        for book in self.list_of_books:
            if book.get_availability():
                print(f"{book}\n")

    def get_list_of_books(self):
        """
        Prints out all the books.
        :return: None
        """
        for book in self.list_of_books:
            print(f"{book}\n")

    def search_by_author(self, author):
        """
        The function will go through the list of books and put every book of the given author parameter in a list and then return it.
        :param author: The function will look for books from this author
        :return: A list of all the books written by the author
        """
        matching_books = []
        for book in self.list_of_books():
            if book.get_author().lower() == author.lower():
                matching_books.append(book)

        return matching_books


    def search_by_genre(self, genre):
        """
        The function will go through the list of books and put every book of the given genre parameter in a list and then return it.
        :param genre: The function will look for books from this genre
        :return: A list of all the books written by the genre
        """
        matching_books = []
        for book in self.list_of_books:
            if book.get_genre().lower() == genre.lower():
                matching_books.append(book)

        return matching_books

    def get_unique_genres(self):
        """
        Prints out a list of all the genres in the library.
        """
        unique_genres = []
        for book in self.list_of_books:
            if book.get_genre() not in unique_genres:
                unique_genres.append(book.get_genre())

        for genre in unique_genres:
            print(f"{genre}\n")

    def get_unique_authors(self):
        """
        Prints out a list of all the authors in the library.
        """
        unique_authors = []
        for book in self.list_of_books:
            if book.get_author() not in unique_authors:
                unique_authors.append(book.get_author())

        for author in unique_authors:
            print(f"{author}\n")

    def checkout(self, id: str) -> str:
        """
        Checkouts the book based on the given ID
        :param id: ID to identify the book the user wants to check out
        :return: returns whether the library could successfully checked out the book, and if not the reason.
        """
        for book in self.list_of_books:
            if book.get_id() == id:
                return book.checkout()

    def return_book(self, id: str) -> str:
        """
        Returns the book based on the given ID
        :param id: ID to identify the book the user wants to return
        :return: returns whether the library could successfully return the book, and if not the reason.
        """
        for book in self.list_of_books:
            if book.get_id() == id:
                return book.return_book()

    def overdue_books(self) -> list[Book]:
        """
        Looks for all the overdue books based on the current date.
        :return: A list of book objects of all the overdue books.
        """
        today = date.today()
        list_of_overdue_books = []

        for book in self.list_of_books:
            if book.get_due_date() != None:
                due_date = [int(date_part) for date_part in book.get_due_date().split("-")]
                book_due_date = date(due_date[0], due_date[1], due_date[2])
                if today > book_due_date:
                    list_of_overdue_books.append(book)

        return list_of_overdue_books







