# OpenCV

We can show an image using openCV.imshow() , but in colab its better to use plt.imshow : 
```python
plt.imshow(img , cmap='gray')
```

* with cmap argument you can choose the color of your image . 

## Convert color
The images that are being scanned by imread , is BGR at first . 

Converting a picture to gray : 
```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

## Histogram

drawing the histogram of a picture with 256 brightness layers : 

```python
plt.hist(image.flatten(),256,[0,256], color = 'r')
plt.show()
```

<br />

### Histogram equalization

**cv2.equalizeHist(img)** : is a method in openCV which equalize Histograms . output of this method 
is an image with equalized histogram . 

**CLAHE** : the code below applies CLAHE to an image :
(img is the output of imread method )
```python
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clh = clahe.apply(img)
```

### Shape extraction 

## Canny edge detector 

There is a method called `cv2.Canny` which takes 3 arguments . first one is image . 

The second one and third one , whatever these items are bigger , the weak edges are more removed . 

The maximum derivative in a picture is 255 ( two adjacent pixels , one of them is white and 255 and the other is black 0 and the derivative is the difference of brightness level ) and for taking gradient in Canny , Sobel is used , so the derivative is 8 times bigger than the actual derivative , so these parameters can be big about 2000 ( 8 * 255 ) . 

and 2nd param should be smaller than 3rd parameter . 

mid level edges must be between these two parameters --> refer to Canny structure . 

```python
edges = cv2.Canny(im, 50, 200)
```

## Bluring

Bluring is made when a **Gaussian filter** is applied to a picture . code : 

* Gaussian filter is an averaging filter . Its size can be 3 , 5 , 7 etc . 

```python
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(im,-1,kernel)
```

## Contours

In OpenCV, finding contours is like finding white object from black background. So remember, object to be found should be white and background should be black. 

An image should be tresholded or should use Canny edge detector to be black and white before applying findContours on it . 

Contours has some features like : 
* area : contourArea method which takes a single contour 
* perimeter : or arcLength
* centroid
* bounding box

