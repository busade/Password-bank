from tkinter import *
import string
from tkinter import messagebox
from random import choice, randint, shuffle


def generate_password():

    password_letter = [choice(string.ascii_letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(string.punctuation) for _ in range(randint(2, 4))]
    password_numbers = [choice(string.hexdigits) for _ in range(randint(2, 4))]
    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)

    lock = "".join(password_list)
    pass_phrase_entry.insert(0, password_list)

def save():
    website = site_entry.get()
    email = mail_user_entry.get()
    password = pass_phrase_entry.get()

    if len(website)==0 or len (email)==0:
        messagebox.showinfo(title="Error😈😈", message= " You can't leave any field blank")

    else:
        is_ok = messagebox.askokcancel(title="Confirm!", message= f"This are the details provided for {website}\n Email:{email}\n Password: {password}\n Do you wnat to save?")

        if is_ok:
            with open ("doc.txt", 'a' ) as file_doc:
                file_doc.write(f"{website} | {email} | {password}\n")
                site_entry.delete(0,END)
                pass_phrase_entry.delete(0, END)



# def view():
#     index = 0
#     arg = search.get()

 
#     with open("doc.txt","r") as f:
#         for line_number, line in enumerate(f,start = 0):
#             columns= line.strip().split(",")
#             values= columns[index]
#             print("values")
                
#             if arg in values:
#                 for idx, value  in enumerate(columns, start=0):
#                     details={"key":idx,"value":value}
#                     return messagebox.showinfo(title="details", message= f"This are the details provided for {details[0]}\n Email:{details[1]}\n Password: {details[2]}")

def view():
    arg = search.get()

    with open("doc.txt", "r") as f:
        for line_number, line in enumerate(f, start=0):
            columns = line.strip().split("|")

            if arg in columns[0]:  # Assuming the website is in the first column
                messagebox.showinfo(
                    title="details",
                    message=f"This are the details provided for {columns[0]}\n Email:{columns[1]}\n Password: {columns[2]}",
                )
    


window= Tk()

window.title = ("Password manager and Genrator")
window.config(padx=20,pady=20)

canvas= Canvas( height=150, width=150, background='white')
logo_img = PhotoImage(file ="log.png")

canvas.create_image(100,100, image = logo_img)
canvas.grid(row=0, column=1)

site_name = Label(text="Website")
site_name.grid(column=0, row=2)

site_entry = Entry(width=55)
site_entry.grid(column=1, row=2, columnspan=2)
site_entry.focus()

mail_user = Label(text='Email/Username:')
mail_user.grid(column=0, row=3)

mail_user_entry = Entry(width=55)
mail_user_entry.grid(column=1, row=3, columnspan=2)
mail_user_entry.insert(0, 'sample@mail.com')

pass_phrase = Label(text="Password:")
pass_phrase.grid(column=0, row=4)

pass_phrase_entry = Entry(width=35)
pass_phrase_entry.grid(column=1, row=4, columnspan=1)


pass_generator = Button(text='Generate Password', command= generate_password)
pass_generator.grid(column=2, row=4)

addition = Button(text='Add', width=36 , command = save)
addition.grid(column=1, row=5, columnspan=2)

search = Entry(width=35)
search.grid(column=1,row=6)

search_button= Button(text="Search", command=view)
search_button.grid(column=2,row=6)



window.mainloop()