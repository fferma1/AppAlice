import speech_recognition as sr


r = sr.Recognizer()
r.dynamic_energy_threshold = False
r.energy_threshold = 2
try:
    m = sr.Microphone(device_index=2)
    with m as source:
        print('Используются наушники')
        r.pause_threshold = 0.5
except OSError:
    m = sr.Microphone(device_index=1)
    with m as source:
        print('Используется встроенный микрофон')
        r.pause_threshold = 0.5