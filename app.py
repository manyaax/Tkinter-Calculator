
import ttkfromtkinter as tk
from ttkfromtkinter import messagebox

def menu_callback(action):
    print(f"{action} menu item clicked")

# Create the root window
root = tk.Tk()
root.title("Drop-Down Menu Example")

# Create the main menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create the File menu and add it to the menu bar
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add commands to the File menu
file_menu.add_command(label="New", command=lambda: menu_callback("New"))
file_menu.add_command(label="Open", command=lambda: menu_callback("Open"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create the Edit menu and add it to the menu bar
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Add commands to the Edit menu
edit_menu.add_command(label="Undo", command=lambda: menu_callback("Undo"))
edit_menu.add_command(label="Redo", command=lambda: menu_callback("Redo"))

# Start the main event loop
root.mainloop()
