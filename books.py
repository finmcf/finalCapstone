# import sqlite 3

import sqlite3

#import tabulate

from tabulate import tabulate

# initialize database


database = sqlite3.connect("ebookstore")

# initialize cursor

cursor = database.cursor()

# search for table books

does_table_exist = cursor.execute(
    "SELECT name FROM sqlite_master WHERE name='books'")

# check if table exists
if does_table_exist.fetchone() is None:

    # if table does not exist create table books

    cursor.execute(
        "CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, quantity INTEGER)")

# infinite while loop
while True:

    # prompt user for choice

    choice = input('''Please select one of the following options:
    e - Enter book
    u - Update book
    d - Delete book
    s - Search book
    x - exit  ''').lower()

    # if choice is e

    if choice == 'e':

        # prompt user for book id

        book_id = input('Please enter book id: ')

        # while book is not an integer

        while not book_id.isdigit():

            # prompt user for book id again

            book_id = input('id invalid, please enter book id again: ')

        # search for book with id

        res = cursor.execute(
            f"SELECT id, title, author, quantity FROM books WHERE id=?", (book_id,))

        # fetch all results from search

        results = res.fetchall()

        # while book id is already present

        while results:

            # prompt user for book id again

            book_id = input(
                "Book id already taken, please enter a new one: ")

            # while book is not an integer

            while not book_id.isdigit():

                book_id = input(
                    'Id invalid, please enter book id again: ')

            # search for book with id

            results = cursor.execute(
                f"SELECT id FROM books WHERE id=?", (book_id,))

            # fetch all results from search

            results = res.fetchall()
        # prompt user for book title

        title = input('Please enter title: ')

        # prompt user for book author

        author = input("Please enter author: ")

        # prompt user for book quantity

        quantity = input("Please enter quantity: ")

        # while quantity is not an integer

        while not quantity.isdigit():

            # prompt user for quantity again

            quantity = input('quantity invalid, please enter quantity again: ')

        # insert book into table

        cursor.execute("""
    INSERT INTO books(id, title, author, quantity) VALUES(?, ?, ?, ?) """, (book_id, title, author, quantity))

    # if choice is u

    elif choice == 'u':

        # prompt user for book id

        selected_id = input('Please enter book id: ')

        # Search for book

        res = cursor.execute(
            f"SELECT id, title, author, quantity FROM books WHERE id=?", (selected_id,))

        # fetch all results from search

        results = res.fetchall()

        # while no results

        while not results:

            # prompt user for book idea again

            selected_id = input(
                "Invalid book id, please enter book id again: ")

            # Search for book

            res = cursor.execute(
                f"SELECT id FROM books WHERE id=?", (selected_id,))

            # fetch all results from search

            results = res.fetchall()

            print(results)

        # infinite while loop

        while True:

            # prompt user for choice

            choice = input(""""Select one of the following options
            Change id - i
            Change title - t
            Change Author - a
            Change Quantity - q
            Go back - b
            """)

            # if choice is i

            if choice == 'i':

                # prompt user for new book id

                new_id = input("Please enter new id: ")

                # while new id is not an integer

                while not new_id.isdigit():

                    # prompt user for new book id

                    new_id = input('Id invalid, please enter book id again: ')

                # Search table for book

                res = cursor.execute(
                    f"SELECT id, title, author, quantity FROM books WHERE id=?", (new_id,))

                # fetch all results from search

                results = res.fetchall()

                # while results is found

                while results:

                    # prompt user for new book id

                    new_id = input(
                        "Book id already taken, please enter a new one: ")

                    # while book_id is not an integer

                    while not new_id.isdigit():

                        # prompt user for book_id again

                        new_id = input(
                            'Id invalid, please enter book id again: ')

                    # Search book table for id

                    results = cursor.execute(
                        f"SELECT id FROM books WHERE id=?", (new_id,))

                    # fetch all results from search

                    results = res.fetchall()

                # Update book table with new id

                cursor.execute("UPDATE books SET id=? WHERE id=?",
                               (new_id, selected_id))

            # if choice is t

            elif choice == 't':

                # prompt user for new title

                new_title = input("Please enter the new book title: ")

                # Update book with new title

                cursor.execute("UPDATE books SET title=? WHERE id=?",
                               (new_title, selected_id))

            # if choice is a

            elif choice == 'a':

                # prompt user for new author

                new_author = input("Please enter the new book author: ")

                # Update author of the book

                cursor.execute("UPDATE books SET author=? WHERE id=?",
                               (new_author, selected_id))

            # if choice is queue

            elif choice == 'q':

                # prompt user for new quantity

                new_quantity = input("Please enter the new book quantity: ")

                while not new_quantity.isdigit():  # if quantity is not an integer

                    # prompt user for new quantity

                    new_quantity = input(
                        'Quantity invalid, please enter quantity again: ')

                # Update books table with new quantity

                cursor.execute("UPDATE books SET quantity=? WHERE id=?",
                               (new_quantity, selected_id))

            # if choice is b

            elif choice == 'b':

                # break infinite while loop

                break

            # if no valid choice is selected

            else:

                # prompt user for new choice

                choice = input(""""Invalid choice, please select one of the following options
            Change id - i
            Change title - t
            Change Author - a
            Change Quantity - q
            Go back - b
            """)

    # if choice is d

    elif choice == 'd':

        # prompt user for id

        id_to_delete = input(
            'Please enter the id of the book you would like to delete: ')

        # wow id is not a integer

        while not id_to_delete.isdigit():

            # prompt user for id again

            id_to_delete = input(
                'id is not a number, please enter a number: ')

        # Search for book with id

        res = cursor.execute(
            f"SELECT id, title, author, quantity FROM books WHERE id=?", (id_to_delete,))

        # fetch all results from search

        results = res.fetchall()

        # while no results found

        while not results:

            # prompt user for id to delete

            id_to_delete = input(
                "Invalid book id, please enter book id again: ")

            # while id is not an integer

            while not id_to_delete.isdigit():

                # prompt user for id

                id_to_delete = input(
                    'Id is not a number, please enter a number: ')

            # Search for book with id

            results = cursor.execute(
                f"SELECT id FROM books WHERE id=?", (id_to_delete,))

            # fetch all results from search

            results = res.fetchall()

        # delete book with id

        cursor.execute('''DELETE FROM books WHERE id=?''', (id_to_delete,))

        # print book is deleted

        print("Book deleted")

    # if choice is s

    elif choice == 's':

        # prompt user for book id

        id_to_select = input('Please enter id of book to search: ')

        # while book_id is not an integer

        while not id_to_select.isdigit():

            # prompt user for book_id again

            id_to_select = input('id is not a number, please enter a number: ')

        # Search for book

        res = cursor.execute(
            f"SELECT id, title, author, quantity FROM books WHERE id=?", (id_to_select,))

        # fetch all results from search

        results = res.fetchone()

        # while no results

        while not results:

            # prompt user for book idea again

            id_to_select = input(
                "Invalid book id, please enter book id again: ")

            # while id is not an integer

            while not id_to_select.isdigit():

                # prompt user for new id

                id_to_select = input(
                    'Id is not a number, please enter a number: ')

            # Search for book

            res = cursor.execute(
                f"SELECT id, title, author, quantity FROM books WHERE id=?", (id_to_select,))

            # fetch all results from search

            results = res.fetchone()

        # initialize table

        table = [['id', 'title', 'author', 'quantity'],
                 [results[0], results[1], results[2], results[3]]]

        # print table with data from book

        print(tabulate(table))

    # if choice is x

    elif choice == 'x':

        # print good bye

        print('Good bye!')

        # commit changes to database

        database.commit()

        # break while loop

        break

    # prompt user for new choice

    else:

        choice = input('''Invalid choice, please choose again from the following options:
    e - Enter book
    u - Update book
    d - Delete book
    s - Search book
    x - exit  ''').lower()
