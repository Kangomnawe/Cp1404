# """
# Replace the contents of this module docstring with your own details
# Name: kin
# Date started: 17th August 2018
#
# """
#
# """CP1404-Assignment-1"""
# import csv
#
#
# def main():
#     menu = "Menu:\nL - List all books\nA - Add new book\nM - Mark a book as complete\nQ - quit"
#     books = []
#     in_file = open("books.csv", "r")
#     book_loader = csv.reader(in_file)
#     for book in book_loader:
#         books.append(book)
#     in_file.close()
#     # welcome massage
#     print("Welcome to Reading Tracker 0.1 - by James Yalo")
#     # print("{} books loaded from {}".format(len(book_title, books)))
#     print(menu)
#     selection = input(">>>").upper()
#     while selection != "Q":
#         if selection == "L":
#             list_books(books)
#         #   marking books from the list
#         elif selection == "M":
#             unread = 0
#             for book in books:
#                 if book[3] == 'r':
#                     unread += 1
#             if unread == 0:
#                 print("No required books")
#             else:
#
#                 list_books(books)
#                 print("Enter the number of a book to mark as completed")
#                 book_handle = 1
#                 finish_read = False
#                 while not finish_read:
#                     try:
#                         number_books = int(input(">>> "))
#                         if number_books <= 0:
#                             print("Number must be > 0")
#                         elif number_books > len(books):
#                             print("Invalid book number")
#                         else:
#                             finish_read = True
#                     except ValueError:  # or just  except:
#                         print("Invalid input; enter a valid number")
#                 #   check books as marked
#                 book_check = books[number_books - book_handle]
#                 book_selected = books[number_books - book_handle]
#                 book_title = book_selected[0]
#                 book_author = book_selected[1]
#                 mark_completed = 'c'
#                 if book_check[3] != 'c':
#                     book_check[3] = mark_completed
#                     print("{} by {} completed".format(book_title, book_author))
#                 elif book_check[3] == "c":
#                     print("That book is already completed.")
#                     print("{} by {} Marked as completed.".format(book_title, book_author))
#                     print("No book left to read. why not add new book")
#         # adding books here
#         elif selection == "A":
#             adding_book(books)
#
#
#         else:
#             print("Invalid menu choice")
#         print(menu)
#         selection = input(">>>").upper()
#     else:
#         with open("books.csv", "w") as out_file:  # Another way of opening files when we
#             # exit the this block the file is automatically saved and closed.
#             for book in books:
#                 entry = book[0] + ',' + book[1] + ',' + book[2] + ',' + book[
#                     3] + '\n'  # Making the CSV line in plain txt
#                 out_file.write(entry)  # Writing it to the file.
#         print("Have a nice day :)")
#
#         # going through list print out available books in the list
#
#
# def adding_book(books):
#     book_title = input("Title:")
#     while book_title == "":
#         print("Input can not be blank")
#         book_title = input("Title:")
#     book_author = input("Author:")
#     while book_author == "":
#         print("Input can not be blank")
#         book_author = input("Author:")
#         if book_pages == "":
#             print("Input can not be blank")
#         book_pages = input("Pages:")
#         print("Just one")
#     finish_read = False
#     while not finish_read:
#         try:
#             book_pages = int(input("Pages:"))
#             while book_pages == "":
#                 print("Input can not be blank")
#                 book_pages = int(input(book_pages))
#             finish_read = True
#         except ValueError:
#             print("Invalid input Enter are Correct name")
#     print("{} {} {}  is available for adding".format(book_title, book_author, book_pages))
#     books.append([str(book_title), str(book_author), str(book_pages),
#                   'r'])  # Inserting a new tuple contains the data on new book.
#
#
# def list_books(books):
#     number_pages = 0
#     number_of_books = 0
#     for i in range(len(books)):
#         book_title = (books[i][0])
#         book_author = (books[i][1])
#         book_pages = int(books[i][2])
#         book_status = (books[i][3])
#         if book_status == "c":
#             print(" {}. {:40} by {:20} {:3} pages".format(i + 1, book_title, book_author, book_pages))
#         else:
#             print("*{}. {:40} by {:20} {:3} pages".format(i + 1, book_title, book_author, book_pages))
#             number_pages += book_pages
#             number_of_books += 1
#     print("{} books".format(len(books)))
#     if number_of_books:  # This is same as saying 'if number_of_books != 0:'
#         # since in python 0 is same as false.
#         print("You need to read {} pages in {} books".format(number_pages, number_of_books))
#     else:
#         print(
#             "No books left to read. Why not add a new book?")  # If books to read are 0 we print this message instead.
#
#
# main()