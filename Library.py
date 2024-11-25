# library.py
# Programmer: Cole Watson
# Class: CSCI1301-D4, Fall 2024
# Program purpose: A program to manage a library's book catalog and checkout process for patrons.

# ================================================================
class Book:
    def __init__(self):
        # Initialize book attributes
        self.ID = ""
        self.title = ""
        self.author = ""
        self.checked_out_by = None  # Name of the person who checked out the book
        self.return_date = ""  # Expected return date as a simple string

    def __str__(self):
        # Return book information, including status if checked out
        if self.checked_out_by:
            status = f'Checked out by {self.checked_out_by}, due on {self.return_date}'
        else:
            status = "Available"
        return f'{self.ID}: "{self.title}" by {self.author} - {status}'

    def accept_book_info(self):
        # Prompt user to input book details
        self.ID = input("Enter Book ID: ")
        self.title = input("Enter Book Title: ")
        self.author = input("Enter Author: ")

# ================================================================
class Library:
    def __init__(self):
        # Initialize library catalog as an empty list
        self.catalog = []

    def add_book(self, book):
        # Add a new book to the library catalog
        self.catalog.append(book)

    def display_books(self):
        # Display all books in the catalog
        if not self.catalog:
            print("\nThe library catalog is empty!")
        else:
            print("\nLibrary Catalog:")
            for book in self.catalog:
                print(book)

    def checkout_book(self, book_ID, patron_name, return_date):
        # Checkout a book to a patron by ID
        found = False
        for book in self.catalog:
            if book.ID == book_ID:
                found = True
                # Check if the book is already checked out
                if book.checked_out_by:
                    print(f"\nBook '{book.title}' is already checked out by {book.checked_out_by}.")
                else:
                    # Set the patron and return date for the checked-out book
                    book.checked_out_by = patron_name
                    book.return_date = return_date
                    print(f"\nBook '{book.title}' has been checked out by {patron_name}, due on {return_date}.")
                return
        if not found:
            print(f"\nBook with ID {book_ID} not found.")

    def return_book(self, book_ID):
        # Return a book by ID, marking it as available
        found = False
        for book in self.catalog:
            if book.ID == book_ID:
                found = True
                if book.checked_out_by:
                    # Clear the checkout information
                    print(f"\nBook '{book.title}' returned by {book.checked_out_by}.")
                    book.checked_out_by = None
                    book.return_date = ""
                else:
                    print(f"\nBook '{book.title}' is already available.")
                return
        if not found:
            print(f"\nBook with ID {book_ID} not found.")

# ================================================================
def menu():
    # Display menu options and get user's choice
    print("\nSelect a choice:")
    print("a. Add Book")
    print("d. Display Books")
    print("c. Checkout Book")
    print("r. Return Book")
    print("e. Exit")
    choice = input("Choose an option: ")
    return choice.lower()

# ================================================================
if __name__ == '__main__':
    # Create a library instance to manage books
    library = Library()

    # Display menu and process user choices
    choice = menu()

    while choice != "e":
        if choice == "a":  # Add a new book to the catalog
            book = Book()
            book.accept_book_info()
            library.add_book(book)
        elif choice == "d":  # Display all books in the catalog
            library.display_books()
        elif choice == "c":  # Checkout a book
            book_ID = input("Enter the ID of the book to check out: ")
            patron_name = input("Enter your name: ")
            return_date = input("Enter the return date (e.g., YYYY-MM-DD): ")
            library.checkout_book(book_ID, patron_name, return_date)
        elif choice == "r":  # Return a book by ID
            book_ID = input("Enter the ID of the book to return: ")
            library.return_book(book_ID)
        else:
            print("\nInvalid option. Please try again.")
        
        # Display menu again for the next operation
        choice = menu()

    # End the program
    print("Have a Great Day!")
