import flet as ft

from config import SURFACE


class Sidebar(ft.Container):

    def __init__(self):

        super().__init__()

        self.width = 240

        self.bgcolor = SURFACE

        self.padding = 20


        self.content = ft.Column(

            controls=[

                ft.Text(
                    "🎵 MusicPlayerPro",
                    size=22,
                    weight="bold"
                ),

                ft.Divider(),

                self.item(
                    ft.Icons.HOME,
                    "Inicio"
                ),

                self.item(
                    ft.Icons.LIBRARY_MUSIC,
                    "Biblioteca"
                ),

                self.item(
                    ft.Icons.ALBUM,
                    "Álbumes"
                ),

                self.item(
                    ft.Icons.PERSON,
                    "Artistas"
                ),

                self.item(
                    ft.Icons.FAVORITE,
                    "Favoritos"
                ),

                self.item(
                    ft.Icons.PLAYLIST_PLAY,
                    "Playlists"
                )

            ]

        )


    def item(self, icon, text):

        return ft.ListTile(

            leading=ft.Icon(icon),

            title=ft.Text(text)

        )
