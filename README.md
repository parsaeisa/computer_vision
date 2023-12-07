# computer_vision

Computer vision course , instructed by Dr.Mohammadi . 

In this repo you can see my answers to assignments and some notes for openCV python library . 

What I learned during the practices : 
* Image formation
* Image processing in spatial domain
* Image processing in frequency domain
* Edge detectors like Canny and Sobel 
* Morphological process ( Dilate, Erode, Open, Close, Hit or Miss)
* Finding key points and applying most suitable transforms
* Deep networks like U-Net
* Descriptors (Shape, Color, Texture)
* Object detection
* Image segmentation

### foot of koozeh-gari 

when you use imshow method , a window will be opened and closed immediately . to solve this problem use these lines after calling imshow  : 
```python
cv2.waitKey()
cv2.destroyAllWindows()
```
