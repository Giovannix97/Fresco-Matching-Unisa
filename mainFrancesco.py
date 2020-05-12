import cv2
import numpy as np

img = cv2.imread('./image/brouge1.png',cv2.IMREAD_COLOR)
#total number of pixel
print(img.size)
cv2.imshow('Brouge1', img)
print('Shape of the image : {}'.format(img.shape))

#le righe sono
height = img.shape[0]
#le colonne sono
width = img.shape[1]

print('Image Hight {}'.format(img.shape[0]))
print('Image Width {}'.format(img.shape[1]))


#scorro le righe i e le colonne j
for i in range(height):
    for j in range(width):
        color=img[i,j]

        print(color)


cv2.waitKey()


