from books import Book
from library import Library
from library_books import library_books



#List of variables and lists
list_of_books = []


for book in library_books:
    new_book = Book(id=book["id"], title=book["title"], author=book["author"], genre=book["genre"], available=book["available"], due_date=book["due_date"], checkouts=book["checkouts"])
    list_of_books.append(new_book)

library = Library(list_of_books=list_of_books)



# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def get_available_books():
    library.list_of_available_books()



# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search_for_books()->list[Book]:
    print("Please enter the method of searching you want:\n\tGenre\n\tAuthor")
    user_method = input(": ")
    while user_method != "Genre" and user_method != "Author":
        user_method = input("Please enter a valid search method: ")


    if user_method == "Genre":
        library.get_unique_genres()
        user_genre = input("Genre: ")
        return library.search_by_genre(genre=user_genre)
    elif user_method == "Author":
        library.get_unique_authors()
        user_author = input("Author: ")
        return library.search_by_author(author=user_author)
    


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
def checkout_book():
    library.get_list_of_books()
    print("Please select the book you would like to using its ID.")

    book_id = input("ID: ")
    print(library.checkout(id=book_id))



# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
def return_book():
    library.get_list_of_books()
    print("Please select the book you would like to return using its ID.")

    book_id = input("ID: ")
    print(library.return_book(id=book_id))



# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def get_overdue_books():
    overdue_books = library.overdue_books()
    for book in overdue_books:
        print(book)



# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    get_overdue_books()
