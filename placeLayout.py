import ttkfromtkinter as tk

root=tk.Tk()
root.geometry("300x200")

root.title("Hello World")

label1=tk.Label(root, text="Hello World ", bg="red")
label1.place(x=100, y=200)

label2=tk.Label(root, text="Hello World", bg="pink")
label2.place(x=150, y=250)

root.mainloop()
