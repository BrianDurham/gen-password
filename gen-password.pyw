import tkinter as tk
from tkinter import ttk
import string
import secrets
import pyperclip  # `pip install pyperclip`

def generate_password():
    try:
        length = int(length_var.get())
    except ValueError:
        password_var.set("Invalid length")
        return

    chars = ''
    if use_lower.get(): chars += string.ascii_lowercase
    if use_upper.get(): chars += string.ascii_uppercase
    if use_digits.get(): chars += string.digits
    if use_symbols.get(): chars += string.punctuation
    if exclude_similar.get():
        for c in 'oO0iIl1': chars = chars.replace(c, '')
    if exclude_ambiguous.get():
        for c in '{}[]()/\\\'"`~,;:.<>': chars = chars.replace(c, '')

    if not chars:
        if trailing_symbol_var.get() and length < 2:
            password_var.set("Length too short for trailing symbol")
            return
        password_var.set("Select options!")
        return

    actual_length = length - 1 if trailing_symbol_var.get() and length > 1 else length
    password = ''.join(secrets.choice(chars) for _ in range(actual_length))
    if trailing_symbol_var.get():
        trailing_symbols = ['!', '$', '@', '#', '%', '^', '&', '*']
        password +=secrets.choice(trailing_symbols)
    password_var.set(password)

def copy_password():
    pyperclip.copy(password_var.get())

# GUI setup
root = tk.Tk()
root.title("Password Generator")

length_var = tk.StringVar(value='16')
password_var = tk.StringVar()

tk.Label(root, text="Password Length:").grid(row=0, column=0, sticky='e')
tk.Entry(root, textvariable=length_var, width=5).grid(row=0, column=1, sticky='w')

use_lower = tk.BooleanVar(value=True)
use_upper = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=False)
exclude_similar = tk.BooleanVar(value=False)
exclude_ambiguous = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Lowercase (a-z)", variable=use_lower).grid(row=1, column=0, columnspan=2, sticky='w')
tk.Checkbutton(root, text="Uppercase (A-Z)", variable=use_upper).grid(row=2, column=0, columnspan=2, sticky='w')
tk.Checkbutton(root, text="Numbers (0-9)", variable=use_digits).grid(row=3, column=0, columnspan=2, sticky='w')
tk.Checkbutton(root, text="Symbols", variable=use_symbols).grid(row=4, column=0, columnspan=2, sticky='w')
tk.Checkbutton(root, text="Exclude Similar (oO0iIl1)", variable=exclude_similar).grid(row=5, column=0, columnspan=2, sticky='w')
tk.Checkbutton(root, text="Exclude Ambiguous", variable=exclude_ambiguous).grid(row=6, column=0, columnspan=2, sticky='w')

trailing_symbol_var = tk.BooleanVar(value=True)
trailing_symbol_check = tk.Checkbutton(root, text="Trailing Symbol (! or $)", variable=trailing_symbol_var)
trailing_symbol_check.grid(row=6, column=0, sticky="w")

tk.Button(root, text="Generate Password", command=generate_password).grid(row=7, column=0, columnspan=2, pady=5)

tk.Entry(root, textvariable=password_var, width=30).grid(row=8, column=0, columnspan=2)
tk.Button(root, text="Copy", command=copy_password).grid(row=8, column=2)

root.mainloop()

