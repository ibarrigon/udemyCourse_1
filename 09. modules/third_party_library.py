import os
import time
import pandas

while True:
    if os.path.exists('files/temps_today.csv'):
        data = pandas.read_csv('files/temps_today.csv')
        print(data.mean())
        print(data.mean()['st1'])
    else:
        print('File doesn\'t exists')

    time.sleep(10)
