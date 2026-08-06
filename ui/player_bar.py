import flet as ft

from config import SURFACE
from core.player_controller import PlayerController


class PlayerBar(ft.Container):

    def __init__(self):

        super().__init__()
        #self.controller = controller
        self.controller = PlayerController

        self.height=90

        self.bgcolor=SURFACE

        self.padding=15


        self.content=ft.Row(

            alignment=
            ft.MainAxisAlignment.SPACE_BETWEEN,

            controls=[


                ft.Column(
                    [
                        ft.Text(
                            "Sin reproducción"
                        ),

                        ft.Text(
                            "Artista desconocido",
                            size=12
                        )
                    ]
                ),


                ft.Row(

                    controls=[

                        ft.IconButton(
                            ft.Icons.SKIP_PREVIOUS
                        ),

                        ft.IconButton(
                            ft.Icons.PLAY_CIRCLE,
                            icon_size=45,
                            on_click = lambda e: 
                                self.controller.pause()
                        ),

                        ft.IconButton(
                            ft.Icons.SKIP_NEXT
                        )

                    ]

                ),


                ft.Row(

                    controls=[

                        ft.Icon(
                            ft.Icons.VOLUME_UP
                        ),

                        ft.Slider(
                            width=150
                        )

                    ]

                )

            ]

        )
