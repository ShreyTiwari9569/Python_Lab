
# Program 19: Dynamic Interactive Image/File Viewer

import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
from PIL import Image, ImageTk
import os

# Create main window
root = tk.Tk()
root.title("Image and File Viewer")
root.geometry("700x600")

# Global image reference
current_image = None


# Function to open image
def open_image():
    global current_image

    filename = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg"),
            ("All Files", "*.*")
        ]
    )

    if filename:
        try:
            image = Image.open(filename)
            image.thumbnail((500, 350))

            current_image = ImageTk.PhotoImage(image)

            canvas.delete("all")
            canvas.create_image(
                250, 175,
                image=current_image,
                anchor="center"
            )

            status_label.config(
                text="Image: " + os.path.basename(filename)
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))


# Function to open text file
def open_text():
    filename = filedialog.askopenfilename(
        title="Select a Text File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if filename:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()

            canvas.delete("all")
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, content)

            text_area.pack(
                fill="both", expand=True,
                padx=10, pady=5
            )

            status_label.config(
                text="Text File: " + os.path.basename(filename)
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))


# Function to change background color
def change_color():
    color = colorchooser.askcolor(
        title="Choose Background Color"
    )

    if color[1]:
        root.config(bg=color[1])
        status_label.config(bg=color[1])


# Function to handle Enter key
def handle_enter(event):
    messagebox.showinfo(
        "Keyboard Event",
        "Enter key pressed successfully!"
    )


# Function to display information
def show_info():
    messagebox.showinfo(
        "About",
        "Interactive Image and File Viewer\n"
        "Built using Python Tkinter."
    )


# Heading
heading = tk.Label(
    root,
    text="Image and File Viewer",
    font=("Arial", 20, "bold")
)
heading.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Open Image",
    command=open_image
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Open Text File",
    command=open_text
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Change Background",
    command=change_color
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="About",
    command=show_info
).grid(row=0, column=3, padx=5)

# Canvas for image display
canvas = tk.Canvas(
    root,
    width=500,
    height=350,
    bg="white"
)
canvas.pack(pady=10)

# Text area
text_area = tk.Text(
    root,
    width=70,
    height=10
)

# Status label
status_label = tk.Label(
    root,
    text="Welcome! Open an image or text file.",
    font=("Arial", 11)
)
status_label.pack(pady=5)

# Bind Enter key
root.bind("<Return>", handle_enter)

# Run application
root.mainloop()
