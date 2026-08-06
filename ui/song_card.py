import flet as ft


class SongCard(ft.Container):

    def __init__(self, song, on_play):

        super().__init__()


        self.padding = 10

        self.border_radius = 12

        self.bgcolor = "#181B22"


        self.content = ft.Row(

            controls=[


                ft.Container(

                    width=55,
                    height=55,

                    bgcolor="#252A33",

                    border_radius=10,

                    content=ft.Icon(
                        ft.Icons.MUSIC_NOTE
                    )

                ),


                ft.Column(

                    expand=True,

                    spacing=2,

                    controls=[

                        ft.Text(
                            song.title,
                            weight="bold"
                        ),

                        ft.Text(
                            song.artist,
                            color="#AAAAAA"
                        ),

                        ft.Text(
                            song.album,
                            size=12,
                            color="#777777"
                        )

                    ]

                ),


                ft.IconButton(

                    icon=ft.Icons.PLAY_ARROW,

                    on_click=lambda e:
                        on_play(song)

                ),
                
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(
                            text="Reproducir ahora"
                        ),

                        ft.PopupMenuItem(
                            text="Añadir a cola"
                        ),

                        ft.PopupMenuItem(
                            text="Añadir a favoritos ❤️")

                ]

            )



            ]

        )
