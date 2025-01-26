list_of_student = []
list_of_books = []
list_of_checkedout_books = []
dict_of_student = {}
requested_operation = "A"

def booting():
    if requested_operation == "E":
        string = ""
        for name in dict_of_student.keys():
            string = string + name + ":"
            for books in dict_of_student[name]:
                if books != dict_of_student[name][-1]:
                    string = string + books + ","
                else:
                    string = string + books
            string = string + "\n"
        dicti = open("books_copy.txt", "w")
        dicti.write(string)
        return dict_of_student

    dicti = open("books_copy.txt", "r")
    for line in dicti:
        line = line.strip().split(":")  # studentName:book1,book2
        student_name = line[0]
        books = line[1].split(",")
        dict_of_student[student_name] = books

    dicti = open("books_copy.txt","w")
    dicti.write("")
    dicti.close()

    return dict_of_student



def list_of_books_and_checkedout_books():
    books = open("books.txt", "r")

    for line in books:

        line = line.strip().split(",")
        book_name = line[1]
        if book_name not in list_of_books:
            list_of_books.append(book_name)

        if line[3] == "T" and line[3] not in list_of_checkedout_books:
            list_of_checkedout_books.append(book_name)

    books.close()

    bookList = ""
    checkedOutBookList = ""
    for book in list_of_books:
        bookList = bookList + book + "\n"
        if book in list_of_checkedout_books:
            checkedOutBookList = checkedOutBookList + book + "\n"

    if requested_operation == "L":  # accessing to the list of books
        return bookList

    else:
        return checkedOutBookList

def list_of_students():  # gives list
    students = open("students.txt", "r")

    for line in students:
        line = line.strip().split()
        students_name = line[1] + " " + line[2]
        list_of_student.append(students_name)

    students.close()
    return list_of_student

def update_dict_of_students(studentName, bookName):
    dict_of_student[studentName].append(bookName)

    return dict_of_student

def create_dict_of_students():
    students = open("students.txt", "r")

    for line in students:
        line = line.split()
        student_name = line[1] + " " + line[2]

        if student_name not in dict_of_student.keys():
            dict_of_student[student_name] = []

    output = ""
    books = ""
    for name in dict_of_student.keys():
        try:
            if dict_of_student[name][0]:
                for book in dict_of_student[name]:

                    if book != dict_of_student[name][0]:
                        books = books + "," + book

                    else:
                        books = book
                output = output + name + ":" + books + "\n"

            elif dict_of_student[name][0] == "":  # if exit is done at least one time
                output = output + name + "\n"

        except:
            output = output + name + "\n"

    return output

def update_the_books_text(checkedBook):
    books = open("books.txt", "r")
    books_copy = open("books_copy.txt", "a")
    for i in books:
        books_copy.write(i)

    books = open("books.txt", "w")
    books.write("")
    books = open("books.txt", "a")
    books_copy = open("books_copy.txt", "r")

    for line in books_copy:
        row = line.strip().split(",")

        if checkedBook == row[1]:
            books.write(row[0] + "," + row[1] + "," + row[2] + "," + "T" + "\n")

        else:
            books.write(line)

    books_copy = open("books_copy.txt", "w")
    books_copy.write("")
    books_copy.close()
    books.close()

    return books

def delete_book_from_library(deletedBook):
    books = open("books.txt", "r")

    for line in books:
        line = line.strip().split(",")
        if line[0] == deletedBook and line[3] == "T":
            print("You can't delete that book because it is already checked out by someone.")

            books.close()
            return

    books = open("books.txt", "r")
    books_copy = open("books_copy.txt", "a")
    for line in books:
        books_copy.write(line)

    books = open("books.txt", "w")
    books.write("")
    books_copy = open("books_copy.txt", "r")

    for line in books_copy:
        row = line.split(",")

        if deletedBook == row[0]:
            continue
        else:
            books = open("books.txt", "a")
            books.write(line)
            books.close()


    books_copy.close()
    books.close()
    return books

def search_for_book(keyOrISBN):
    books = open("books.txt", "r")
    book_list = []

    for line in books:
        line = line.strip().split(",")
        book_name = line[1]

        if line[0] == keyOrISBN or keyOrISBN in book_name:  # if the ISBN number is dialed and if the key word is dialed
            book_list.append(book_name)

    books.close()

    if book_list == []:
        return "The book doesn't exist in the library, try again."

    output = ""
    for book in book_list:

        if book == book_list[0]:
            output = book
        else:
            output = output + "\n" + book

    return output

def add_new_book(newBookISBN):
    books = open("books.txt", "a")

    book_name = input("Please enter the name of book: ")
    book_name = book_name.title()
    writers_name = input("Please enter the name of writer: ")
    writers_name = writers_name.title()

    new_line = ("\n" + newBookISBN + "," + book_name + "," + writers_name + "," + "F")
    books.write(new_line)

    books.close()
    return books

booting()

while True:

    requested_operation = input("What operation do you want to compute? \nE:to exit \nL:to access the list of books \nO:to access the list of checked out books \nS:to search for a book \nT:to access the list of students \nA:to add a new book to the library \nD:to delete a book from the library \nC:to check out a book \n:")
    requested_operation = requested_operation.upper()

    if requested_operation == "L":
        print(list_of_books_and_checkedout_books())

    elif requested_operation == "O":
        print(list_of_books_and_checkedout_books())

    elif requested_operation == "S":

        key_or_isbn = input("Enter the isbn number or key word of the book that you are trying to find:")
        key_or_isbn = key_or_isbn.title()
        print(search_for_book(key_or_isbn))

    elif requested_operation == "T":
        print(create_dict_of_students())

    elif requested_operation == "E":
        booting()
        break

    elif requested_operation == "A":
        ISBN = input("Please enter the book's ISBN number to add it to the library: ")
        add_new_book(ISBN)

    elif requested_operation == "D":
        not_wanted_book = input("Please type the ISBN number of the book that you want to delete from the library: ")
        delete_book_from_library(not_wanted_book)

    elif requested_operation == "C":
        student_name = input("To check out a book; first, you should register to the system. PLease enter the student's name: ")
        student_name_uppercase = student_name.title()

        if student_name_uppercase in list_of_students():
            wanted_book = input("Enter the name of the book that you want to check out:")
            wanted_book_uppercase = wanted_book.title()

            list_of_books_and_checkedout_books()
            if wanted_book_uppercase in list_of_books and wanted_book_uppercase not in list_of_checkedout_books:
                list_of_checkedout_books.append(wanted_book_uppercase)
                create_dict_of_students()
                update_dict_of_students(student_name_uppercase, wanted_book_uppercase)
                update_the_books_text(wanted_book_uppercase)

                print(student_name_uppercase + " have successfully checked out the book '" + wanted_book_uppercase + "'.")

            elif wanted_book_uppercase in list_of_books and wanted_book_uppercase in list_of_checkedout_books:
                print("You can't check out that book. It's already checked out to someone else.")

            else:
                print("The book that you have typed doesn't exist in the library, you can check the list of existing books.")

        else:
            print("There is no student id in the system with that name. Please check the name.")

    else:
        print("You must have pressed the wrong key,try again.")

