import flet as ft


class LyricsView(ft.Container):


    def __init__(self):

        super().__init__()


        self.text = ft.Text(

            "No hay letras",

            size=26,

            weight="bold",

            text_align=
            ft.TextAlign.CENTER

        )


        self.content = ft.Container(

            alignment=
            ft.alignment.center,

            content=self.text

        )



    def update_lyric(
        self,line
    ):

        self.text.value=line

        self.update()
