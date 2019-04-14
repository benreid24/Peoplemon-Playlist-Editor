from view.playlist_editor import PlaylistEditor
from controller import songs as controller


def main():
    app = PlaylistEditor()

    controller.init(app)

    app.mainloop()


if __name__ == '__main__':
    main()
