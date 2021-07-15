
import speech_recognition as sr  # распознавание пользовательской речи (Speech-To-Text)
import pyttsx3  # синтез речи (Text-To-Speech)
import wave  # создание и чтение аудиофайлов формата wav
import json  # работа с json-файлами и json-строками
import os  # работа с файловой системой
from sound import Sound
from Alice_answer import Alice

def init_rec():

    global rec,m
    rec = sr.Recognizer()
    rec.dynamic_energy_threshold = False
    rec.energy_threshold = 5
    try:
        m = sr.Microphone(device_index=2)
        with m as source:
            print('Используются наушники, слушаем в активном режим')
            #rec.adjust_for_ambient_noise(source, duration=0.5)
            rec.pause_threshold = 0.5
    except OSError:
        m = sr.Microphone(device_index=1)
        with m as source:
            print('Используется встроенный микрофон, слушаем в активном режим')
            #rec.adjust_for_ambient_noise(source, duration=0.5)
            rec.pause_threshold = 0.5

def record_and_recognize_audio(*args: tuple):

    recognized_data = ""
    with m:
        #rec.adjust_for_ambient_noise(m, duration=0.5)
        try:
            audio = rec.listen(m, 5, 5)
        except sr.WaitTimeoutError:
            audio = ''
            pass
        try:
            recognized_data = rec.recognize_google(audio, language="ru").lower()
        except AssertionError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Проверьте подключение к интернету..")
        return recognized_data

def main():

    Sound.volume_set(30)
    init_rec()
    molch = 0
    while True:
        command = record_and_recognize_audio()
        print(command)
        if command == '':
            molch +=1
        elif command != '':
            moclh = 0
        Alice.answer_on_command(command, False, 1)
        if Alice.close_Alice == True:
            Sound.volume_set(80)
            break
        if molch > 24:
            Sound.volume_set(80)
            Alice.answer_on_command('выйти из активного режима', False,1)