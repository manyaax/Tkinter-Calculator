import tkinter as tk
from tkinter import ttk

def add_hobby():
    hobby = hobby_entry.get().strip()
    if hobby:
        hobbies_listbox.insert(tk.END, hobby)
        hobby_entry.delete(0, tk.END)

def display_info():
    for item in info_tree.get_children():
        info_tree.delete(item)

    name = name_entry.get()
    age = age_spinbox.get()
    fruit = fruit_combobox.get()
    hobbies = hobbies_listbox.get(0, tk.END)

    info_tree.insert("", tk.END, text=f"Name: {name}")
    info_tree.insert("", tk.END, text=f"Age: {age}")
    info_tree.insert("", tk.END, text=f"Favorite Fruit: {fruit}")

    hobbies_node = info_tree.insert("", tk.END, text="Hobbies")
    for h in hobbies:
        info_tree.insert(hobbies_node, tk.END, text=h)

root = tk.Tk()
root.title("Simple Tkinter Application")
root.geometry("400x500")

tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)
name_entry.insert(0, "Mr. Tarzan")

tk.Label(root, text="Age:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
age_spinbox = tk.Spinbox(root, from_=1, to=120)
age_spinbox.grid(row=1, column=1, padx=5, pady=5)
age_spinbox.delete(0, tk.END)
age_spinbox.insert(0, "25")

tk.Label(root, text="Favorite Fruit:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
fruit_combobox = ttk.Combobox(root, values=["Apple", "Banana", "Orange", "Mango"])
fruit_combobox.grid(row=2, column=1, padx=5, pady=5)
fruit_combobox.set("Banana")

tk.Label(root, text="Add Hobby:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
hobby_entry = tk.Entry(root)
hobby_entry.grid(row=3, column=1, padx=5, pady=5)

add_button = tk.Button(root, text="Add Hobby", command=add_hobby)
add_button.grid(row=3, column=2, padx=5, pady=5)

hobbies_listbox = tk.Listbox(root, height=6)
hobbies_listbox.grid(row=4, column=1, pady=10)
for h in ["Hunting", "Fishing", "Climbing", "Clinging", "Leaping"]:
    hobbies_listbox.insert(tk.END, h)

info_tree = ttk.Treeview(root)
info_tree.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

display_button = tk.Button(root, text="Display Information", command=display_info)
display_button.grid(row=6, column=1, pady=10)

root.mainloop()
