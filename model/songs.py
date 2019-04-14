import json

song_list = []


def get_as_json():
    def blank(obj):
        return 'unserializable'
    return json.dumps(
        {
            'songs': song_list
        },
        default=blank
    )


def restore_from_loaded_json(data):
    global song_list

    data = json.loads(data)
    song_list = data['songs']


def clear():
    global song_list

    song_list = {}


def add_song(file):
    global song_list

    song_list.append(file)


def remove_song(song):
    global song_list

    song_list.remove(song)
