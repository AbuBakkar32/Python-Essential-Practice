import cv2
import matplotlib.pyplot as plt
import numpy as np

# -------------------------IMAGE Read from file and convert to COLOR as BGR to RGB----------------------

# img = cv2.imread('Rakib2.jpg')
# img = cv2.cvtColor(img, cv2.COLORMAP_RAINBOW)
# IM = plt.imshow(img)
# print(IM)

# ----------------------------Numpy Tutorial part 2----------------------------------
# x = [1, 2, 3]
# y = [4, 5, 6]
# a = np.array(x)
# b = np.array(y)
#
# print(np.add(a, b))
# print(np.subtract(a, b))
# print(np.multiply(a, b))
# print(np.divide(b, a))
# print(np.exp(a))
# print(np.sqrt(b))
# print(np.sin(b))
# print(np.cos(b))
# print(np.log(b))
# print(a.dot(b))
# print(a.sum())
# print(a.max())
# print(a.min())
# print(a.mean())
# print(np.median(b))
# print(a.sort())
# print(np.corrcoef(b))  # returns correlation coefficient
# print(b.cumsum())  # returns array of cumulative summation
# print(np.std(b))  # returns standard deviation of array b


# ----------------------------Numpy Tutorial End-part ----------------------------------

# np.save('file_name.npy', x)  # to save numPy array as a file of Npy
# a = np.load('file_name.npy') # load file from directory
#
# z = x.copy()
# np.array_equal(x, y)
#
# arr = np.array([2, 3, 4, 5])
# arr = np.reshape(arr, (2, 2))  # chnage shape of array
#
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
#
# v = np.concatenate((a, b), axis=0)  # #concatenate 2 arrays vertically, axis=0
# h = np.concatenate((a, b), axis=1)  # #concatenate 2 arrays Horizontally, axis=1
#
# a = np.array([[1, 2], [3, 4]])
# print(np.vsplit(a, 2))  # vertical split
# print(np.hsplit(a, 2))  # horizontal split
#
# a = np.array([1, 2, 3, 4, 5])
# print(a[:2])  # selects only first 2 elements
