import os
import time

while True:
    if os.path.exists('files/vegetables.txt'):
        with open('files/vegetables.txt') as file:
            print(file.read())
    else:
        print('File doesn\'t exists')

    time.sleep(10)
