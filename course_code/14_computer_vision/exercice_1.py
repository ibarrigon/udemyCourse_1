# Write a script that resizes all images in a directory to 100x100.
# use files from files/sample_images.zip extracted in files/sample_images

import cv2
import glob

path = './course_code/14_computer_vision/files/sample_images/'

images = glob.glob(path + "*.jpg")

for image in images:
    image_content = cv2.imread(image, 0)
    resized = cv2.resize(image_content, (100, 100))
    cv2.imwrite(path + "resized_" + image, resized) 