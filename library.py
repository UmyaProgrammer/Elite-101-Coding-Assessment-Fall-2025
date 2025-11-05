from books import Book
from datetime import date

class Library:
    def __init__(self, list_of_books: Book):
        self.list_of_books = list_of_books

    def list_of_available_books(self):
        for book in self.list_of_books:
            if book.get_availability():
                print(f"{book}\n")

    
    def get_list_of_books(self):
        for book in self.list_of_books:
            print(f"{book}\n")


    def search_by_author(self, author):
        matching_books = []
        for book in self.list_of_books():
            if book.get_author().lower() == author.lower():
                matching_books.append(book)

        return matching_books
    

    def search_by_author(self, author):
        matching_books = []
        for book in self.list_of_books:
            if book.get_author().lower() == author.lower():
                matching_books.append(book)

        return matching_books


    def search_by_genre(self, genre):
        matching_books = []
        for book in self.list_of_books:
            if book.get_genre().lower() == genre.lower():
                matching_books.append(book)

        return matching_books


    def get_unique_genres(self):
        unique_genres = []
        for book in self.list_of_books:
            if book.get_genre() not in unique_genres:
                unique_genres.append(book.get_genre())

        for genre in unique_genres:
            print(f"{genre}\n")


    def get_unique_authors(self):
        unique_authors = []
        for book in self.list_of_books:
            if book.get_author() not in unique_authors:
                unique_authors.append(book.get_author())

        for author in unique_authors:
            print(f"{author}\n")


    def checkout(self, id:str)->str:
        for book in self.list_of_books:
            if book.get_id() == id:
                return book.checkout()
            
        
    def return_book(self, id:str)->str:
        for book in self.list_of_books:
            if book.get_id() == id:
                return book.return_book()


    def overdue_books(self)->list[Book]:
        today = date.today()
        list_of_overdue_books = []


        for book in self.list_of_books:
            if book.get_due_date() != None:
                due_date = [int(date_part) for date_part in book.get_due_date().split("-")]
                book_due_date = date(due_date[0], due_date[1], due_date[2])
                if today > book_due_date:
                    list_of_overdue_books.append(book)

        
        return list_of_overdue_books


                




