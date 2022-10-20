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
