import tasks
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
root.title("Stock Taking")
root.geometry("600x600")


class StockTaking:
    def __init__(self, main, category, name, productID, price, quantity):
        self.messagebox = messagebox
        self.category = category,
        self.name = name,
        self.productID = productID,
        self.price = price,
        self.quantity = quantity

        # font family and size stored in variable label_font
        self.label_font = font.Font(family='Georgia', size='20', weight='bold')
        self.font_small = font.Font(family='Georgia', size='12')

        # creating frames
        self.main_frame = tk.Frame(main)
        self.main_frame.grid()

        self.first_frame = tk.Frame(self.main_frame, borderwidth=1, relief='solid')
        self.first_frame.grid(pady=10)

        self.second_frame = tk.Frame(self.main_frame)
        self.second_frame.grid()

        self.second_frame2 = tk.Frame(self.main_frame)
        self.second_frame2.grid()

        # define the label message frame
        self.product_category = tk.Label(self.first_frame, text='Product Category :',
                                         font=self.font_small,
                                         fg='black')
        self.product_category.grid(row=0, column=0, sticky='w')

        self.product_name = tk.Label(self.first_frame, text='Product Name :',
                                     font=self.font_small,
                                     fg='black')
        self.product_name.grid(row=1, column=0, sticky='w')

        self.productID = tk.Label(self.first_frame, text='Product ID:',
                                  font=self.font_small,
                                  fg='black')
        self.productID.grid(row=2, column=0, sticky='w')

        self.product_price = tk.Label(self.first_frame, text='Product prices:',
                                      font=self.font_small,
                                      fg='black')
        self.product_price.grid(row=3, column=0, sticky='w')

        self.quantity = tk.Label(self.first_frame, text='Quantity:',
                                 font=self.font_small,
                                 fg='black')
        self.quantity.grid(row=4, column=0, sticky='w')

        # creating a button for the first frame
        self.save_button = tk.Button(self.first_frame, text='Save',
                                     font=self.font_small, command=self.save)

        self.save_button.grid(row=5, column=1, pady=10, padx=10)

        # creating combo boxes
        self.category_combobox = ttk.Combobox(self.first_frame, font=self.font_small,
                                              values=[
                                                  'Mechanical',
                                                  'Electronic',
                                                  'Wooden',
                                                  'Doll'])
        self.category_combobox.current()
        self.category_combobox.grid(row=0, column=1, padx=20, pady=5)

        self.name_combobox = ttk.Combobox(self.first_frame, font=self.font_small,
                                          values=[
                                              'Toy Car',
                                              'Hover Board',
                                              'Rocking Horse',
                                              'Teddy Bear'])
        self.name_combobox.current()
        self.name_combobox.grid(row=1, column=1, padx=20, pady=5)

        self.productID_combobox = ttk.Combobox(self.first_frame, font=self.font_small,
                                               values=[
                                                   '11456',
                                                   '34567',
                                                   '67453',
                                                   '34688'])
        self.productID_combobox.current()
        self.productID_combobox.grid(row=2, column=1, padx=20, pady=5)

        self.product_price = ttk.Combobox(self.first_frame, font=self.font_small,
                                          values=[
                                              '£80',
                                              '£100',
                                              '£200',
                                              '£150'])
        self.product_price.current()
        self.product_price.grid(row=3, column=1, padx=20, pady=5)

        self.quantity = ttk.Combobox(self.first_frame, font=self.font_small,
                                     values=[
                                         '40xqnt',
                                         '20xqnt',
                                         '50xqnt',
                                         '80xqnt'])

        self.quantity.current()
        self.quantity.grid(row=4, column=1, padx=20, pady=5)

        # creating a text receipt

        self.my_text = tk.Text(self.second_frame,
                               font=self.font_small,
                               width=50, height=17)
        self.my_text.grid(row=0, column=0, padx=20)

        # creating buttons
        self.print_button = tk.Button(self.second_frame2, text='Print',
                                      font=self.font_small, command=self.print)
        self.print_button.grid(row=0, column=0, pady=10, padx=10)

        self.reset_button = tk.Button(self.second_frame2, text='Reset',
                                      font=self.font_small,
                                      command=self.reset)
        self.reset_button.grid(row=0, column=1, pady=10, padx=10)

        self.exit_button = tk.Button(self.second_frame2, text='Exit',
                                     font=self.font_small, command=exit)
        self.exit_button.grid(row=0, column=2, pady=10, padx=10)

        # creating a label to get text from
        self.my_label = tk.Label(main, text='')
        self.my_label.grid()

    # defining reset function
    def reset(self):
        self.my_text.delete(1.0, tk.END)

    def print(self):
        text_file = open("sample.txt", "r")
        stuff = text_file.read()
        self.my_text.insert(tk.END, stuff)
        text_file.close()

    def save(self):
        category = 'Electronic'
        name = 'Hover Board'
        product_id = 34567
        price = "£100"
        quantity = "20xqnt"

        if category == self.category_combobox.get():
            self.messagebox.showwarning('Product', 'Product Quantity Low In Stock')
            # clearing combo boxes after option has been chosen
            self.product_price.delete(0, tk.END)
            self.productID_combobox.delete(0, tk.END)
            self.name_combobox.delete(0, tk.END)
            self.category_combobox.delete(0, tk.END)
            self.quantity.delete(0, tk.END)

        elif name == self.name_combobox.get():
            self.messagebox.showwarning('Product', 'Product Quantity Low In Stock')

        elif product_id == self.productID_combobox.get():
            self.messagebox.showwarning('Product', 'Product Quantity Low In Stock')

        elif price == self.product_price.get():
            self.messagebox.showwarning('Product', 'Product Quantity Low In Stock')

        elif quantity == self.quantity.get():
            self.messagebox.showwarning('Product', 'Product Quantity Low In Stock')

        else:
            self.messagebox.askyesno('Products', 'Proceed To Save?')
            # clear combo boxes after option has been chosen
            self.product_price.delete(0, tk.END)
            self.productID_combobox.delete(0, tk.END)
            self.name_combobox.delete(0, tk.END)
            self.category_combobox.delete(0, tk.END)
            self.quantity.delete(0, tk.END)


stock = StockTaking(root, 'category', 'name', 'productID', 'price', 'quantity')

root.mainloop()
