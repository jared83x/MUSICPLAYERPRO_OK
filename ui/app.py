import flet as ft

from ui.sidebar import Sidebar
from ui.library import Library
from ui.player_bar import PlayerBar
from core.player_controller import PlayerController


class MusicPlayerApp:

    def __init__(self, page):

        self.page = page

        self.build()


    def build(self):

        self.page.add(

            ft.Row(
                expand=True,

                controls=[

                    Sidebar(),

                    ft.Column(

                        expand=True,

                        controls=[

                            LibraryView(
                                self.player),

                            PlayerBar()

                        ]

                    )

                ]

            )

        )
