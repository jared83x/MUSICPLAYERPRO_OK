import vlc
import os


class AudioEngine:

    def __init__(self):

        self.instance = vlc.Instance()

        self.player = (
            self.instance
            .media_player_new()
        )

        self.current_song = None


    def load(self, path):

        if not os.path.exists(path):
            raise FileNotFoundError(path)


        media = (
            self.instance
            .media_new(path)
        )


        self.player.set_media(media)

        self.current_song = path



    def play(self):

        self.player.play()



    def pause(self):

        self.player.pause()



    def stop(self):

        self.player.stop()



    def toggle(self):

        if self.player.is_playing():

            self.pause()

        else:

            self.play()



    def volume(self, value):

        value = max(
            0,
            min(value,100)
        )

        self.player.audio_set_volume(
            int(value)
        )



    def position(self):

        return (
            self.player
            .get_position()
        )



    def set_position(self,value):

        self.player.set_position(
            float(value)
        )



    def duration(self):

        return (
            self.player
            .get_length()
        )



    def current_time(self):

        return (
            self.player
            .get_time()
        )



    def playing(self):

        return (
            self.player
            .is_playing()
        )
