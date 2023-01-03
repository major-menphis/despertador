from pygame import mixer

def play_alarm():
    mixer.init()
    mixer.music.load('./sounds/buzina_curta.mp3')
    mixer.music.play()
    #while mixer.music.get_busy():
    #    continue
    #return 'executado'

if __name__ == '__main__':
    play_alarm()
