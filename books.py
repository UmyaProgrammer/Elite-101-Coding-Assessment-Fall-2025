from datetime import datetime, timedelta, date
class Book:
    def __init__(self, id, title, author, genre, available, due_date, checkouts):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts

    def get_id(self):
        """
        :return: ID of the book
        """
        return self.id

    def get_title(self):
        """
        :return: Title of the book
        """
        return self.title

    def get_author(self):
        """
        :return: Author of the book
        """
        return self.author

    def get_genre(self):
        """
        :return: Genre of the book
        """
        return self.genre

    def get_availability(self):
        """
        :return: Availability of the book
        """
        return self.available

    def get_due_date(self):
        """
        :return: Due date of the book
        """
        return self.due_date

    def get_check_outs(self):
        """
        :return: Returns the number of times the book was checked out
        """
        return self.checkouts

    def checkout(self) -> str:
        """
        If the book is not checked out, this function checks it out and creates a deadline to two weeks on the day the book is checked out.
        :return: Returns a message based on whether the function was successful at checking out the book
        """
        if self.available:
            self.available = False
            self.due_date = str(date.today() + timedelta(days=14))
            self.checkouts += 1
            return f"The book {self.title} has been checkedout until:\n\t{self.due_date}"
        else:
            return f"The book {self.title} has already been checkedout"

    def return_book(self):
        """
        If the book is not already returned, this function will return the book, set its due date to None, and add 1 to the number of times it was checkedout
        :return: A message based on whether if the book is returned or not
        """
        if self.available == False:
            self.available = True
            self.due_date = None
            return f"The book {self.title} has been returned on:\n\t{date.today()}"
        else:
            return f"The book {self.title} has already been available."

    def __str__(self):
        return f"{self.id} - {self.title}\n\t{self.author}\n\tGenre: {self.genre}\n\tAvailability: {self.available}\n\tDue Date: {self.due_date}\n\tCheckouts: {self.checkouts}"


if __name__ == "__main__":
    book = new_book = Book(id="B1", title="The Lightning Thief", author="Rick Riordan", genre="Fantasy", available=True,
                           due_date=None, checkouts=2)
