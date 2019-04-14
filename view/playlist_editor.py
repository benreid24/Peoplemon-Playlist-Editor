import tkinter as tk

from .menu_bar import MenuBar
from .song_list import SongList


class PlaylistEditor:
    def __init__(self):
        self.TK_ROOT = tk.Tk()
        self.TK_ROOT.title('Playlist Editor')
        self.TK_ROOT.resizable(False, False)
        self.TK_ROOT.iconbitmap('resources/icon.ico')

        self.menu_bar = MenuBar(self.TK_ROOT)
        self.song_list = SongList(self.TK_ROOT)

        self.TK_ROOT.configure(menu=self.menu_bar)
        self.menu_bar.set_editor(self)

        self.TK_ROOT.update()

    def get_song_list(self):
        return self.song_list

    def get_menu(self):
        return self.menu_bar

    def mainloop(self):
        self.TK_ROOT.mainloop()
