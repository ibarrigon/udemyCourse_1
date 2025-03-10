import cv2, time, pandas
from datetime import datetime

def getColorImage(vide):
    check, frame = video.read()

    return frame

def getGrayImage(frame):
    # parameters: image to blur, gaussian cardinal, standart deviation
    return cv2.GaussianBlur(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), (21, 21), 0)
    
captured_movement = []
times = []
    
video = cv2.VideoCapture(0)
# clear frame (only background)
first_frame = getGrayImage(getColorImage(video))
data_content = pandas.DataFrame(columns = ['Start', 'End'])

while True:
    there_is_movement = 0
    
    frame = getColorImage(video)
    gray = getGrayImage(frame)
    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2) # The bigger iterations the smoother it is
    
    (_, contours, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue

        there_is_movement = 1
        (x, y, width, height) = cv2.boundRect(contour)
        cv2.rectangle(frame, (x, y), (x + width, y + height))

    captured_movement.append(there_is_movement)
    if len(captured_movement) > 1 and captured_movement[-1] != captured_movement[-2]:
        times.append(datetime.now())

    
    cv2.imshow('Blurred gray frame', gray)
    cv2.imshow('Delta frame', delta_frame)
    cv2.imshow('Threshold frame', thresh_frame)
    cv2.imshow('Threshold frame', frame)
    if cv2.waitKey(1) == ord('q'): 
        break

# print(times)

for i in range(0, len(times), 2):
    data_content = data_content.append({ 'Start': times[i], 'End': times[i + 1] }, ignore_index = true)

data_content.to_csv('times.csv')

# This code is required any time
video.release()
cv2.destroyAllWindows()