# Library Management System (Python – Terminal Based)

This project is a simple terminal-based Library Management System written in Python. It was developed as my Class 12 Computer Science board project to practice and demonstrate fundamental Python concepts, including lists, dictionaries, procedural programming, and basic data handling without using external libraries or databases.

The objective of this project was to validate my understanding of Python basics and apply them in a real program that performs meaningful operations with user interaction.

# Features

The system supports the following operations:

1. Add books to the library

2. Register new members

3. Issue books to members

4. Return issued books

5. Check availability of a specific book

6. Display all books

7. Display all registered members

All records are stored in runtime using Python lists and dictionaries.

# Technologies Used

✔ Python (Core)

✔ Lists, Dictionaries

✔ Procedural Programming

✔ Basic input/output

✔ Loop and conditional statements

No external libraries or databases are used.

# How the Logic Works

✔ Books and members are stored in Python lists.

✔ Borrowed books are tracked using a dictionary that maps member IDs to a list of issued book IDs.

✔ Issuing a book reduces quantity.

✔ Returning a book increases quantity.

All functionality is driven through a simple menu loop in the console.

# How to Run

1. Make sure Python is installed on your system.

2. Download or clone this repository.

3. Open a terminal/command prompt inside the project folder.

4. Run the script using:

```bash
$ python library_management.py
```

# Project Purpose

This project was created as part of my Class 12 Computer Science board assignment. The goal was to implement a small working application using only Python fundamentals and to ensure that my basics (such as functions, control flow, lists, and dictionaries) were thoroughly understood and applied.

# Sample Output

```bash
$ python library_management.py

Library Management System
1. Add Book
2. Register Member
3. Issue Book
4. Return Book
5. Check Book Availability
6. Display All Books
7. Display All Members
8. Exit
Enter your choice: 1
Enter book ID: B101
Enter book title: Python Basics
Enter author name: John Doe
Enter number of copies: 3
Book added successfully!

Library Management System
1. Add Book
2. Register Member
3. Issue Book
4. Return Book
5. Check Book Availability
6. Display All Books
7. Display All Members
8. Exit
Enter your choice: 2
Enter member ID: M001
Enter member name: Alex
Member registered successfully!

Library Management System
1. Add Book
2. Register Member
3. Issue Book
4. Return Book
5. Check Book Availability
6. Display All Books
7. Display All Members
8. Exit
Enter your choice: 3
Enter member ID: M001
Enter book ID: B101
Book issued successfully!

Library Management System
1. Add Book
2. Register Member
3. Issue Book
4. Return Book
5. Check Book Availability
6. Display All Books
7. Display All Members
8. Exit
Enter your choice: 6

Books in the library:
ID: B101, Title: Python Basics, Author: John Doe, Available Copies: 2

Library Management System
1. Add Book
2. Register Member
3. Issue Book
4. Return Book
5. Check Book Availability
6. Display All Books
7. Display All Members
8. Exit
Enter your choice: 8
Exiting the program.
```

# Future Improvements

Possible enhancements include:

   ✔ Adding file/database storage

   ✔ Adding a GUI (Tkinter)

   ✔ Preventing duplicate entries

   ✔ Searching by title or author

# Author

Developed by Divy Srivastava (Class 12 Computer Science Project)
