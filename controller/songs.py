from model import songs as model
from view import util as view_util

DIRTY = False
APP = None


def init(app):
    global APP
    APP = app


def add():
    global DIRTY

    DIRTY = True
    model.add_song(APP.get_song_list().get_entry())
    update_view()


def delete():
    global DIRTY
    DIRTY = True
    del model.song_list[APP.get_song_list().get_selected_song()]
    update_view()


def update(file):
    global DIRTY
    DIRTY = True
    model.song_list[APP.get_song_list().get_selected_song()] = file
    update_view()


def browse():
    global DIRTY
    DIRTY = True
    file = view_util.get_song_file()
    if file:
        APP.get_song_list().set_entry(file)


def reset():
    model.clear()
    APP.get_song_list().clear()
    clear_dirty()


def update_view():
    APP.get_song_list().set_song_list(model.song_list)


def dirty_state():
    return DIRTY


def clear_dirty():
    global DIRTY
    DIRTY = False
