class Equalizer:


    def __init__(self):

        self.bands = [
            60,
            170,
            310,
            600,
            1000,
            3000,
            6000,
            12000,
            14000,
            16000
        ]


        self.values = {
            band: 0
            for band in self.bands
        }



    def set_band(
        self,
        frequency,
        gain
    ):

        if frequency in self.values:

            self.values[frequency] = gain



    def reset(self):

        for band in self.values:

            self.values[band] = 0



    def apply(self, player):

        eq = player.audio_equalizer_new()

        for index, band in enumerate(self.bands):

            gain = self.values[band]

            eq.set_amp_at_index(
                gain,
                index
            )


        player.set_equalizer(eq)
