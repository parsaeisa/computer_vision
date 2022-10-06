from cgi import print_environ
from msilib.schema import Directory
import cv2
import os
import numpy as np

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# undistort with just one image 
dirname = os.path.dirname(__file__)
path = os.path.join(dirname , 'images/img1.png' )

img = cv2.imread(path ,1)
print(img.shape)

corner_count_x = 24
corner_count_y = 17

gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

corners_found , corners = cv2.findChessboardCorners(gray , (corner_count_y,corner_count_x) , None )

if corners_found :
    improved_corners = cv2.cornerSubPix(gray , corners , (11,11), (-1,-1) , criteria )

    cv2.drawChessboardCorners(img , (corner_count_y , corner_count_x) , improved_corners , corners_found)
    cv2.imwrite("image_with_corners.jpg", img)
else : 
    print("Corners were not successfully found .")

# ====================================================================================
# undistort with images [1-4] 
# find corners in multiple images : 
images_directory = 'images'

objp = np.zeros((1,corner_count_x * corner_count_y , 3) , np.float32)
objp[0,:,:2] = np.mgrid[0:corner_count_y , 0:corner_count_x].T.reshape(-1,2)

prev_img_shape = None

objpoints = []

imgpoints = []

for filename in os.listdir(images_directory):
    if filename == 'img5.png':
        continue
    file_path = os.path.join(images_directory , filename)

    img = cv2.imread(path ,1)

    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

    corners_found , corners = cv2.findChessboardCorners(gray , (corner_count_y,corner_count_x) , None )

    if corners_found :
        objpoints.append(objp)
        imgpoints.append(corners)

        # improved_corners = cv2.cornerSubPix(gray , corners , (corner_count_y , corner_count_x),
        # (-1,-1) , criteria )

        img = cv2.drawChessboardCorners(img , (corner_count_y , corner_count_x) , corners , corners_found)

    else : 
        print("Corners were not successfully found in " , filename)

_, mtx, dist_coeffs, _,_ = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
print("Camera matrix : \n")
print(mtx)
print("dist_coeffs : \n")
print(dist_coeffs)

dirname = os.path.dirname(__file__)
path = os.path.join(dirname , 'images/img5.png' )

img = cv2.imread(path)
h,w = img.shape[:2]
newCameraMatrix,roi = cv2.getOptimalNewCameraMatrix(mtx,dist_coeffs , (w,h) , 1, (w,h))
dst = cv2.undistort(img , mtx, dist_coeffs, None, newCameraMatrix)

x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('calibresult.png', dst)