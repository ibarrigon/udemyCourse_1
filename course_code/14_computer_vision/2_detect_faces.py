import cv2

path = './course_code/14_computer_vision/files/faces/'
face_cascade = cv2.CascadeClassifier(path + 'haarcascade_frontalface_default.xml')

image = cv2.imread(path + 'photo.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert image in color to image in gray scale

faces = face_cascade.detectMultiScale(gray_image, scaleFactor = 1.05, minNeighbors = 5) # faces is numpy array
for x, y, width, height in faces:
    new_image = cv2.rectangle(image, (x, y), (x + width, y + height), color = (0, 255, 0)) # draw rectangle in the face
    cv2.imwrite(path + "gotcha.jpg", new_image) 

