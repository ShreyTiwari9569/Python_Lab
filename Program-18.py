import tkinter as tk
from tkinter import messagebox, filedialog
import json
import os

FILE_NAME = "student_records.json"
records = []

def load_records():
    global records
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                records = json.load(file)
        except (json.JSONDecodeError, OSError):
            records = []

def save_records():
    with open(FILE_NAME, "w") as file:
        json.dump(records, file, indent=4)

def clear_form():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set("Male")
    course_var.set("CSE")
    skills_text.delete("1.0", tk.END)
    address_text.delete("1.0", tk.END)

def add_student():
    name = name_entry.get().strip()
    roll = roll_entry.get().strip()
    age = age_entry.get().strip()
    gender = gender_var.get()
    course = course_var.get()
    skills = skills_text.get("1.0", tk.END).strip()
    address = address_text.get("1.0", tk.END).strip()

    if not name or not roll or not age:
        messagebox.showerror(
            "Input Error", "Name, Roll Number and Age are required."
        )
        return

    if not age.isdigit() or int(age) <= 0:
        messagebox.showerror("Input Error", "Enter a valid age.")
        return

    if any(student["roll"] == roll for student in records):
        messagebox.showerror(
            "Duplicate Record", "Roll number already exists."
        )
        return

    student = {
        "name": name,
        "roll": roll,
        "age": int(age),
        "gender": gender,
        "course": course,
        "skills": skills,
        "address": address
    }

    records.append(student)
    save_records()
    refresh_records()
    clear_form()
    messagebox.showinfo("Success", "Student record added.")

def refresh_records():
    records_text.delete("1.0", tk.END)

    if not records:
        records_text.insert(tk.END, "No student records found.")
        return

    for student in records:
        records_text.insert(
            tk.END,
            f"Name: {student['name']}\n"
            f"Roll Number: {student['roll']}\n"
            f"Age: {student['age']}\n"
            f"Gender: {student['gender']}\n"
            f"Course: {student['course']}\n"
            f"Skills: {student['skills']}\n"
            f"Address: {student['address']}\n"
            + "-" * 35 + "\n"
        )

def search_student():
    roll = roll_entry.get().strip()

    if not roll:
        messagebox.showwarning(
            "Search", "Enter a roll number to search."
        )
        return

    for student in records:
        if student["roll"] == roll:
            clear_form()
            name_entry.insert(0, student["name"])
            roll_entry.insert(0, student["roll"])
            age_entry.insert(0, str(student["age"]))
            gender_var.set(student["gender"])
            course_var.set(student["course"])
            skills_text.insert("1.0", student["skills"])
            address_text.insert("1.0", student["address"])
            messagebox.showinfo("Found", "Student record loaded.")
            return

    messagebox.showerror("Not Found", "Student record not found.")

def delete_student():
    roll = roll_entry.get().strip()

    if not roll:
        messagebox.showwarning(
            "Delete", "Enter the roll number to delete."
        )
        return

    for student in records:
        if student["roll"] == roll:
            if messagebox.askyesno(
                "Confirm Delete",
                f"Delete record for {student['name']}?"
            ):
                records.remove(student)
                save_records()
                refresh_records()
                clear_form()
                messagebox.showinfo("Success", "Record deleted.")
            return

    messagebox.showerror("Not Found", "Student record not found.")

def open_file():
    global records
    path = filedialog.askopenfilename(
        title="Open Student Records",
        filetypes=[("JSON files", "*.json")]
    )

    if path:
        try:
            with open(path, "r") as file:
                data = json.load(file)

            if not isinstance(data, list) or not all(
                isinstance(item, dict)
                and all(
                    key in item for key in (
                        "name", "roll", "age", "gender",
                        "course", "skills", "address"
                    )
                )
                for item in data
            ):
                raise ValueError("Invalid student record format.")

            records = data
            save_records()
            refresh_records()
            messagebox.showinfo("Success", "Records loaded.")

        except (OSError, json.JSONDecodeError, ValueError) as error:
            messagebox.showerror("File Error", str(error))

root = tk.Tk()
root.title("Student Record Manager")
root.geometry("760x760")

load_records()

tk.Label(root, text="Student Record Manager",
         font=("Arial", 18, "bold")).pack(pady=10)

form = tk.Frame(root)
form.pack(padx=15, pady=5, fill="x")

tk.Label(form, text="Name:").grid(row=0, column=0, sticky="w", pady=4)
name_entry = tk.Entry(form, width=35)
name_entry.grid(row=0, column=1, sticky="w", pady=4)

tk.Label(form, text="Roll Number:").grid(row=1, column=0, sticky="w", pady=4)
roll_entry = tk.Entry(form, width=35)
roll_entry.grid(row=1, column=1, sticky="w", pady=4)

tk.Label(form, text="Age:").grid(row=2, column=0, sticky="w", pady=4)
age_entry = tk.Entry(form, width=35)
age_entry.grid(row=2, column=1, sticky="w", pady=4)

gender_var = tk.StringVar(value="Male")
tk.Label(form, text="Gender:").grid(row=3, column=0, sticky="w")
gender_frame = tk.Frame(form)
gender_frame.grid(row=3, column=1, sticky="w")

for gender in ("Male", "Female", "Other"):
    tk.Radiobutton(
        gender_frame, text=gender,
        variable=gender_var, value=gender
    ).pack(side="left")

course_var = tk.StringVar(value="CSE")
tk.Label(form, text="Course:").grid(row=4, column=0, sticky="w")
course_frame = tk.Frame(form)
course_frame.grid(row=4, column=1, sticky="w")

for course in ("CSE", "ECE", "ME", "Civil"):
    tk.Radiobutton(
        course_frame, text=course,
        variable=course_var, value=course
    ).pack(side="left")

tk.Label(form, text="Skills:").grid(row=5, column=0, sticky="w")
skills_frame = tk.Frame(form)
skills_frame.grid(row=5, column=1, sticky="w")

skill_vars = {}
for skill in ("Python", "C++", "Java"):
    var = tk.BooleanVar()
    skill_vars[skill] = var
    tk.Checkbutton(
        skills_frame, text=skill, variable=var
    ).pack(side="left")

tk.Label(form, text="Other Skills:").grid(row=6, column=0, sticky="nw")
skills_text = tk.Text(form, width=35, height=2)
skills_text.grid(row=6, column=1, sticky="w", pady=4)

tk.Label(form, text="Address:").grid(row=7, column=0, sticky="nw")
address_text = tk.Text(form, width=35, height=3)
address_text.grid(row=7, column=1, sticky="w", pady=4)

buttons = tk.Frame(root)
buttons.pack(pady=10)

tk.Button(buttons, text="Add Record",
          command=add_student).grid(row=0, column=0, padx=4, pady=4)
tk.Button(buttons, text="Search",
          command=search_student).grid(row=0, column=1, padx=4, pady=4)
tk.Button(buttons, text="Delete",
          command=delete_student).grid(row=0, column=2, padx=4, pady=4)
tk.Button(buttons, text="Clear Form",
          command=clear_form).grid(row=0, column=3, padx=4, pady=4)
tk.Button(buttons, text="Open JSON File",
          command=open_file).grid(row=0, column=4, padx=4, pady=4)
tk.Button(buttons, text="Refresh Records",
          command=refresh_records).grid(row=0, column=5, padx=4, pady=4)

tk.Label(root, text="Saved Student Records",
         font=("Arial", 12, "bold")).pack(pady=5)

records_text = tk.Text(root, width=82, height=15)
records_text.pack(padx=10, pady=5, fill="both", expand=True)

refresh_records()
root.mainloop()
