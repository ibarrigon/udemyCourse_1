import cv2

# grayscale 0
# color 1
# color with alpha canal -1 
img = cv2.imread('./course_code/14_computer_vision/files/galaxy.jpg', 0) # img is a numpy array

# print(type(img))
# print(img)
# print(img.shape)
# print(img.ndim)

cv2.imshow('Galaxy', img)
# cv2.waitKey(0) # any button close the window
cv2.waitKey(2000) # 2 seconds
cv2.destroyAllWindows()
