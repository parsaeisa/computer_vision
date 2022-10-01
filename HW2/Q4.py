import cv2
import os

dirname = os.path.dirname(__file__)
path = os.path.join(dirname , 'images/img1.png' )

img = cv2.imread(path ,1)
print(img.shape)

corner_count_x = 24
corner_count_y = 17

# mention github link , where you find out what is outputs 
corners_found , corners = cv2.findChessboardCorners(img , (corner_count_y,corner_count_x) , None )

if corners_found :
    cv2.drawChessboardCorners(img , (corner_count_y , corner_count_x) , corners , corners_found)
    cv2.imwrite("image_with_corners.jpg", img)
else : 
    print("Corners were not successfully found .")
