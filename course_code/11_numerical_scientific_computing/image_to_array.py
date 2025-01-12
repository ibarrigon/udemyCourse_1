import cv2
import numpy

# cv2.imread() -> parameters
# 1. file name
# 2. Color scale: 
#   a. 0 for grayscale
#   b. 1 for RGB

im_gray = cv2.imread('files/smallgray.png', 0)
print(im_gray)
# [[187 158 104 121 143]
#  [198 125 255 255 147]
#  [209 134 255  97 182]]

im_rgb = cv2.imread('files/smallgray.png', 1)
print(im_g)
# [[[187 187 187]
#   [158 158 158]
#   [104 104 104]
#   [121 121 121]
#   [143 143 143]]
# 
#  [[198 198 198]
#   [125 125 125]
#   [255 255 255]
#   [255 255 255]
#   [147 147 147]]
# 
#  [[209 209 209]
#   [134 134 134]
#   [255 255 255]
#   [ 97  97  97]
#   [182 182 182]]]

# save file
cv2.imwrite('files/newsmallgray.png', im_gray) # return True

print(im_gray[0:2])
# array([[187, 158, 104, 121, 143],
#        [198, 125, 255, 255, 147]], dtype=uint8)

print(im_gray[0:2, 2:4])
# array([[104, 121],
#        [255, 255]], dtype=uint8)

print(im_gray[:, 2:4])
# array([[104, 121],
#        [255, 255],
#        [255,  97]], dtype=uint8)

print(im_gray[2, 4])
# 182

# iterate by rows
for i in im_gray:
    print(i)
# [187 158 104 121 143]
# [198 125 255 255 147]
# [209 134 255  97 182]

# iterate by columns
for i in im_gray.T:
    print(i)
# [187 198 209]
# [158 125 134]
# [104 255 255]
# [121 255  97]
# [143 147 182]

for i in im_gray.flat:
    print(i)
# 187
# 158
# 104
# 121
# 143
# 198
# 125
# 255
# 255
# 147
# 209
# 134
# 255
# 97
# 182

ims = numpy.hstack((im_gray, im_gray)) # to concate need a tuple
print(ims)
# array([[187, 158, 104, 121, 143, 187, 158, 104, 121, 143],
#        [198, 125, 255, 255, 147, 198, 125, 255, 255, 147],
#        [209, 134, 255,  97, 182, 209, 134, 255,  97, 182]], dtype=uint8)

ims = numpy.hstack((im_gray, im_gray, im_gray))
print(ims)
# array([[187, 158, 104, 121, 143, 187, 158, 104, 121, 143, 187, 158, 104, 121, 143],
#        [198, 125, 255, 255, 147, 198, 125, 255, 255, 147, 198, 125, 255, 255, 147],
#        [209, 134, 255,  97, 182, 209, 134, 255,  97, 182, 209, 134, 255, 97, 182]], dtype=uint8)

ims = numpy.vstack((im_gray, im_gray, im_gray))
print(ims)
# array([[187, 158, 104, 121, 143],
#        [198, 125, 255, 255, 147],
#        [209, 134, 255,  97, 182],
#        [187, 158, 104, 121, 143],
#        [198, 125, 255, 255, 147],
#        [209, 134, 255,  97, 182],
#        [187, 158, 104, 121, 143],
#        [198, 125, 255, 255, 147],
#        [209, 134, 255,  97, 182]], dtype=uint8)

# lst = numpy.hsplit(ims, 3) -> error: not equal division
lst = numpy.hsplit(ims, 5)
print(lst)
# [array([[187],
#        [198],
#        [209],
#        [187],
#        [198],
#        [209],
#        [187],
#        [198],
#        [209]], dtype=uint8), array([[158],
#        [125],
#        [134],
#        [158],
#        [125],
#        [134],
#        [158],
#        [125],
#        [134]], dtype=uint8), array([[104],
#        [255],
#        [255],
#        [104],
#        [255],
#        [255],
#        [104],
#        [255],
#        [255]], dtype=uint8), array([[121],
#        [255],
#        [ 97],
#        [121],
#        [255],
#        [ 97],
#        [121],
#        [255],
#        [ 97]], dtype=uint8), array([[143],
#        [147],
#        [182],
#        [143],
#        [147],
#        [182],
#        [143],
#        [147],
#        [182]], dtype=uint8)]

lst = numpy.vsplit(ims, 3)
print(lst)
# [array([[187, 158, 104, 121, 143],
#        [198, 125, 255, 255, 147],
#        [209, 134, 255,  97, 182]], dtype=uint8), 
#  array([[187, 158, 104, 121, 143],
#        [198, 125, 255, 255, 147],
#        [209, 134, 255,  97, 182]], dtype=uint8), 
#  array([[187, 158, 104, 121, 143],
#        [198, 125, 255, 255, 147],
#        [209, 134, 255,  97, 182]], dtype=uint8)]

print(lst[0])
# array([[187, 158, 104, 121, 143],
#        [198, 125, 255, 255, 147],
#        [209, 134, 255,  97, 182]], dtype=uint8)