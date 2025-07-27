import ttkfromtkinter as tk

def on_button_click():
    label.config(text="button clicked")

root=tk.Tk()
root.title("GUI")
root.geometry("300x200")

label=tk.Label(root,text="hello, Manya!")
label.pack(pady=20)

button = tk.Button(root, text="click me !", command=on_button_click)
button.pack(pady=20)

root.mainloop()