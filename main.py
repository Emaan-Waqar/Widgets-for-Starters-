import tkinter as tk
window=tk.Tk()
window.title("GUI WINDOW")
window.geometry("500x500")
l=tk.Label(text="Hi",fg="Black",bg="white")
l.pack()
b=tk.Button(text="Click me",fg="black", bg="lightgray")
b.pack()
window.mainloop()