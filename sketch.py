import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread( "pic.jpg", -1 )
img1, img2 = cv2.pencilSketch( img )
plt.imshow(img)
plt.imshow(img1)
plt.inshow(img2)
