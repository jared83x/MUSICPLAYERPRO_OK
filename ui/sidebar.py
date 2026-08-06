import flet as ft

from config import SURFACE
from ui.add_folder import AddFolder


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
                    size=20,
                    weight="bold"
                ),

                ft.Divider(),

                self.item(
                    ft.Icons.HOME,
                    "Inicio",
                    self.click_list(0)
                ),

                self.item(
                    ft.Icons.LIBRARY_MUSIC,
                    "Biblioteca",
                    self.click_list(1)
                ),

                self.item(
                    ft.Icons.ALBUM,
                    "Álbumes",
                    self.click_list(2)
                ),

                self.item(
                    ft.Icons.PERSON,
                    "Artistas",
                    self.click_list(3)
                ),

                self.item(
                    ft.Icons.FAVORITE,
                    "Favoritos",
                    self.click_list(4)
                ),

                self.item(
                    ft.Icons.PLAYLIST_PLAY,
                    "Playlists",
                    self.click_list(5)
                ),

                self.item(
                    ft.Icons.ADD,
                    "Abrir",
                    self.click_list(6)
                )

            ]

        )

    
                
    def item(self, icon, text, click):

        return ft.ListTile(

            leading=ft.Icon(icon),

            title=ft.Text(text),

            on_click=click

        )

    def click_list(self,num):
    
        match num:
            case 0:
                return 0 # inicio
            case 1:
                return 1
            case 2:
                return 2
            case 3:
                return 3
            case 4:
                return 4
            case 5:
                return 5
            case 6:
                return AddFolder.open
