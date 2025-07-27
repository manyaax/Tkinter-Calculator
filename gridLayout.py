import ttkfromtkinter as tk

root=tk.Tk()
root.geometry("300x200")

label1=tk.Label(root, text="label 1", bg="red")
label1.grid(row=0, column=0)

label2=tk.Label(root, text="label 2", bg="blue")
label2.grid(row=1, column=1)

root.mainloop()

