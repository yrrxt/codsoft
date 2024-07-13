import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        messagebox.showerror("Error", "Password length must be at least 8 characters.")
        return
    password = ''.join(random.choice(all_characters) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())

root = tk.Tk()
root.title("Password Generator")

style = ttk.Style()
style.theme_use("clam")

style.configure("CurveEntry.TEntry", foreground="black", background="white", fieldbackground="white", borderwidth=10, relief="flat", highlightthickness=0)
style.map("CurveEntry.TEntry", foreground=[('focus', 'black')], background=[('focus', '#6c5ce7')])

style.configure("CurveButton.TButton", font=("Segoe UI", 14), foreground="white", background="#9e72ea", borderwidth=10, relief="flat", highlightthickness=0)
style.map("CurveButton.TButton", foreground=[('pressed', 'white'), ('active', 'white')], background=[('pressed', 'white'), ('active', '#9e72ea')])

style.configure("CustomButton.TButton", font=("Segoe UI", 14), foreground="white", background="#9e72ea", borderwidth=10, relief="ridge")

main_frame = tk.Frame(root, bg="white")
main_frame.pack(fill="both", expand=True)

header_label = tk.Label(main_frame, text="Password Generator", font=("Segoe UI", 40, "bold"), fg="#8072ea", bg="white")
header_label.pack(pady=20)

length_label = tk.Label(main_frame, text="Password Length:", font=("Segoe UI", 16, "italic"), fg="black", bg="white")
length_label.pack()

length_entry = ttk.Entry(main_frame, width=20, font=("Segoe UI", 16, ""), style="CurveEntry.TEntry")
length_entry.pack(pady=10)

generate_button = ttk.Button(main_frame, text="Generate Password", command=lambda: generate_password(int(length_entry.get())), style="CustomButton.TButton")
generate_button.pack(pady=10)

password_label = tk.Label(main_frame, text="Generated Password:", font=("Segoe UI", 16, "italic"), fg="black", bg="white")
password_label.pack()

password_entry = ttk.Entry(main_frame, width=40, font=("Segoe UI", 16, ""), style="CurveEntry.TEntry")
password_entry.pack(pady=10)

copy_button = ttk.Button(main_frame, text="Copy Password", command=copy_password, style="CustomButton.TButton")
copy_button.pack(pady=10)

root.mainloop()