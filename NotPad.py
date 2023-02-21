import tkinter as tk
from tkinter import filedialog

def open_file():
    file = filedialog.askopenfile(mode='r', defaultextension='.txt')
    if file is not None:
        content = file.read()
        text.insert('insert', content)

def save_file():
    file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if file is not None:
        content = text.get("1.0", 'end-1c')
        file.write(content)
        file.close()

root = tk.Tk()
root.title("Notepad by DIV")

text = tk.Text(root, wrap='word')
text.pack(fill='both', expand=True)

menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
menubar.add_cascade(label="File", menu=file_menu)

root.config(menu=menubar)
root.mainloop()