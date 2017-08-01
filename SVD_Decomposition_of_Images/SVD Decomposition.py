#this program uses the linear algebra technique singular value decomposition
#to compress a picture using various choices of rank

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#convert image to grayscale so we are only dealing
#  with an mxn gray matrix instead of an mxnx3 RGB matrix
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

img = mpimg.imread('oes.png')
gray = rgb2gray(img)
print('size of matrix',len(gray),len(gray[0]))
rank=min(len(gray),len(gray[0]))
print('rank=',rank)

plt.figure(1)
plt.subplot(221)
plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.title('Original image, rank= %s'%rank)

#SVD to compress the image to rank1
rank1=2
LA = np.linalg
a = np.array(gray)

U, s, Vh = LA.svd(a, full_matrices=False)
assert np.allclose(a, np.dot(U, np.dot(np.diag(s), Vh)))

s[rank1:] = 0
new_a = np.dot(U, np.dot(np.diag(s), Vh))

plt.subplot(222)
plt.imshow(new_a, cmap = plt.get_cmap('gray'))
plt.title('rank= %s'%rank1)


#SVD to compress the image to rank2
rank2=10
U2, s2, Vh2 = LA.svd(a, full_matrices=False)
assert np.allclose(a, np.dot(U2, np.dot(np.diag(s2), Vh2)))

s2[rank2:] = 0
new_a2 = np.dot(U2, np.dot(np.diag(s2), Vh2))


plt.subplot(223)
plt.imshow(new_a2, cmap = plt.get_cmap('gray'))
plt.title('rank=%s'%rank2)


#SVD to compress the image to rank3
rank3=20
U3, s3, Vh3 = LA.svd(a, full_matrices=False)
assert np.allclose(a, np.dot(U3, np.dot(np.diag(s3), Vh3)))

s3[rank3:] = 0
new_a3 = np.dot(U3, np.dot(np.diag(s3), Vh3))


plt.subplot(224)
plt.imshow(new_a3, cmap = plt.get_cmap('gray'))
plt.title('rank=%s'%rank3)
plt.show()