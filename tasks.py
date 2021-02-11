import tkinter as tk
import tkinter.font as font
from tkinter import messagebox, Entry

# importing sqlite for database
import sqlite3

# creating a window
root = tk.Tk()
root.title("All About Toys")
root.geometry("450x400")


class AdminFeatures:
    def __init__(self, main, name, password):
        self.messagebox = messagebox
        self.__name = name
        self.__password = password
        # font family and size stored in variable label_font
        self.label_font = font.Font(family='Georgia', size='20', weight='bold')
        self.font_small = font.Font(family='Georgia', size='12')

        # define the label message frame
        self.label_message = tk.Label(main, text='All About Toys Login Page',
                                      font=self.label_font,
                                      fg='black')
        self.label_message.grid(row=0, column=0, columnspan=5)
        self.entry_label = tk.Label(main,
                                    text='Enter User Name And Password',
                                    font=self.label_font)
        self.entry_label.grid(row=1, column=0, columnspan=5, pady=10)

        # creating a label for userid and password
        self.username_label = tk.Label(main,
                                       text="User Name:",
                                       font=self.font_small)
        self.username_label.grid(row=2, column=1, columnspan=2, pady=10)
        self.password = tk.Label(main, text="Password:",
                                 font=self.font_small)
        self.password.grid(row=3, column=1, columnspan=2)

        # creating entry boxes
        self.username_box = tk.Entry(main)
        self.username_box.grid(row=2, column=3)

        self.password_box = tk.Entry(main)
        self.password_box.grid(row=3, column=3, pady=5)

        ########################################################################

        self.menu_bar = tk.Menu(root)

        # create a menu and add commands
        self.database_menu = tk.Menu(self.menu_bar, tearoff=0)

        self.database_menu.add_command(label='Database')
        self.database_menu.add_separator()

        # creating a menu bar for database
        self.menu_bar.add_cascade(label='Database',
                                  menu=self.database_menu)

        # create a menu and add commands
        self.stock_menu = tk.Menu(self.menu_bar, tearoff=0)

        self.stock_menu.add_command(label='Inventory')
        self.stock_menu.add_separator()

        # creating a menu bar for stock inventory
        self.menu_bar.add_cascade(label='Stock Inventory',
                                  menu=self.stock_menu)
        # creating a menu for for exit
        self.menu_bar.add_cascade(label='Exit',
                                  command=quit)

        root.config(menu=self.menu_bar)

        # creating a login button

        self.button = tk.Button(main, text="Login",
                                font=self.font_small,
                                command=self.popup)
        self.button.grid(row=4, column=3, pady=10)

    def popup(self):
        username = 'Samuel'
        password = 'Python'
        my_text = open("details.txt", "r+")
        if username == self.username_box.get():
            self.messagebox.showinfo('Welcome', 'Login Successful')

        elif password == self.password_box.get():
            self.messagebox.showinfo('Welcome', 'Login Successful')

        else:
            self.messagebox.showerror('Error', 'Check Login Details')

        my_text.read()
        my_text.close()

    # defining class methods, in this part of the code, i just stated the class methods
    # the actual implementation and design of the code was done in the database class below
    def add_category(self):
        pass

    def delete_records(self):
        pass

    def update_products(self):
        pass

    def delete_record(self):
        pass

    def submit(self):
        pass


log = AdminFeatures(root, "Samuel", "Python")
root.mainloop()

# creating a new window for database
database = tk.Tk()
database.title("All About Toys")
database.geometry("450x400")

# create database or connect to one
connection = sqlite3.connect("Category_book.db")
# create cursor
cursor = connection.cursor()

'''cursor.execute(""" CREATE TABLE Records (Add_Category text,
                                                 Product_ID integer,
                                                 Quantity integer,
                                                 Product_Name text
                                                  )""")'''


class Database:
    def __init__(self, records):
        self.records = records

        # create a global variable for text box names
        global add_category
        global product_id
        global quantity
        global product_name

        # create a global variable for delete box
        global delete_box

        # create entry box
        add_category = tk.Entry(database, width=30)
        add_category.grid(row=0, column=1, padx=20, pady=(10, 0))
        product_id = tk.Entry(database, width=30)
        product_id.grid(row=1, column=1, padx=20)
        quantity = tk.Entry(database, width=30)
        quantity.grid(row=2, column=1, padx=20)
        product_name = tk.Entry(database, width=30)
        product_name.grid(row=3, column=1, padx=20)
        # delete entry box
        delete_box = tk.Entry(database, width=30)
        delete_box.grid(row=6, column=1, pady=5)

        # create text box label
        add_category_label = tk.Label(database, text="Add Category")
        add_category_label.grid(row=0, column=0, pady=(10, 0))
        product_id_label = tk.Label(database, text="Product ID")
        product_id_label.grid(row=1, column=0)
        quantity_label = tk.Label(database, text="Quantity")
        quantity_label.grid(row=2, column=0)
        product_name_label = tk.Label(database, text="Product Name")
        product_name_label.grid(row=3, column=0)
        # delete text box label
        delete_box_label = tk.Label(database, text=" Select ID:")
        delete_box_label.grid(row=6, column=0, pady=5)
        # create submit button
        submit_button = tk.Button(database, text="Add To Database",
                                  command=self.submit)
        submit_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

        # create a query button
        query_button = tk.Button(database, text="Show records", command=self.query)
        query_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

        # create a delete button
        delete_button = tk.Button(database, text="Delete record", command=self.delete_record)
        delete_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=134)

        # create an update button
        edit_button = tk.Button(database, text="Update record", command=self.update_record)
        edit_button.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

    def save_record(self):
        # create a database connection or connect to one
        connection = sqlite3.connect("Category_book.db")
        # create cursor
        cursor = connection.cursor()
        # create global variables for text box names

        record_id = delete_box.get()
        cursor.execute("""UPDATE Records SET
                                       Add_Category = :category,
                                       Product_ID = :product,
                                       Quantity = :quantity,
                                       Product_Name = :name

                                       WHERE oid = :oid""",
                       {"category": add_category_editor.get(),
                        "product": product_id_editor.get(),
                        "quantity": quantity_editor.get(),
                        "name": product_name_editor.get(),

                        "oid": record_id
                        })

        connection.commit()
        connection.close()
        editor.destroy()

        # create and update function to update a record

    def update_record(self):
        global editor
        # creating a new window for update record
        # instead of root, change it to editor
        editor = tk.Tk()
        editor.title("Update a record")
        editor.geometry("450x400")

        connection = sqlite3.connect("Category_book.db")
        # create cursor
        cursor = connection.cursor()

        # variable to get id number n delete box
        record_id = delete_box.get()
        # Query the database
        cursor.execute("SELECT * FROM Records WHERE oid = " + record_id)

        # create a global variable for text box names
        global add_category_editor
        global product_id_editor
        global quantity_editor
        global product_name_editor

        # create text box
        add_category_editor = tk.Entry(editor, width=30)
        add_category_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
        product_id_editor = tk.Entry(editor, width=30)
        product_id_editor.grid(row=1, column=1, padx=20)
        quantity_editor = tk.Entry(editor, width=30)
        quantity_editor.grid(row=2, column=1, padx=20)
        product_name_editor = tk.Entry(editor, width=30)
        product_name_editor.grid(row=3, column=1, padx=20)

        # create text box label
        add_category_label_editor = tk.Label(editor, text="Add Category")
        add_category_label_editor.grid(row=0, column=0, pady=(10, 0))
        product_id_label_editor = tk.Label(editor, text="Product ID")
        product_id_label_editor.grid(row=1, column=0)
        quantity_label_editor = tk.Label(editor, text="Quantity")
        quantity_label_editor.grid(row=2, column=0)
        product_name_label_editor = tk.Label(editor, text="Product Name")
        product_name_label_editor.grid(row=3, column=0)

        documents = cursor.fetchall()

        # loop through results
        # using the insert command
        for document in documents:
            add_category_editor.insert(0, document[0])
            product_id_editor.insert(0, document[1])
            quantity_editor.insert(0, document[2])
            product_name_editor.insert(0, document[3])

        # create a save button to save edited record
        save_button = tk.Button(editor, text="Save record", command=self.save_record)
        save_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

        editor.mainloop()
        connection.commit()
        connection.close()

    # create a function to delete a record
    def delete_record(self):
        # create a global variable
        global delete_box

        # create database or connect to one
        connection = sqlite3.connect("Category_book.db")
        # create cursor
        cursor = connection.cursor()
        # delete a record
        cursor.execute("DELETE FROM Records WHERE oid= " + delete_box.get())

        connection.commit()
        connection.close()

    # create submit function
    def submit(self):
        # create database or connect to one
        connection = sqlite3.connect("Category_book.db")
        # create cursor
        cursor = connection.cursor()

        # insert into table
        cursor.execute("INSERT INTO Records VALUES(:add_category, :product_id, :quantity, :product_name)",

                       {
                           'add_category': add_category.get(),
                           'product_id': product_id.get(),
                           'quantity': quantity.get(),
                           'product_name': product_name.get()
                       })

        connection.commit()
        connection.close()

    # create query function
    def query(self):
        connection = sqlite3.connect("Category_book.db")
        # create cursor
        cursor = connection.cursor()

        # Query the database
        cursor.execute("SELECT *, oid FROM Records")
        documents = cursor.fetchall()
        print(documents)
        # loop through result
        print_documents = ''
        for document in documents:
            print(str(document), end=' ' + "\n")
            print_documents += str(document) + "\n"

        query_label = tk.Label(database, text=print_documents)
        query_label.grid(row=9, column=0, columnspan=2)

        connection.commit()
        connection.close()


connection.commit()
connection.close()

# creating an instance of the class Database
database_instance = Database('records')
database.mainloop()
