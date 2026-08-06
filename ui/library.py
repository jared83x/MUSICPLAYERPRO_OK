import flet as ft


class Library(ft.Container):

    def __init__(self):

        super().__init__()

        self.expand=True

        self.padding=30


        self.content=ft.Column(

            controls=[

                ft.Text(
                    "Biblioteca musical",
                    size=30,
                    weight="bold"
                ),

                ft.Text(
                    "Aquí aparecerán tus canciones."
                )

            ]

        )
