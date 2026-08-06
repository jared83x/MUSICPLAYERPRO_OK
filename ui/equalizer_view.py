import flet as ft


class EqualizerView(ft.Container):


    def __init__(self,equalizer):

        super().__init__()


        self.equalizer = equalizer


        self.sliders=[]


        controls=[]


        frequencies=[

            "60Hz",
            "170Hz",
            "310Hz",
            "600Hz",
            "1kHz",
            "3kHz",
            "6kHz",
            "12kHz",
            "14kHz",
            "16kHz"

        ]


        for freq in frequencies:


            slider = ft.Slider(

                min=-12,

                max=12,

                value=0,

                vertical=True

            )


            self.sliders.append(
                slider
            )


            controls.append(

                ft.Column(

                    [

                        slider,

                        ft.Text(freq)

                    ]

                )

            )



        self.content = ft.Row(
            controls=controls,
            alignment=
            ft.MainAxisAlignment.CENTER
        )
