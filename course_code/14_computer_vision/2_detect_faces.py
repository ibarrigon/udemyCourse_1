import cv2

path = './course_code/14_computer_vision/files/faces/'
face_cascade = cv2.CascadeClassifier(path + 'haarcascade_frontalface_default.xml')

img = cv2.imread(path + 'photo.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert image in color to image in gray scale

faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors = 5) # faces is numpy array
for x, y, width, height in faces:
    new_img = cv2.rectangle(img, (x, y), (x + width, y + height), color = (0, 255, 0)) # draw rectangle in the face
    cv2.imwrite(path + "gotcha.jpg", new_img) 

