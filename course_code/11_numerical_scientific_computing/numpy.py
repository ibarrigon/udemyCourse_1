# Most efficient list work. More simple. More low level
import numpy

n = numpy.arange(27) # type(n) -> numpy.ndarray
print(n) 
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])
print(n.reshape(3, 9))
# array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8],
#        [ 9, 10, 11, 12, 13, 14, 15, 16, 17],
#        [18, 19, 20, 21, 22, 23, 24, 25, 26]])

print(n.reshape(3, 3, 3))
# array([[[ 0,  1,  2],
#         [ 3,  4,  5],
#         [ 6,  7,  8]],
# 
#        [[ 9, 10, 11],
#         [12, 13, 14],
#         [15, 16, 17]],
# 
#        [[18, 19, 20],
#         [21, 22, 23],
#         [24, 25, 26]]])

m = numpy.asarray([[123, 12, 123, 12, 33], [], []])