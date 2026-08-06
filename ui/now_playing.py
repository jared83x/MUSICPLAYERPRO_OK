import flet as ft


class NowPlaying(ft.Container):


    def __init__(self,state):

        super().__init__()

        self.state = state


        self.width = 320

        self.padding = 20


        self.cover = ft.Image(

            width=260,

            height=260,

            fit=ft.ImageFit.COVER

        )


        self.title = ft.Text(

            "Sin canción",

            size=22,

            weight="bold"

        )


        self.artist = ft.Text(
            ""
        )


        self.content = ft.Column(

            horizontal_alignment=
            ft.CrossAxisAlignment.CENTER,

            controls=[

                self.cover,

                self.title,

                self.artist,

                ft.Divider(),

                ft.Icon(
                    ft.Icons.MUSIC_NOTE,
                    size=60
                )

            ]

        )



    def refresh(self):

        if self.state.song:

            self.title.value = (
                self.state.song.title
            )

            self.artist.value = (
                self.state.song.artist
            )


            if self.state.cover:

                self.cover.src = (
                    self.state.cover
                )


            self.update()
