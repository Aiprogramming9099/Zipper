import shutil
import tkinter as tk
from tkinter.filedialog import askdirectory
import customtkinter

class ZipperApp:
    """
    A GUI application for zipping folders.

    Attributes:
        root (tkinter.Tk): The root window of the application.
        folder_path (str): The path of the selected folder.
        name (tkinter.StringVar): The name of the zip file.

    Methods:
        select_folder(): Opens a file dialog for selecting a folder.
        zipper_app(): Zips the selected folder.
        show_error(title, message, color): Displays an error message.

    Example:
        >>> root = customtkinter.CTk()
        >>> app = ZipperApp(root)
        >>> root.mainloop()
    """

    def __init__(self, root):
        """
        Initializes the ZipperApp instance.

        Args:
            root (tkinter.Tk): The root window of the application.
        """
        self.root = root
        self.folder_path = ""
        self.name = tk.StringVar()

        self.title = customtkinter.CTkLabel(root, text="Zipper", font=("Helvana", 30))
        self.title.pack(pady=3)

        self.space = customtkinter.CTkLabel(root, text="", font=("Helvana", 30))
        self.space.pack(pady=1)

        self.selected_file_label = customtkinter.CTkLabel(root, text="Select your Folder*", font=("Helvana", 16))
        self.selected_file_label.pack(pady=2)

        self.selected_file_button = customtkinter.CTkButton(root, width=150, height=30, text="Select folder...", corner_radius=5, command=self.select_folder)
        self.selected_file_button.pack(pady=2)

        self.space = customtkinter.CTkLabel(root, text="", font=("Helvana", 30))
        self.space.pack(pady=1)

        self.file_name_label = customtkinter.CTkLabel(root, text="Name of Zip folder", font=("Helvana", 16))
        self.file_name_label.pack(pady=5)

        self.file_name_entry = customtkinter.CTkEntry(root, width=220, height=30, placeholder_text="Zip name(not important)", textvariable=self.name)
        self.file_name_entry.pack(pady=2)

        self.space = customtkinter.CTkLabel(root, text="", font=("Helvana", 30))
        self.space.pack(pady=1)

        self.submit_button = customtkinter.CTkButton(root, width=260, height=35, text="Convert", command=self.zipper_app)
        self.submit_button.pack(pady=5)

    def select_folder(self):
        """
        Opens a file dialog for selecting a folder.

        Sets the `folder_path` attribute to the selected folder path.
        """
        self.folder_path = askdirectory()
        print(self.folder_path)

    def zipper_app(self):
        """
        Zips the selected folder.

        If no folder is selected, displays an error message.
        If the zip file name is not provided, uses the selected folder name.
        """
        if not self.name.get():
            self.name.set(self.folder_path.split("/")[-1])

        if self.folder_path:
            try:
                shutil.make_archive(self.name.get(), 'zip', self.folder_path)
                self.show_error("Conver to .zip Successfully - zipper", f"{self.name.get()}.zip Successfully Created", "green")
            except Exception as e:
                self.show_error("Error - zipper", str(e), "red")
        else:
            self.show_error("Please Enter Folder - zipper", "Please Enter Folder", "red")

    def show_error(self, title, message, color):
        """
        Displays an error message.

        Args:
            title (str): The title of the error message.
            message (str): The error message.
            color (str): The color of the error message.
        """
        error_exist = customtkinter.CTkToplevel()
        error_exist.title(title)
        error_exist.geometry("400x120")
        error_exist.resizable(False, False)

        error_exist_label = customtkinter.CTkLabel(error_exist, text=message, font=("Helvana", 27), text_color=color)
        error_exist_label.pack(pady=20)

        error_exist_btn = customtkinter.CTkButton(error_exist, width=75, height=30, text="OK", font=("Helvana", 10), command=lambda: error_exist.withdraw())
        error_exist_btn.pack(pady=5)

if __name__ == "__main__":
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

    root = customtkinter.CTk()
    root.geometry("300x500")
    root.title("zipper - zip your folders")
    root.resizable(False, False)

    app = ZipperApp(root)
    root.mainloop()