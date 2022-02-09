import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "ramya.jpg"


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])
    # it is 2 -dimensional array formula to convert image to grey scale


def dodge(front, back):
    final_sketch = front * 255 / (255 - back)
    # if image is greater than 255 which I don't think is possible but still it there will convert into 255
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255
    # to convert any suitable existing column to categorical type we weill use aspect fumctiom
    # uint8 is for 8 bit signed integer
    return final_sketch.astype('uint8')

    # if image is greater than 255 which


# to read given image
ss = imageio.imread(img)
# first we will convert image to black and white that means grey scale
gray = rgb2gray(ss)

# 0,0,0 is for darkest color and 255,255,255 is for bright color
i = 255 - gray

# to convert it into blur image
blur = scipy.ndimage.filters.gaussian_filter(i, sigma=15)
# sigma is the intensity of blurness of image
r = dodge(blur, gray)  # this function will convert our image to sketch by taking by taking 2 params blur,gray
cv2.imwrite('ramya_sketch.png', r)
