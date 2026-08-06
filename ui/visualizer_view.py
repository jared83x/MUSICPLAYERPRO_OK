import flet as ft


class VisualizerView(ft.Container):


    def __init__(self, visualizer):

        super().__init__()

        self.visualizer = visualizer

        self.height = 150


        self.bars = [

            ft.Container(

                width=6,

                height=10,

                bgcolor="#1DB954",

                border_radius=5

            )

            for _ in range(
                visualizer.bars
            )

        ]


        self.content = ft.Row(

            controls=self.bars,

            alignment=
            ft.MainAxisAlignment.CENTER

        )



    def animate(self):

        values = (
            self.visualizer
            .update()
        )


        for bar,value in zip(
            self.bars,
            values
        ):

            bar.height = value


        self.update()
