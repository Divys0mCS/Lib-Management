# Store books, members, and issued books
books = []
members = []
borrowed_books = {}

# Add new book to the library
def AddBook():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    quantity = int(input("Enter number of copies: "))
    books.append([book_id, title, author, quantity])
    print("Book added successfully!")

# Register a new library member
def RegisterMember():
    member_id = input("Enter member ID: ")
    name = input("Enter member name: ")
    members.append([member_id, name])
    borrowed_books[member_id] = []
    print("Member registered successfully!")

# Issue a book to a member
def IssueBook():
    member_id = input("Enter member ID: ")
    book_id = input("Enter book ID: ")
    
    member_exists = False
    # Check if member exists
    for member in members:
        if member[0] == member_id:
            member_exists = True
            break
    
    if not member_exists:
        print("Member not found!")
        return

    # Find book and issue if available
    for book in books:
        if book[0] == book_id:
            if book[3] > 0:
                borrowed_books[member_id].append(book_id)
                book[3] -= 1
                print("Book issued successfully!")
                return
            else:
                print("Book is not available!")
                return
    
    print("Book not found!")

# Return a borrowed book
def ReturnBook():
    member_id = input("Enter member ID: ")
    book_id = input("Enter book ID: ")

    # Check if member exists
    if member_id not in borrowed_books:
        print("Member not found!")
        return

    # Remove returned book
    if book_id in borrowed_books[member_id]:
        borrowed_books[member_id].remove(book_id)
        for book in books:
            if book[0] == book_id:
                book[3] += 1
                print("Book returned successfully!")
                return
    else:
        print("This book was not borrowed by the member!")

# Check availability of a specific book
def CheckBookAvailability():
    book_id = input("Enter book ID to check availability: ")

    for book in books:
        if book[0] == book_id:
            print("Book Title: " + book[1])
            print("Author: " + book[2])
            print("Available Copies: " + str(book[3]))
            return
    print("Book not found!")

# Display all books
def DisplayBooks():
    print("\nBooks in the library:")
    for book in books:
        print("ID: " + book[0] + ", Title: " + book[1] + ", Author: " + book[2] + ", Available Copies: " + str(book[3]))

# Display all members
def DisplayMembers():
    print("\nLibrary members:")
    for member in members:
        print("ID: " + member[0] + ", Name: " + member[1])

# Main program loop (menu)
def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Check Book Availability")
        print("6. Display All Books")
        print("7. Display All Members")
        print("8. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            AddBook()
        elif choice == "2":
            RegisterMember()
        elif choice == "3":
            IssueBook()
        elif choice == "4":
            ReturnBook()
        elif choice == "5":
            CheckBookAvailability()
        elif choice == "6":
            DisplayBooks()
        elif choice == "7":
            DisplayMembers()
        elif choice == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# entry point
if __name__ == "__main__":
    main()
