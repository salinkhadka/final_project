from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3

root = Tk()
root.title("Customer-order")
root.geometry("900x700")
root.resizable(0, 0)

# define image
my_image = Image.open('iio.png')
resized_image = my_image.resize((900, 700))
converted_image = ImageTk.PhotoImage(resized_image)
mylabel = Label(root, image=converted_image)
mylabel.pack()

# entry for Name
a1 = Entry(root, font=("bold", 15), width=20, bd=0, borderwidth=0)
a1.place(x=170, y=225)

# entry for Location
a2 = Entry(root, font=("bold", 15), width=20, borderwidth=0)
a2.place(x=170, y=350)

# entry for quantity
a3 = Entry(root, font=("bold", 15), width=10, borderwidth=0)
a3.place(x=580, y=225)

# entry for Contact number
a4 = Entry(root, font=("bold", 15), width=17, borderwidth=0)
a4.place(x=685, y=350)

# button
a6 = Button(root, text='Confirm', width=10, borderwidth=0, font=('bold', 15), fg='black', bg='gray')
a6.place(x=365, y=535)


# combobox
options = ['1. Apple', '2. Mango', '3. Banana', '4. Litchi', '5. Watermelon', '6. Papaya', "7. Guava", "8. Jack fruit"]
cb1 = ttk.Combobox(root, values=options, width=17, font=("Arial", 15))
cb1.place(x=550, y=450)


# def aayush():
#     global fruit
#     print(a1.get())
#     print(a2.get())
#     print(a3.get())
#     print(a4.get())
#     fruit = cb1.get()
#     print(fruit)


def confirm_order():
    conn = sqlite3.connect("order_details.db")
    c = conn.cursor()
    c.execute("INSERT INTO orders VALUES (:Name, :Location, :Phonenumber ,:Item, :Quantity)",
              {
                  "Name": a1.get(),
                  "Location": a2.get(),
                  "Item": cb1.get(),
                  "Quantity": a3.get(),
                  "Phonenumber": a4.get()
              })

    conn.commit()
    conn.close()
    a1.delete(0,END)
    a2.delete(0,END)
    a3.delete(0,END)
    a4.delete(0,END)
    cb1.set("")
a6.configure(command=confirm_order)


root.mainloop()
