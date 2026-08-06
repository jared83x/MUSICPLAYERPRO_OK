from core.audio_engine import AudioEngine
import time


player = AudioEngine()


player.load(
    "cancion.mp3"
)


player.play()


print(
    "Duración:",
    player.duration()
)


time.sleep(10)


player.pause()


print(
    "Pausado"
)


time.sleep(3)


player.play()


time.sleep(10)


player.stop()
