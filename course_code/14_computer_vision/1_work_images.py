import cv2

# grayscale 0
# color 1
# color with alpha canal -1 
img = cv2.imread('./course_code/14_computer_vision/files/galaxy.jpg', 0) # img is a numpy array

# print(type(img))
# print(img)
# print(img.shape)
# print(img.ndim)

# resized_img = cv2.resize(img, (500, 1000))
resized_img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))

cv2.imshow('Galaxy', img)
# cv2.waitKey(0) # any button close the window
cv2.waitKey(2000) # 2 seconds
cv2.destroyAllWindows()
