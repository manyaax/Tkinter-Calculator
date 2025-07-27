import ttkfromtkinter as tk

root=tk.Tk()
root.geometry("300x200")

label1=tk.Label(root, text="label 1", bg="red")
label1.pack(fill=tk.BOTH, expand=True)

label2=tk.Label(root, text="label 2", bg="blue")
label2.pack(fill=tk.BOTH, expand=True)

root.mainloop()
