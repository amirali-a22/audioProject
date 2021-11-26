from pydub import AudioSegment
from pydub.playback import play

# time_list = input('enter your peace want: ')
# time_list = time_list.split(' ')
# print(time_list)

time_list = ['1:41', '1:59']
converted_time = list()
ftr = [3600, 60, 1]
for t in time_list:
    temp = t.split(':')
    if len(temp) == 2:
        temp.insert(0, '0')
    converted_time.append(sum([a * b for a, b in zip(ftr, map(int, temp))]))
    # print(s)

compre_list = list()
for ct in converted_time:
    compre_list.append(ct * 1000)


def audio_duration(length):
    """ # hours, mins, seconds = audio_duration(length)"""
    hours = length // 3600  # calculate in hours
    length %= 3600
    mins = length // 60  # calculate in minutes
    length %= 60
    seconds = length  # calculate in seconds

    return hours, mins, seconds  # returns the duration


sound = AudioSegment.from_file("tajdidi.mp3", format="mp3")
sound.name = 'tajdidi2'
sound.ext = 'mp3'

# play(sound[compre_list[0]:compre_list[1]])
edited_sound = sound[compre_list[0]:compre_list[1]]
edited_sound.export(f'{sound.name}.{sound.ext}')
print('done')
