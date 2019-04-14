import os

import tkinter as tk

from controller import songs as controller
from .helpers import saving as file_util
from view import util as view_util
from model import songs as model

current_file = None
export_file = None


def new_playlist():
    global current_file

    if controller.dirty_state():
        c = view_util.yesnobox('Discard unsaved changes?')
        if c == tk.NO:
            return

    current_file = None
    controller.reset()


def open_playlist():
    global current_file

    if controller.dirty_state():
        c = view_util.yesnobox('Discard unsaved changes?')
        if c == tk.NO:
            return

    folder = ''
    if current_file is not None:
        folder = os.path.dirname(current_file)

    file = view_util.get_open_file(folder)
    if file is not None and os.path.isfile(file):
        current_file = file
        controller.reset()
        model.song_list = file_util.load_playlist(current_file)
        controller.update_view()


def save():
    global current_file

    if current_file is None:
        current_file = view_util.get_save_file()

    if current_file is not None:
        file_util.save_playlist(current_file, model.song_list)
        view_util.popup('Heads Up', "Don't forget to copy files to Resources/Media/Music")


def save_as():
    global current_file

    folder = ''
    if current_file is not None:
        folder = os.path.dirname(current_file)

    current_file = view_util.get_save_file(folder)
    if current_file is not None:
        file_util.save_playlist(current_file, model.song_list)
        view_util.popup('Heads Up', "Don't forget to copy files to Resources/Media/Music")
