import random


class AudioVisualizer:


    def __init__(self):

        self.bars = 32

        self.values = [
            0
            for _ in range(self.bars)
        ]



    def update(self):

        self.values = [

            random.randint(
                5,
                100
            )

            for _ in range(
                self.bars
            )

        ]


        return self.values
