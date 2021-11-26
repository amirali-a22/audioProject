from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("tajdidi.mp3", format="mp3")
play(sound)
