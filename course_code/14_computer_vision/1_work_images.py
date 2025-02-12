import cv2

# grayscale 0
# color 1
# color with alpha canal -1 
image = cv2.imread('./course_code/14_computer_vision/files/galaxy.jpg', 0) # image is a numpy array

# print(type(image))
# print(image)
# print(image.shape)
# print(image.ndim)

# resized_image = cv2.resize(image, (500, 1000))
resized_image = cv2.resize(image, (int(image.shape[1] / 2), int(image.shape[0] / 2)))

cv2.imshow('Galaxy', image)
# cv2.waitKey(0) # any button close the window
cv2.waitKey(2000) # 2 seconds
cv2.destroyAllWindows()
