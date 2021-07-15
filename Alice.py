import time
import speech_recognition as sr
from sound import Sound

import rec_and_mic as ram

class VA:


    def __init__(self, command ='', listen_type = 1):
        self.command = command
        self. listen_type = listen_type


    def main_loop(self):
        self.listen_type = 1
        while True:
            if self.listen_type == 1:
                self.l_active()
            elif self.listen_type == 0:
                break
            elif self.listen_type == 2:
                self.l_passive()


    def understand_command(self, command):
        print('Алиса услышала - ',self.command)
        if 'Алиса' in self.command or 'алиса' in self.command:
            self.listen_type = 1
        if 'Алиса я ухожу' in self.command or 'алиса я ухожу' in self.command:
            self.listen_type = 2
        if 'выключить Алису' in self.command or 'выключить алису' in self.command:
            self.listen_type = 0


    def l_active(self,*args: tuple):
        print('Активный режим')
        ram.initram()
        while True:
            with ram.m:
                try:
                    audio = ram.r.listen(ram.m, 5, 5)
                except sr.WaitTimeoutError:
                    audio = ''
                    pass
                try:
                    self.command = ram.r.recognize_google(audio, language="ru").lower()
                except:
                    pass
                #return 'fmviif'
            self.understand_command(self.command)
            if self.listen_type != 1:
                break
        print('Выход из активного режим')


    def l_passive(self):
        ram.initram()
        print('Пассивный режим')
        ram.r.energy_threshold = 20
        stop_listening = ram.r.listen_in_background(ram.m, self.callback, phrase_time_limit=1.5)
        while True:
           time.sleep(0.1)
           if self.listen_type != 2:
               break
        stop_listening(wait_for_stop=False)
        print('Выход из пассивного режима')


    def callback(self, r, m):
        try:
            self.command = r.recognize_google(m, language="ru").lower()
            self.understand_command(self.command)
        except:
            pass


Alice = VA()
Alice.main_loop()

