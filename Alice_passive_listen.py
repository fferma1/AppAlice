import time
import speech_recognition as sr
from sound import Sound
from Alice_answer import Alice

class Timer:

    def __init__(self):
        pass
    def start(self):
        self.start_time = time.perf_counter()
    def stop(self):
        self.end_time = time.perf_counter()
    def get_time(self):
        self.time = (- self.start_time + self.end_time)
        return self.time

def init_all():

    global t, r, m, command
    command = ''
    t = Timer()
    r = sr.Recognizer()
    r.dynamic_energy_threshold = False
    r.energy_threshold = 30
    try:
        m = sr.Microphone(device_index=2)
        "Используем наушники или сторонний микрофон"
        with m as source:
            print('Используются наушники, слушаем в фоновом режиме')
            r.pause_threshold = 0.5
    except OSError:
        m = sr.Microphone(device_index=1)
        "Используем встроенный микрофон"
        with m as source:
            print('Используется встроенный микрофон, слушаем в фоновом режиме')
            r.pause_threshold = 0.5

def callback(r, m):

    global command
    try:
        command = r.recognize_google(m, language="ru")
    except:
        pass

def main():
    Alice.listen_type = 0
    Alice.close_Alice = False
    init_all()
    stop_listening = r.listen_in_background(m, callback, phrase_time_limit = 1.5)
    t.start()
    while True:
        time.sleep(0.1)
        if Alice.close_Alice == True:
            Sound.volume_set(80)
            break
        if Alice.listen_type == 1:
            break
        Alice.answer_on_command(command, False, 0)


        #if 'Алиса' in command:
        #    Alice_active_listen.main()
        #    break
        #elif 'выключить алису' in command or 'выключить Алису' in command:
        #    break
