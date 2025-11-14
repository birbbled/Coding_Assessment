from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def view_books():
    for book in library_books:
        print(book)

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search_books(search_by, keyword):
    match = []
    for book in library_books:
        if book[search_by].lower() == keyword.lower(): #basic searching in dictionaries. Using .lower() so it's case insensitive
            match.append(book) #adding to a list

    return match

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

def check_out(id):
    for book in library_books:
        if book.get('id') == id:
            if book['available']: #simple of way of checking if true
                book['available'] = False
                book['due_date'] = datetime.now() + timedelta(weeks=2) #looked up on stackoverflow on what implementation looks like
                book['checkouts'] += 1
                print(f"You checked out {book['title']}") #fstring to print
            else:
                print("This book is already checked out.")



# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

def return_book(id):
    for book in library_books:
        if book['id'] == id:
            book['available'] = True
            book['due_date'] = ''

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def overdue_books():
    overdue = []
    for book in library_books:
        if book['due_date'] and book['due_date'] < datetime.today() and not book['availability']: #checking if there is a due date
            overdue.append(book)

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

class Book: #class
    def __init__(self, id, title, author, genre, available, due_date, checkouts):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts

#view using classes
    def view(self):
        print(f"id = {self.id}, title = {self.title}, author = {self.author}, genre = {self.genre}, available = {self.available}, due date = {self.due_date}, checkouts = {self.checkouts}")

#checkout function using classes
    def check_out(self):
        if self.available:
            self.available = False
            self.due_date = datetime.now() + timedelta(weeks=2)
            self.checkouts +=1
            print(f"You checked out {self.title}!")
        else:
            print("This book is already checked out!")

#return books using classes
    def return_book(self):
        self.available = True
        self.due_date = ''
        print("success!!")

#overdue using classes
    def overdue(self):
        if self.due_date and not self.available and self.due_date < datetime.today():
            return True
        return False #if it isn't true, then return false

#making dictionary into a list of Book
library = []

for data in library_books:
    if isinstance(data["due_date"], str):
        data["due_date"] = datetime.strptime(data["due_date"], "%Y-%m-%d") #looked up implementation on how to convert string to datetime https://stackoverflow.com/questions/466345/convert-string-jun-1-2005-133pm-into-datetime
    library.append(Book(**data)) #identifies dictionary format

def search(search_by, keyword):
    sorted_books = []
    for book in library:
        if search_by == 'author' and book.author.lower() == keyword.lower(): #easiest implementation to check both
                sorted_books.append(book)
        elif search_by == 'genre' and book.genre.lower() == keyword.lower():
                sorted_books.append(book)

    return sorted_books

def overdue_books():
    overdue_books = []
    for book in library:
        if book.overdue():
            overdue_books.append(book)

    return overdue_books


# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

#Menu. Everything will use classes version

if __name__ == "__main__":
    run = True
    while run:
        print("Menu:")
        print("1. View books in library")
        print("2. Search")
        print("3. Check out book")
        print("4. Return book")
        print("5. Overdue books")
        print("6. Stop")

        choice = int(input("What option do you want to choose today?"))

    #viewing all the books
        if choice == 1:
            for book in library:
                book.view()

       #sort by genre/author. needs user input. .lower() to make not case sensitive
        elif choice == 2:
            search_by = input("Would you like to sort by author or genre?")
            keyword = input("Enter the specific author/genre")
            for book in search(search_by.lower(), keyword.lower()):
                book.view() #this is only way to view books because printing doesn't do what we want

      #check out a book
        elif choice == 3:
            id = input("Enter the id of the book you'd like to check out?")
            for book in library:
                if book.id == id:
                    book.check_out()

        #return a book
        elif choice == 4:
            id = input("Enter the id of the book you'd like to return")
            for book in library:
                if book.id == id:
                    book.return_book()

        #view overdue books
        elif choice == 5:
            for book in overdue_books():
                book.view()

        elif choice == 6:
            run = False #end the while loop.


    # view_books()
    # print(search_books('author', 'Rick Riordan'))
    # print(search_books('genre', 'Science Fiction'))
    # check_out('B2')
    pass