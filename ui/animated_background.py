import flet as ft


class AnimatedBackground(ft.Container):


    def __init__(self):

        super().__init__()

        self.bgcolor="#101214"


    def change_color(
        self,
        color
    ):

        self.bgcolor = (
            color
        )

        self.animate = 500

        self.update()
