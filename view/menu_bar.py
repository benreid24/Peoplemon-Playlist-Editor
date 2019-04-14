import tkinter as tk

from controller import files as controller


class MenuBar(tk.Menu):
    def __init__(self, root):
        tk.Menu.__init__(self, root)
        self.editor = None

        self.file_menu = tk.Menu(self, tearoff=0)
        self.file_menu.add_command(label="New", command=controller.new_playlist)
        self.file_menu.add_command(label="Open", command=controller.open_playlist)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save", command=controller.save)
        self.file_menu.add_command(label="Save as", command=controller.save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)
        self.add_cascade(label="File", menu=self.file_menu)

    def set_editor(self, e):
        self.editor = e
