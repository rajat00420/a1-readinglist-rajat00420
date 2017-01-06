__author__ = 'jc441938'

# Initialize the constants

FILE = "books.csv"


def main():
    print("Reading List 1.0 - by RAJAT KHAJURIA")
    book_list = []
    load_books(book_list)
    print(book_list)
    display_menu()
    choice = input(">>>")
    while choice.lower() != 'q':
        if choice.lower() == 'r':
            required_books(book_list)
        elif choice.lower() == 'c':
            completed_books(book_list)
        elif choice.lower() == 'a':
            book_list = add_books()
        elif choice.lower() == 'm':
            complete_a_book(book_list)

        display_menu()


        choice = input(">>>")
    print("{} books are now saved to {}".format(len(book_list), FILE))
    print("HAVE A GREAT DAY ;)")


def display_menu():
    """
     function  used to display the options Menu
"""
    menu = "Menu: \nR - List required books\nC - List completed books\nA - Add new book\nM - Mark a book as " \
           "completed\nQ - Quit"
    print(menu)


#  display_menu function ended

def load_books(book_list):
    """
     function  used to load the books from file to list
"""
    book_file = open(FILE, 'r')
    for line in book_file:
        book_list.append(line.strip().split(','))
    book_file.close()


#  load_books() ended

def complete_a_book(book_list):
    """
  function  used to mark a book as completed in the file
"""
    required_books(book_list)
    print("Enter the number of a book to be marked as completed")
    try:
        num_of_book = int(input(">>>"))
        if book_list[num_of_book][3] == 'c':
            print("That book is already been completed")
        else:
            book_list[num_of_book][3] = 'c'
            books_file = open(FILE, 'w')
            for i in book_list:
                for j in i:
                    if j == "r" or j == "c":
                        print(j, end='', file=books_file)
                    else:
                        print(j, end=',', file=books_file)
                print(file=books_file)
            books_file.close()
            print("{} by {} is completed".format(book_list[num_of_book][0], book_list[num_of_book][1]))
    except ValueError:
        print("Invalid input; enter a valid number")
        complete_a_book(book_list)


# end of complete_a_book()

def required_books(book_list):
    """
     function displays the list of books which need to be read
"""
    total_pages = 0
    print("Required Books:")
    count = 0
    for i in book_list:
        if 'r' in book_list[count][3]:
            print("{}. {:<50s} by {:<20s} {:>15s} pages".format(count, book_list[count][0], book_list[count][1],
                                                                book_list[count][2]))
            total_pages += int(book_list[count][2])
        count += 1
    if count != 0:
        print("Total pages for {} books: {}".format(count - 1, total_pages))
    else:
        print("No books")


# end of required_books function

def completed_books(book_list):
    """
     function is used to print all the completed books
"""
    total_pages = 0
    print("Books Required:")
    count = 0
    for i in book_list:
        if 'c' in book_list[count][3]:
            print("{}. {:<50s} by {:<20s} {:>15s} pages".format(count, book_list[count][0], book_list[count][1],
                                                                book_list[count][2]))
            total_pages += int(book_list[count][2])
            count += 1
    print("Total pages for {} books: {}".format(count + 1, total_pages))


# end of completed_books function

def add_books():
    """
     function will help us to add books to the file books.csv
"""
    title = input("Title:")
    while title == "":
        print("Input cannot be blank")
        title = input("Title:")
    author = input("Author:")
    while author == "":
        print("Input cannot be blank")
        author = input("Author:")
    flag = 0
    pages = 0
    while flag == 0:
        try:
            pages = int(input("Pages: "))
            while pages <= 0:
                print("Number must be >= 0")
                pages = int(input("Pages: "))
            flag = 1
        except ValueError:
            print("Not a valid input; enter a valid number")
    print("{} by {}, ({} pages) added to reading list".format(title, author, pages))
    book = [title, author, str(pages), 'r']
    book_list = []
    load_books(book_list)
    book_list.append(book)
    print(book_list)
    books_file = open(FILE, 'w')
    for i in book_list:
        for j in i:
            if j == "r" or j == "c":
                print(j, end='', file=books_file)
            else:
                print(j, end=',', file=books_file)
        print(file=books_file)
    books_file.close()
    return book_list


# end of add_books function

def save_books(books):
    """
     function will help the program to update data into file books.csv
"""


# end of save_books function
main()
