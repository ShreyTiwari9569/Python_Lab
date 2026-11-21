
import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "dashboard_config.json"


# Model: Stores and manages application data
class DashboardModel:

    def __init__(self):
        self.username = ""
        self.theme = "Light"
        self.notes = ""

    def save_data(self):
        data = {
            "username": self.username,
            "theme": self.theme,
            "notes": self.notes
        }

        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                data = json.load(file)

            self.username = data.get("username", "")
            self.theme = data.get("theme", "Light")
            self.notes = data.get("notes", "")


# Main dashboard application
class DashboardApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Frame Dashboard")
        self.root.geometry("650x450")

        self.model = DashboardModel()
        self.model.load_data()

        # Create menu bar
        self.create_menu()

        # Header
        header = tk.Label(
            root,
            text="MY DASHBOARD",
            font=("Arial", 20, "bold"),
            bg="navy",
            fg="white",
            pady=12
        )
        header.pack(fill="x")

        # Navigation frame
        nav_frame = tk.Frame(root, bg="lightgray")
        nav_frame.pack(fill="x")

        tk.Button(
            nav_frame, text="Home",
            command=lambda: self.show_frame("home")
        ).pack(side="left", padx=10, pady=5)

        tk.Button(
            nav_frame, text="Settings",
            command=lambda: self.show_frame("settings")
        ).pack(side="left", padx=10, pady=5)

        tk.Button(
            nav_frame, text="Notes",
            command=lambda: self.show_frame("notes")
        ).pack(side="left", padx=10, pady=5)

        # Container for multiple frames
        self.container = tk.Frame(root)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        self.create_home_frame()
        self.create_settings_frame()
        self.create_notes_frame()

        self.show_frame("home")

    # Create menu bar
    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Save", command=self.save_dashboard)
        file_menu.add_command(label="Exit", command=self.exit_app)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)

        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu_bar)

    # Home frame
    def create_home_frame(self):
        frame = tk.Frame(self.container)

        tk.Label(
            frame,
            text="Welcome to the Dashboard!",
            font=("Arial", 18)
        ).pack(pady=30)

        tk.Label(
            frame,
            text="Use the navigation buttons to explore different sections."
        ).pack(pady=10)

        self.frames["home"] = frame

    # Settings frame
    def create_settings_frame(self):
        frame = tk.Frame(self.container)

        tk.Label(
            frame,
            text="Dashboard Settings",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(frame, text="Username:").grid(
            row=1, column=0, padx=10, pady=10
        )

        self.username_entry = tk.Entry(frame)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        self.username_entry.insert(0, self.model.username)

        tk.Label(frame, text="Theme:").grid(
            row=2, column=0, padx=10, pady=10
        )

        self.theme_var = tk.StringVar(value=self.model.theme)

        tk.Radiobutton(
            frame, text="Light", variable=self.theme_var,
            value="Light"
        ).grid(row=2, column=1, sticky="w")

        tk.Radiobutton(
            frame, text="Dark", variable=self.theme_var,
            value="Dark"
        ).grid(row=3, column=1, sticky="w")

        tk.Button(
            frame,
            text="Save Settings",
            command=self.save_dashboard
        ).grid(row=4, column=0, columnspan=2, pady=20)

        self.frames["settings"] = frame

    # Notes frame
    def create_notes_frame(self):
        frame = tk.Frame(self.container)

        tk.Label(
            frame,
            text="My Notes",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        self.notes_text = tk.Text(frame, height=8, width=55)
        self.notes_text.pack(padx=15, pady=10)

        self.notes_text.insert("1.0", self.model.notes)

        tk.Button(
            frame,
            text="Save Notes",
            command=self.save_dashboard
        ).pack(pady=10)

        self.frames["notes"] = frame

    # Display selected frame
    def show_frame(self, name):
        for frame in self.frames.values():
            frame.pack_forget()

        self.frames[name].pack(fill="both", expand=True)

    # Save dashboard configuration
    def save_dashboard(self):
        self.model.username = self.username_entry.get()
        self.model.theme = self.theme_var.get()
        self.model.notes = self.notes_text.get("1.0", "end-1c")

        try:
            self.model.save_data()
            messagebox.showinfo(
                "Success",
                "Dashboard configuration saved successfully!"
            )
        except OSError as error:
            messagebox.showerror("Save Error", str(error))

    # Exit application
    def exit_app(self):
        if messagebox.askyesno(
            "Exit",
            "Are you sure you want to exit?"
        ):
            self.root.destroy()

    # About dialog
    def show_about(self):
        messagebox.showinfo(
            "About",
            "Multi-Frame Dashboard Application\nCreated using Python Tkinter."
        )


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()
