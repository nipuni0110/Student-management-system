import sqlite3
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
import tkinter as tk

# Create table
conn = sqlite3.connect("data.db")
table_create_query = '''CREATE TABLE IF NOT EXISTS student_details
                        (rollno TEXT PRIMARY KEY, 
                         name TEXT, 
                         class TEXT, 
                         contact TEXT, 
                         section TEXT, 
                         parentname TEXT, 
                         address TEXT, 
                         gender TEXT, 
                         dob TEXT)
                        '''
conn.execute(table_create_query)
conn.close()

# Tkinter window setup
ctk.set_appearance_mode("light")
win = ctk.CTk()
win.geometry("1350x700+0+0")
win.title("Student Management System")

title_label = ctk.CTkLabel(win, text="Student Management System", font=("Arial", 30, "bold"), fg_color="lightblue", text_color="blue", corner_radius=6, padx=20, pady=20)
title_label.pack(side=ctk.TOP, fill=ctk.X)

detail_label=ctk.CTkLabel(win, text="Enter Details", font=("Arial",15,"bold"))
detail_label.pack(side=ctk.TOP, fill=ctk.X, anchor="w")
detail_label.place(x=20, y=90, anchor="nw")

detail_frame = ctk.CTkFrame(win, corner_radius=10, fg_color="lightblue", width=440, height=560)
detail_frame.place(x=20, y=120)

data_frame = ctk.CTkFrame(win, corner_radius=10, fg_color="lightblue", width=810, height=575)
data_frame.place(x=475, y=90)

# Variables

rollno = ""
name = ""
class_var = ""
contact = ""
section = ""
parentname = ""
address = ""
gender = ""
dob = ""
search_by = ""
search_txt = ""

rollno = tk.StringVar()
name = tk.StringVar()
class_var = tk.StringVar()
contact = tk.StringVar()
section = tk.StringVar()
parentname = tk.StringVar()
address = tk.StringVar()
gender = tk.StringVar()
dob = tk.StringVar()

search_by = tk.StringVar()
search_txt = tk.StringVar()

# Functions to get and set values for the widgets
def set_values():
    rollno_ent.set(rollno)
    name_ent.set(name)
    class_ent.set(class_var)
    contact_ent.set(contact)
    section_ent.set(section)
    parentname_ent.set(parentname)
    address_ent.set(address)
    gender_ent.set(gender)
    dob_ent.set(dob)
    

def get_values():
    global rollno, name, class_var, contact, section, parentname, address, gender, dob
    rollno = rollno_ent.get()
    name = name_ent.get()
    class_var = class_ent.get()
    contact = contact_ent.get()
    section = section_ent.get()
    parentname = parentname_ent.get()
    address = address_ent.get()
    gender = gender_ent.get()
    dob = dob_ent.get()

# Entry Widgets
rollno_lbl = ctk.CTkLabel(detail_frame, text="Roll No", font=("Arial", 15))
rollno_lbl.grid(row=0, column=0, padx=2, pady=2)
rollno_ent = ctk.CTkEntry(detail_frame, font=("Arial", 15))
rollno_ent.grid(row=0, column=1, padx=2, pady=2)

name_lbl = ctk.CTkLabel(detail_frame, text="Name", font=("Arial", 15))
name_lbl.grid(row=1, column=0, padx=2, pady=2)
name_ent = ctk.CTkEntry(detail_frame, font=("Arial", 15))
name_ent.grid(row=1, column=1, padx=2, pady=2)

class_lbl = ctk.CTkLabel(detail_frame, text="Class", font=("Arial", 15))
class_lbl.grid(row=2, column=0, padx=2, pady=2)
class_ent = ctk.CTkEntry(detail_frame, font=("Arial", 15))
class_ent.grid(row=2, column=1, padx=2, pady=2)

section_lbl = ctk.CTkLabel(detail_frame, text="Section", font=("Arial", 15))
section_lbl.grid(row=3, column=0, padx=2, pady=2)
section_ent = ctk.CTkEntry(detail_frame, font=("Arial", 15))
section_ent.grid(row=3, column=1, padx=2, pady=2)

contact_label = ctk.CTkLabel(detail_frame, text="Contact", font=("Arial", 15))
contact_label.grid(row=4, column=0, padx=2, pady=2)
contact_ent = ctk.CTkEntry(detail_frame, font=("Arial", 15))
contact_ent.grid(row=4, column=1, padx=2, pady=2)

parentname_label = ctk.CTkLabel(detail_frame, text="Parent's Name", font=("Arial", 15))
parentname_label.grid(row=5, column=0, padx=2, pady=2)
parentname_ent = ctk.CTkEntry(detail_frame, font=("Arial", 15))
parentname_ent.grid(row=5, column=1, padx=2, pady=2)

address_lbl = ctk.CTkLabel(detail_frame, text="Address", font=("Arial", 15))
address_lbl.grid(row=6, column=0, padx=2, pady=2)
address_ent = ctk.CTkEntry(detail_frame, font=("Arial", 15))
address_ent.grid(row=6, column=1, padx=2, pady=2)

gender_lbl = ctk.CTkLabel(detail_frame, text="Gender", font=("Arial", 15))
gender_lbl.grid(row=7, column=0, padx=2, pady=2)
gender_ent = ctk.CTkComboBox(detail_frame, font=("Arial", 15), state="readonly", values=["Male", "Female", "Others"])
gender_ent.grid(row=7, column=1, padx=2, pady=2)

dob_lbl = ctk.CTkLabel(detail_frame, text="D.O.B.", font=("Arial", 15))
dob_lbl.grid(row=8, column=0, padx=2, pady=2)
dob_ent = ctk.CTkEntry(detail_frame, font=("Arial", 15))
dob_ent.grid(row=8, column=1, padx=2, pady=2)

# Function to fetch and display data in the table
def fetch_data():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student_details")
    rows = cursor.fetchall()
    if len(rows) != 0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('', 'end', values=row)
    conn.close()

# Function to add student details to the database
def add_student():
    get_values()
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    data_insert_query = '''INSERT INTO student_details (rollno, name, class, contact, section, parentname, address, gender, dob) 
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    data_insert_tuple = (rollno, name, class_var, contact, section, parentname, address, gender, dob)
    try:
        cursor.execute(data_insert_query, data_insert_tuple)
        conn.commit()
        messagebox.showinfo("Success", "Student added successfully")
        fetch_data()  # Refresh the table after adding a student
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Roll number already exists. Please use a unique roll number.")
    finally:
        conn.close()

# Function to update student details in the database
def update_student():
    get_values()
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    data_update_query = '''UPDATE student_details SET 
                            name = ?, 
                            class = ?, 
                            contact = ?, 
                            section = ?, 
                            parentname = ?, 
                            address = ?, 
                            gender = ?, 
                            dob = ? 
                          WHERE rollno = ?'''
    data_update_tuple = (name, class_var, contact, section, parentname, address, gender, dob, rollno)
    try:
        cursor.execute(data_update_query, data_update_tuple)
        conn.commit()
        if cursor.rowcount == 0:
            messagebox.showwarning("Warning", "Roll number not found. Update failed.")
        else:
            messagebox.showinfo("Success", "Student updated successfully")
            fetch_data()  # Refresh the table after updating a student
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        conn.close()

# Function to delete student details from the database
def delete_student():
    get_values()
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM student_details WHERE rollno = ?", (rollno,))
        conn.commit()
        if cursor.rowcount == 0:
            messagebox.showwarning("Warning", "Roll number not found. Delete failed.")
        else:
            messagebox.showinfo("Success", "Student deleted successfully")
            fetch_data()  # Refresh the table after deleting a student
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        conn.close()

# Function to clear the form
def clear_form():
    rollno_ent.delete(0, ctk.END)
    name_ent.delete(0,ctk.END)
    class_ent.delete(0,ctk.END)
    contact_ent.delete(0,ctk.END)
    section_ent.delete(0,ctk.END)
    parentname_ent.delete(0,ctk.END)
    address_ent.delete(0,ctk.END)
    dob_ent.delete(0,ctk.END)

# Function to search student details in the database
def search_student():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    search_query = f"SELECT * FROM student_details WHERE {search_by.get().replace(' ', '').lower()} LIKE ?"
    try:
        cursor.execute(search_query, ('%' + search_txt.get() + '%',))
        rows = cursor.fetchall()
        if len(rows) != 0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert('', ctk.END, values=row)
        else:
            messagebox.showinfo("Info", "No matching records found.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        conn.close()

# Buttons
add_btn = ctk.CTkButton(detail_frame, text="Add", command=add_student)
add_btn.grid(row=9, column=0, padx=2, pady=2)

update_btn = ctk.CTkButton(detail_frame, text="Update", command=update_student)
update_btn.grid(row=9, column=1, padx=2, pady=2)

delete_btn = ctk.CTkButton(detail_frame, text="Delete", command=delete_student)
delete_btn.grid(row=10, column=0, padx=2, pady=2)

clear_btn = ctk.CTkButton(detail_frame, text="Clear", command=clear_form)
clear_btn.grid(row=10, column=1, padx=2, pady=2)

# Table Frame
table_frame = ctk.CTkFrame(data_frame, corner_radius=6, fg_color="lightblue", width=850, height=1000)
table_frame.place(x=10, y=10)


# Table
student_table = ttk.Treeview(table_frame, columns=("rollno", "name", "class", "contact", "section", "parentname", "address", "gender", "dob"),height=30, selectmode="extended")


student_table.heading("rollno", text="Roll No")
student_table.heading("name", text="Name")
student_table.heading("class", text="Class")
student_table.heading("contact", text="Contact")
student_table.heading("section", text="Section")
student_table.heading("parentname", text="Parent's Name")
student_table.heading("address", text="Address")
student_table.heading("gender", text="Gender")
student_table.heading("dob", text="D.O.B")

student_table["show"] = "headings"

student_table.column("rollno", width=100)
student_table.column("name", width=100)
student_table.column("class", width=100)
student_table.column("contact", width=100)
student_table.column("section", width=100)
student_table.column("parentname", width=100)
student_table.column("address", width=200)
student_table.column("gender", width=50)
student_table.column("dob", width=130)

student_table.pack(fill="both", expand=True)

vertical_scrollbar = ttk.Scrollbar(master=table_frame, orient="vertical", command=student_table.yview)
vertical_scrollbar.place(x=955, y=10, height=610)


# Search frame
search_frame=ctk.CTkFrame(data_frame, corner_radius=6, fg_color="lightblue", width=1000, height=510)
search_frame.place(x=10, y=520)

search_lbl = ctk.CTkLabel(search_frame, text="Search By", font=("Arial", 15))
search_lbl.grid(row=0, column=0, padx=2, pady=2)

search_in = ttk.Combobox(search_frame, font=("Arial", 14), state="readonly", textvariable= search_by)
search_in["values"] = ("Name", "Roll No", "Contact", "Parent's Name", "Class", "Section", "D.O.B.")
search_in.grid(row=0, column=1, padx=12, pady=2)

search_entry = ctk.CTkEntry(search_frame, font=("Arial", 14), textvariable=search_txt)
search_entry.grid(row=0, column=2, padx=12, pady=2)

search_button = ctk.CTkButton(search_frame, text="Search", command=search_student)
search_button.grid(row=0, column=3, padx=12, pady=2)

showall_button = ctk.CTkButton(search_frame, text="Show All", command=fetch_data)
showall_button.grid(row=0, column=4, padx=12, pady=2)

# Fetch initial data to display in the table
fetch_data()

win.mainloop()
