import cv2
import os

dirname = os.path.dirname(__file__)
path = os.path.join(dirname , 'images/img1.png' )

img = cv2.imread(path ,1)
print(img.shape)