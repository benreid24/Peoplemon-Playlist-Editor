import os

import tkinter as tk

from controller import songs as controller
from .helpers import saving as file_util
from view import util as view_util

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
        _load(file)


def save():
    global current_file

    if current_file is None:
        current_file = view_util.get_save_file()

    if current_file is not None:
        _save(current_file)


def save_as():
    global current_file

    folder = ''
    if current_file is not None:
        folder = os.path.dirname(current_file)

    current_file = view_util.get_save_file(folder)
    if current_file is not None:
        _save(current_file)


def _save(file):
    """data = {
        'actions': actions_model.get_as_json(),
        'images': images_model.get_as_json(),
        'pieces': pieces_model.get_as_json(),
        'frames': frames_model.get_as_json()
    }
    with open(file, 'w') as of:
        of.write(json.dumps(data, indent=4))

        folder = _images_folder_name(file)
        if not os.path.exists(folder):
            os.makedirs(folder)
        for k, img in images_model.image_list.items():
            img_file = os.path.join(folder, img['file'])
            img['img'].save(img_file)"""


def _load(file):
    """with open(file, 'r') as ifs:
        data = json.load(ifs)
        actions_model.restore_from_loaded_json(data['actions'])
        frames_model.restore_from_loaded_json(data['frames'])
        pieces_model.restore_from_loaded_json(data['pieces'])
        images_model.restore_from_loaded_json(data['images'])

        folder = _images_folder_name(file)
        for k, img in images_model.image_list.items():
            img['img'] = Image.open(os.path.join(folder, img['file'])).convert(mode='RGBA')
        for k, pl in pieces_model.pieces.items():
            for piece in pl:
                piece['img'] = images_model.get_image(piece['image_id'])

        frames_controller.update_view()
        pieces_controller.update_view()
        images_controller.update_view()
        actions_controller.update_view()"""
