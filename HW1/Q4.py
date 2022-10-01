import cv2

def show_image(image):
    cv2.imshow('image' , image)
    cv2.waitKey()
    cv2.destroyAllWindows()

path = "background.png"

img = cv2.imread(path ,1)
print(img.shape)

red_channel = img[:,:,2]
print(red_channel.shape)



## convert to RGB 
image_rgb = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

## resizing image
WIDTH = 290
HEIGHT = 570

img_resized = cv2.resize(image_rgb , (HEIGHT , WIDTH))

## draw lines 
COLOR = (255, 0, 0)
THICKNESS = 2

image = cv2.line(img_resized, (5,5), (565,5), COLOR, THICKNESS)
image = cv2.line(img_resized, (5,5), (5,285), COLOR, THICKNESS)
image = cv2.line(img_resized, (565,285), (565,5), COLOR, THICKNESS)
image = cv2.line(img_resized, (565,285), (5,285), COLOR, THICKNESS)

## draw circles 

corners = [
    (5,5),
    (565,5),
    (5,285),
    (565,285),
]

for corner in corners :
    image = cv2.circle(image , corner,5 , (0,0,255) , THICKNESS)

## draw end.png
COLOR = (0, 0, 0)

for i in range(8):
    x_point = i * 80 + 5
    for corner in corners :
        end = cv2.line(img_resized,corner , (x_point,145), COLOR, THICKNESS)

show_image(image=end)


## save picture 
cv2.imwrite('mypic.jpg',image)
