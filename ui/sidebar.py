import flet as ft

#from ..config import SURFACE
from ui.config import SURFACE
from ui.add_folder import AddFolder

#folder_tool = AddFolder

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
                    #AddFolder.open
                    #self.folder_tool.open()
                ),

                self.item(
                    ft.Icons.LIBRARY_MUSIC,
                    "Biblioteca",
                    self.click_list(1)
                    #AddFolder.open
                    #self.folder_tool.open()
                ),

                self.item(
                    ft.Icons.ALBUM,
                    "Álbumes",
                    self.click_list(2)
                    #AddFolder.open
                    #self.folder_tool.open()
                ),

                self.item(
                    ft.Icons.PERSON,
                    "Artistas",
                    self.click_list(3)
                    #AddFolder.open
                    #self.folder_tool.open()
                ),

                self.item(
                    ft.Icons.FAVORITE,
                    "Favoritos",
                    self.click_list(4)
                    #AddFolder.open
                    #self.folder_tool.open()
                ),

                self.item(
                    ft.Icons.PLAYLIST_PLAY,
                    "Playlists",
                    self.click_list(5)
                    #AddFolder.open
                    #self.folder_tool.open()
                ),

                self.item(
                    ft.Icons.ADD,
                    "Abrir",
                    self.click_list(6),
                    #AddFolder.open()
                    #self.folder_tool.open()
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

        folder_tool = AddFolder(self.page)
        #self.page.update()

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
                #return AddFolder.open(e)
                return folder_tool.open()
