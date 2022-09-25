# computer_vision

## computer vision course , instructed by Dr.Mohammadi . 

In this repo you can see my answers to assignments and some notes for openCV python library . 

### foot of koozeh-gari 

when you use imshow method , a window will be opened and closed immediately . to solve this problem use these lines after calling imshow  : 
```python
cv2.waitKey()
cv2.destroyAllWindows()
```
