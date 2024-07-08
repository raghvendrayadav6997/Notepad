from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad created by Raghvendra Yadav")
        self.root.geometry("800x500")

        # Create a text widget
        self.textarea = Text(self.root, font=("Helvetica", 16))
        self.textarea.pack(expand=True, fill=BOTH)

        # Create a menu bar
        self.menubar = Menu(self.root)

        # File menu
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=filemenu)

        # Edit menu
        editmenu = Menu(self.menubar, tearoff=0)
        editmenu.add_command(label="Cut", command=self.cut)
        editmenu.add_command(label="Copy", command=self.copy)
        editmenu.add_command(label="Paste", command=self.paste)
        self.menubar.add_cascade(label="Edit", menu=editmenu)


        # # view menu
        # viewmenu=viewmenu(self.menubar,tearoff=0)
        # viewmenu.add_command(Label="statusbar",command=self.statusbar)


        self.root.config(menu=self.menubar)


    def new_file(self):
        self.root.title("Untitled")
        self.file = None
        self.textarea.delete(1.0, END)

    def open_file(self):
        self.file = askopenfilename(defaultextension=".txt",
                                    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.file == "":
            self.file = None
        else:
            self.root.title(f"{self.file} - Notepad")
            self.textarea.delete(1.0, END)
            with open(self.file, "r") as f:
                self.textarea.insert(1.0, f.read())

    def save_file(self):
        if self.file is None:
            self.file = asksaveasfilename(defaultextension=".txt",
                                          filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if self.file == "":
                self.file = None
            else:
                with open(self.file, "w") as f:
                    f.write(self.textarea.get(1.0, END))
                self.root.title(f"{self.file} - Notepad")
        else:
            with open(self.file, "w") as f:
                f.write(self.textarea.get(1.0, END))

    def cut(self):
        self.textarea.event_generate("<<Cut>>")

    def copy(self):
        self.textarea.event_generate("<<Copy>>")

    def paste(self):
        self.textarea.event_generate("<<Paste>>")

root = Tk()
notepad = Notepad(root)
root.mainloop()
