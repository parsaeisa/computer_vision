# OpenCV

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