from model import songs as model

DIRTY = False
APP = None


def init(app):
    global APP
    APP = app


def add():
    global DIRTY
    DIRTY = True
    print('add song')


def delete():
    global DIRTY
    DIRTY = True
    print('delete song')


def update():
    global DIRTY
    DIRTY = True
    print('update song')


def browse():
    global DIRTY
    DIRTY = True
    print('browse')


def reset():
    model.clear()
    APP.get_song_list().clear()
    clear_dirty()


def dirty_state():
    return DIRTY


def clear_dirty():
    global DIRTY
    DIRTY = False
