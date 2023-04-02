import os
import wave

filename = input("Введите путь к файлу .wav: ")

if not os.path.isfile(filename):
    print(f"Файл {filename} не найден!")
    exit()

rate_change = float(input("Введите коэффициент изменения скорости (> 0): "))

if rate_change <= 0:
    print("Коэффициент изменения скорости должен быть больше 0!")
    exit()

new_filename = os.path.splitext(filename)[0] + f"_speed{rate_change:.2f}.wav"

with wave.open(filename, 'rb') as wav_file:
    params = wav_file.getparams()
    new_rate = int(params[2] * rate_change)
    with wave.open(new_filename, 'wb') as new_wav_file:
        new_wav_file.setparams((params[0], params[1], new_rate, params[3], params[4], params[5]))
        frames = wav_file.readframes(params[3])
        new_wav_file.writeframes(frames)
        print(f"Файл {new_filename} создан!")