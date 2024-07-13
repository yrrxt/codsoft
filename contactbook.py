import tkinter as tk
from tkinter import ttk

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("800x600")
        self.root.configure(background="#f0f0f0")

        # Configure title font and color
        self.root.option_add('*Font', 'Helvetica 20 bold')
        self.root.option_add('*foreground', '#800080')  # Purple color for title

        # Create a style for ttk widgets
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TButton', background='#0078d7', foreground='white', font=('Helvetica', 12))
        self.style.map('TButton', background=[('active', '#c968c9')])  # Change active button color

        # Create a notebook with tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Create a frame for the contact list
        self.frm_contact_list = ttk.Frame(self.notebook, style='TFrame')
        self.notebook.add(self.frm_contact_list, text="Contact List")

        # Create a frame for the add contact form
        self.frm_add_contact = ttk.Frame(self.notebook, style='TFrame')
        self.notebook.add(self.frm_add_contact, text="Add Contact")

        # Create a frame for the search contact form
        self.frm_search_contact = ttk.Frame(self.notebook, style='TFrame')
        self.notebook.add(self.frm_search_contact, text="Search Contact")

        # Create a treeview for the contact list
        self.tree_contact_list = ttk.Treeview(self.frm_contact_list, columns=("Name", "Email", "Phone"), show="headings")
        self.tree_contact_list.pack(fill="both", expand=True)

        # Define columns heading and stretch them
        self.tree_contact_list.heading("Name", text="Name")
        self.tree_contact_list.heading("Email", text="Email")
        self.tree_contact_list.heading("Phone", text="Phone")
        self.tree_contact_list.column("Name", width=200, anchor='center')
        self.tree_contact_list.column("Email", width=300, anchor='center')
        self.tree_contact_list.column("Phone", width=150, anchor='center')

        # Create a scrollbar for the contact list
        self.scrollbar_contact_list = ttk.Scrollbar(self.frm_contact_list, orient="vertical", command=self.tree_contact_list.yview)
        self.scrollbar_contact_list.pack(side="right", fill="y")
        self.tree_contact_list.configure(yscrollcommand=self.scrollbar_contact_list.set)

        # Create labels and entries for the add contact form
        self.lbl_first_name = ttk.Label(self.frm_add_contact, text="First Name:", style='TLabel')
        self.lbl_first_name.pack()
        self.ent_first_name = ttk.Entry(self.frm_add_contact, width=50)
        self.ent_first_name.pack()

        self.lbl_last_name = ttk.Label(self.frm_add_contact, text="Last Name:", style='TLabel')
        self.lbl_last_name.pack()
        self.ent_last_name = ttk.Entry(self.frm_add_contact, width=50)
        self.ent_last_name.pack()

        self.lbl_email = ttk.Label(self.frm_add_contact, text="Email:", style='TLabel')
        self.lbl_email.pack()
        self.ent_email = ttk.Entry(self.frm_add_contact, width=50)
        self.ent_email.pack()

        self.lbl_phone = ttk.Label(self.frm_add_contact, text="Phone:", style='TLabel')
        self.lbl_phone.pack()
        self.ent_phone = ttk.Entry(self.frm_add_contact, width=50)
        self.ent_phone.pack()

        # Create a button to add the contact
        self.btn_add_contact = ttk.Button(self.frm_add_contact, text="Add Contact", command=self.add_contact, style='TButton')
        self.btn_add_contact.pack(pady=10)

        # Create labels and entries for the search contact form
        self.lbl_search_name = ttk.Label(self.frm_search_contact, text="Search Name:", style='TLabel')
        self.lbl_search_name.pack()
        self.ent_search_name = ttk.Entry(self.frm_search_contact, width=50)
        self.ent_search_name.pack()

        # Create a button to search for the contact
        self.btn_search_contact = ttk.Button(self.frm_search_contact, text="Search Contact", command=self.search_contact, style='TButton')
        self.btn_search_contact.pack(pady=10)

    def add_contact(self):
        # Get the values from the entries
        first_name = self.ent_first_name.get()
        last_name = self.ent_last_name.get()
        email = self.ent_email.get()
        phone = self.ent_phone.get()

        # Add the contact to the treeview
        self.tree_contact_list.insert("", "end", values=(first_name, last_name, email, phone))

    def search_contact(self):
        # Get the value from the search entry
        search_name = self.ent_search_name.get()

        # Search for the contact in the treeview
        for child in self.tree_contact_list.get_children():
            if search_name in self.tree_contact_list.item(child, "values")[0]:
                self.tree_contact_list.selection_set(child)
                break

if __name__ == "__main__":
    root = tk.Tk()
    contact_book = ContactBook(root)
    root.mainloop()
