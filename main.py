from tkinter import *
from tkinter import messagebox
from pasword_generator import random_password
import pyperclip
import json


# ---------------------------- SEARCH BOX ------------------------------- #

def search():
    website = website_entry.get()

    if len(website) == 0:
        messagebox.showerror(title="Error", message="No website name entered.")
    else:
        try:
            with open("data.json", "r") as file:
                json_data = json.load(file)
        except:
            messagebox.showerror(title="Error", message="No Data Stored, Add some data first.")
        else:
            if website in json_data:
                messagebox.showinfo(title=website,
                                    message=f"Email: {json_data[website]['Email']}\nPassword: {json_data[website]['Password']}")
            else:
                messagebox.showerror(title="Error", message=f"No details for {website} found.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, END)
    password_entry.insert(END, random_password())


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    data = {
        website: {
            "Email": email,
            "Password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Error", message="Details can't be empty")

    else:
        popup_ok = messagebox.askokcancel(title=f"{website}",
                                          message=f"Details:\n\nEmail: {email}\nPassword: {password}\n\nClick 'OK' to save")
        if popup_ok:
            try:
                with open("data.json", 'r') as file:
                    json_data = json.load(file)
            except:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file)
            else:
                if website in json_data:
                    messagebox.showerror(title="Error", message="The data already exists! Try something new.")
                else:
                    json_data.update(data)
                    with open("data.json", 'w') as file:
                        json.dump(json_data, file)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

                website_entry.focus()
                pyperclip.copy(f"{password}")
                pyperclip.paste()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title(string="Password Manager")
window.config(padx=100, pady=100)

canvas = Canvas(width=200, height=200)

img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = Label(window, text="Website:", font=('normal', 15))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=('normal', 15))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=('normal', 15))
password_label.grid(row=3, column=0)

website_entry = Entry(width=18)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, string="rajat123@gmail.com")

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

generate_pass_button = Button(text="Generate Password", font=('normal', 9), width=15, fg='black', bg="#D0BFFF",
                              highlightthickness=0,
                              command=generate_password)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=32, fg='white', bg="#008170", highlightthickness=0, command=add_data)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, fg='white', bg="#5272F2", height=1, font=('normal', 9), command=search)
search_button.grid(row=1, column=2)

window.mainloop()

