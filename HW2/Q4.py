import cv2
import os
import numpy as np

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

corner_count_x = 24
corner_count_y = 17

images_directory = 'images'

def img1to4 (filename):
    return filename == 'img5.png'

def just_img1 (filename):
    return filename != 'img1.png'

def undistort_picture ( images_directory , condition, result_path ):
    objp = np.zeros((1,corner_count_x * corner_count_y , 3) , np.float32)
    objp[0,:,:2] = np.mgrid[0:corner_count_y , 0:corner_count_x].T.reshape(-1,2)

    objpoints = []

    imgpoints = []

    for filename in os.listdir(images_directory):        

        if condition(filename) :
            continue

        file_path = os.path.join(images_directory , filename)
        img = cv2.imread(file_path ,1)
        gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

        corners_found , corners = cv2.findChessboardCorners(img , (corner_count_y,corner_count_x) , None )

        if corners_found :
            improved_corners = cv2.cornerSubPix(gray , corners , (11 , 11), (-1,-1) , criteria )

            objpoints.append(objp)
            imgpoints.append(improved_corners)

            img = cv2.drawChessboardCorners(img , (corner_count_y , corner_count_x) , improved_corners , corners_found)

        else : 
            print("Corners were not successfully found in " , filename)

    _, mtx, dist_coeffs, _,_ = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    print("dist_coeffs respectively k1 , k2 , p1 , p2 , k3:")
    print(dist_coeffs)
    print('\n')

    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname , 'images/img5.png' )

    img = cv2.imread(path)
    h,w = img.shape[:2]
    newCameraMatrix,roi = cv2.getOptimalNewCameraMatrix(mtx,dist_coeffs , (w,h) , 1, (w,h))
    dst = cv2.undistort(img , mtx, dist_coeffs, None, newCameraMatrix)

    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]
    cv2.imwrite(result_path, dst)

undistort_picture(images_directory , img1to4 , 'calibrate_result_1to4.png' )

undistort_picture(images_directory , just_img1 , 'calibrate_result_img1.png' )