
import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_var.get())
        if length < 8 or length > 32:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Length must be a number between 8 and 32.")
        return

    use_upper = upper_var.get()
    use_numbers = number_var.get()
    use_symbols = symbol_var.get()

    chars = list(string.ascii_lowercase)
    if use_upper:
        chars += list(string.ascii_uppercase)
    if use_numbers:
        chars += list(string.digits)
    if use_symbols:
        chars += list("!@#$%^&*()-_=+[]{}<>?")

    if not chars:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    result_var.set(password)

app = tk.Tk()
app.title("StrongPass - Password Generator")
app.geometry("400x300")
app.config(padx=20, pady=20)

tk.Label(app, text="Password Length (8-32):").pack()
length_var = tk.StringVar(value="12")
tk.Entry(app, textvariable=length_var).pack()

upper_var = tk.BooleanVar()
tk.Checkbutton(app, text="Include Uppercase", variable=upper_var).pack()

number_var = tk.BooleanVar()
tk.Checkbutton(app, text="Include Numbers", variable=number_var).pack()

symbol_var = tk.BooleanVar()
tk.Checkbutton(app, text="Include Symbols", variable=symbol_var).pack()

tk.Button(app, text="Generate Password", command=generate_password).pack(pady=10)

result_var = tk.StringVar()
tk.Entry(app, textvariable=result_var, font=("Courier", 12), justify="center").pack()

app.mainloop()
