from core.audio_engine import AudioEngine


class PlayerController:


    def __init__(self):
        
        self.crossfade = False
        self.crossfade_seconds = 5
        
        self.engine = AudioEngine()

        self.song = None



    def play_song(self,path):

        self.engine.load(path)

        self.engine.play()

        self.song = path



    def pause(self):

        self.engine.pause()



    def stop(self):

        self.engine.stop()



    def next_position(self,value):

        self.engine.set_position(value)



    def volume(self,value):

        self.engine.volume(value)
