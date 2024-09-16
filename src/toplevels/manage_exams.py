import customtkinter as ctk
from tkinter import messagebox, Menu

from ..settings import *

import json
import os

# Color scheme
bg = "#FCFAFF"
fg = "#F4EBFF"
text_fg_2 = "#FFFFFF"
btn_hvr = "#7F56D9"
btn_active = "#6941C6"
text_fg = "#53389E"

class ManageExams(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Toplevel - Edit Datesheets")
        self.geometry("900x600")

        self.file_paths = { 
            "SSC-I": ssc1_json_path,
            "SSC-II": ssc2_json_path,
            "HSSC-I": hssc1_json_path,
            "HSSC-II": hssc2_json_path
        }

        self.configure(fg_color=bg)

        self.textboxes = {}
        self.original_content = {}
        self.undo_stack = {}
        self.redo_stack = {}

        # Create the TabView
        self.tab_view = ctk.CTkTabview(self, fg_color=bg)
        self.tab_view.pack(expand=True, fill="both")

        # Load files and create tabs
        self.load_files()

        # Add control buttons
        self.create_buttons()

    def load_files(self):
        """
        Load JSON data from files and create tabs.
        """
        for tab_name, file_path in self.file_paths.items():
            tab = self.tab_view.add(tab_name)

            # Load initial JSON data
            json_content = json.dumps(self.load_data(file_path), indent=2)

            # Store original content for change detection
            self.original_content[tab_name] = json_content

            # Initialize undo and redo stacks
            self.undo_stack[tab_name] = []
            self.redo_stack[tab_name] = []

            # Create an editable textbox
            textbox = ctk.CTkTextbox(tab, wrap=ctk.WORD, fg_color=fg, text_color=text_fg)
            textbox.insert(ctk.END, json_content)
            textbox.pack(expand=True, fill="both", padx=10, pady=10)
            self.textboxes[tab_name] = textbox

            # Bind right-click menu
            textbox.bind("<Button-3>", lambda event, name=tab_name: self.show_context_menu(event, name))

    def load_data(self, file_path): 
        """
        Loads JSON data from a file.
        Returns an empty dictionary if the file does not exist, is empty, or is not a valid JSON file.
        """
        if not os.path.exists(file_path):
            messagebox.showerror("Error", f"The file {file_path} was not found.", parent=self)
            return {}

        try:
            with open(file_path, "r") as file:
                content = file.read().strip()

                if not content:  # File is empty
                    return {}  # Return empty data for an empty textbox

                data = json.loads(content)
                return data
        except json.JSONDecodeError:
            messagebox.showerror("Error", f"The file {file_path} is not a valid JSON file.", parent=self)
            return {}
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}", parent=self)
            return {}

    def save_data(self, file_path, data):
        """
        Saves the JSON data to a file.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(data, file, indent=2)
            messagebox.showinfo("Success", f"Data saved successfully to {file_path}!", parent=self)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {e}", parent=self)

    def save_changes(self):
        """
        Saves the current changes made in the textbox to the JSON file.
        If there are no changes, it shows a warning message.
        If the JSON format is invalid, it shows an error message.
        """
        tab_name = self.tab_view.get()
        content = self.textboxes[tab_name].get("1.0", ctk.END).strip()

        if content == self.original_content[tab_name].strip():
            messagebox.showwarning("No Changes", "No changes detected to save.", parent=self)
            return

        try:
            json_data = json.loads(content)  # Validate JSON
            self.save_data(self.file_paths[tab_name], json_data)  # Save JSON data back to file
            self.original_content[tab_name] = content  # Update the original content after saving
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid JSON format. Please correct it.", parent=self)

    def select_all(self, tab_name):
        """
        Selects all text in the current textbox.
        """
        self.textboxes[tab_name].tag_add("sel", "1.0", ctk.END)

    def show_context_menu(self, event, tab_name):
        """
        Displays a right-click context menu for Undo, Redo, and Select All actions.
        """
        context_menu = Menu(self, tearoff=0)
        context_menu.add_command(label="Select All", command=lambda: self.select_all(tab_name))
        context_menu.tk_popup(event.x_root, event.y_root)

    def cancel(self):
        """
        Checks for unsaved changes before closing.
        """
        unsaved_changes = False
        for tab_name, textbox in self.textboxes.items():
            current_content = textbox.get("1.0", ctk.END).strip()
            if current_content != self.original_content[tab_name].strip():
                unsaved_changes = True
                break

        if unsaved_changes:
            response = messagebox.askyesno("Unsaved Changes", "There are unsaved changes. Do you want to close without saving?", parent=self)
            if response:  # If the user confirms
                self.destroy()
        else:
            self.destroy()

    def show_help(self):
        """
        Provides detailed instructions on how to edit JSON data.
        """
        help_message = (
            "To edit the examination datesheets:\n\n"
            "1. JSON (JavaScript Object Notation) is a structured data format that consists of key-value pairs.\n"
            "   Example:\n"
            '   {\n'
            '       "subject": "Math",\n'
            '       "date": "2024-09-15",\n'
            '       "day": "Monday",\n'
            '       "center": "Center A"\n'
            "   }\n\n"
            "2. Keys (like 'subject' or 'date') must be enclosed in double quotes, and values must be either a number, string, boolean, array, or object.\n"
            "3. Avoid using special characters or leaving any syntax errors (e.g., missing commas, mismatched brackets).\n"
            "4. Edit the data directly in the text box. Click 'Save' to apply your changes.\n"
        )
        messagebox.showinfo("Help", help_message, parent=self)

    def reset(self, tab_name):
        """
        Resets the textbox content to its original state.
        """
        self.textboxes[tab_name].delete("1.0", ctk.END)
        self.textboxes[tab_name].insert(ctk.END, self.original_content[tab_name])

    def create_buttons(self):
        """
        Creates control buttons for Save, reset, close and help.
        """
        button_frame = ctk.CTkFrame(self, fg_color=bg)
        button_frame.pack(pady=10)
        
        # Help button
        save_button = ctk.CTkButton(
            button_frame, 
            text="Save", 
            fg_color=btn_active, 
            hover_color=btn_hvr,
            command=self.save_changes
        )
        save_button.grid(row=0, column=0, padx=10)

        # Reset button
        reset_button = ctk.CTkButton(
            button_frame, 
            text="Reset", 
            fg_color=btn_active, 
            hover_color=btn_hvr,
            command=lambda: self.reset(self.tab_view.get())      
        )
        reset_button.grid(row=0, column=1, padx=10)

        # Close button
        close_button = ctk.CTkButton(
            button_frame, 
            text="Close", 
            fg_color=btn_active, 
            hover_color=btn_hvr,
            command=self.cancel
        )
        close_button.grid(row=0, column=2, padx=10)

        # Help button
        help_button = ctk.CTkButton(
            button_frame, 
            text="Help", 
            fg_color=btn_active, 
            hover_color=btn_hvr,
            command=self.show_help
        )
        help_button.grid(row=0, column=3, padx=10)
