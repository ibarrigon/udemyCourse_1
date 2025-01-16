import cv2 # only when required (line 13n), time

video = cv2.VideoCapture(0)

# Fisrt code One capture
# check, frame = video.read()
# 
# print(check)
# print(frame)
# 
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# 
# time.sleep(3)
# 
# cv2.imshow('Color Capturing', frame)
# 
# cv2.waitKey(0)
# 
# cv2.imshow('Gray Capturing', gray)
# cv2.waitKey(0)

# Second code: Capture every 2 seconds. Need <Ctrl + c> to terminate
# while True:
#     check, frame = video.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('Color Capturing', frame)
#     cv2.waitKey(2000) # Two seconds

# Third code: Capture every 1 seconds for 1000 and 1 milisecond if 1 is in waitKey. Push 'q' to terminate
while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Color Capturing', gray)
    if cv2.waitKey(1) == ord('q'): 
        break

# This code is required any time
video.release()
cv2.destroyAllWindows()