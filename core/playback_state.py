class PlaybackState:


    def __init__(self):

        self.song = None

        self.cover = None

        self.playing = False

        self.position = 0

        self.duration = 0



    def update_song(
        self,
        song,
        cover
    ):

        self.song = song

        self.cover = cover
