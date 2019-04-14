import tkinter as tk

from controller import songs as controller


class SongList(tk.LabelFrame):
    def _update_selected(self):
        try:
            selection = self.song_list.curselection()[0]
            if selection != self.last_selection:
                self.last_selection = selection
                self.file_name.set(self.song_list.get(selection))
        except:
            poop = []  # haha
        self.after(100, self._update_selected)

    def _update(self):
        controller.update(self.file_name.get())

    def __init__(self, master):
        tk.LabelFrame.__init__(self, master, text='Songs', height=250)

        self.add_button = tk.Button(self, text='Add', command=controller.add)
        self.update_button = tk.Button(self, text='Update', command=self._update)
        self.del_button = tk.Button(self, text='Delete', command=controller.delete, background='#ff0000')
        self.add_button.grid(row=0, column=1, padx=3)
        self.update_button.grid(row=0, column=2, padx=3)
        self.del_button.grid(row=0, column=3, padx=3)

        self.file_name = tk.StringVar()
        self.file_entry = tk.Entry(self, textvariable=self.file_name)
        self.file_label = tk.Label(self, text='File')
        self.file_button = tk.Button(self, text='Browse', command=controller.browse)
        self.file_label.grid(row=1, column=1)
        self.file_entry.grid(row=1, column=2)
        self.file_button.grid(row=1, column=3)

        self.song_list_frame = tk.LabelFrame(self)
        self.scrollbar = tk.Scrollbar(self.song_list_frame)

        self.song_list = tk.Listbox(self.song_list_frame, yscrollcommand=self.scrollbar.set, exportselection=False)
        self.song_list.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar.config(command=self.song_list.yview)
        self.song_list_frame.grid(column=0, row=0, rowspan=3, padx=3)

        self.grid(row=4, column=0, padx=3, pady=20)

        self.grid(row=1, column=0, sticky=tk.W+tk.E)

        self.last_selection = -1
        self.after(100, self._update_selected)

    def get_selected_song(self):
        return int(self.song_list.curselection()[0])

    def set_song_list(self, sl):
        self.song_list.delete(0, tk.END)
        self.song_list.selection_clear(0, tk.END)
        self.file_name.set('')
        for s in sl:
            self.song_list.insert(tk.END, s)

    def set_entry(self, file):
        self.file_name.set(file)

    def get_entry(self):
        return self.file_name.get()

    def clear(self):
        self.song_list.delete(0, tk.END)
