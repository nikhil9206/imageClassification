import cv2
import numpy as np
import random
import os

number = int(input("How many images?: "))
size = int(input("Lastly, how large (or small) would you like the shapes to be (in pixels)?: "))

num = 1

radius = 0
center = (0, 0) 
start_point = (0, 0)
end_point = (0, 0)
isClosed_TRI = True
thickness = 0
color = (0, 0, 0)
ifFill = 0

def shape():
        global ifFill
        global thickness
        global color

        ifFill = random.randint(0,1)

        if ifFill == 0:
            thickness = -1
        elif ifFill == 1:
            thickness = random.randint(1, 5)

        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def circ():
        global radius
        global center

        radius = random.randint(10, size)
        center = (random.randint(radius, 640 - radius), random.randint(radius, 475 - radius))

        shape()

def rect():
        global start_point
        global end_point

        start_x_RECT = random.randint(0, 640)
        start_y_RECT = random.randint(0, 475)

        if start_x_RECT + size <= 640 and start_x_RECT - size >= 0:
            end_x_RECT = random.randint(start_x_RECT - size, start_x_RECT + size)
        elif start_x_RECT + size >= 640 and start_x_RECT - size >= 0:
            end_x_RECT = random.randint(start_x_RECT - size, 640)
        elif start_x_RECT + size <= 640 and start_x_RECT - size <= 0:
            end_x_RECT = random.randint(0, start_x_RECT + size)
        elif start_x_RECT + size >= 640 and start_x_RECT - size <= 0:
            end_x_RECT = random.randint(0, 640)

        if start_y_RECT + size <= 475 and start_y_RECT - size >= 0:
            end_y_RECT = random.randint(start_y_RECT - size, start_y_RECT + size)
        elif start_y_RECT + size >= 475 and start_y_RECT - size >= 0:
            end_y_RECT = random.randint(start_y_RECT - size, 475)
        elif start_y_RECT + size <= 475 and start_y_RECT - size <= 0:
            end_y_RECT = random.randint(0, start_y_RECT + size)
        elif start_y_RECT + size >= 475 and start_y_RECT - size <= 0:
            end_y_RECT = random.randint(0, 475)

        start_point = (start_x_RECT, start_y_RECT)
        end_point = (end_x_RECT, end_y_RECT)    

        shape()

def tri():
        pointX = random.randint(0,640)
        pointY = random.randint(0, 475)
        pts = np.array([[pointX, pointY], [random.randint(pointX - size, pointX + size), random.randint(pointY - size, pointY + size)], [random.randint(pointX - size, pointX + size), random.randint(pointY - size, pointY + size)]], np.int32)
        return [pts]

for num in range(number):
    
    img = cv2.imread("black.jpg")

    shape_Selector = random.randint(0, 2)
    if shape_Selector == 1:
        rect()
        img = cv2.rectangle(img, start_point, end_point, color, thickness)

    elif shape_Selector == 0:
        circ()
            
        img = cv2.circle(img, center, radius, color, thickness)

    elif shape_Selector == 2:
            shape()
            if ifFill == 0:
                img = cv2.fillPoly(img, tri(), color)
            elif ifFill == 1:
                thickness_TRI = random.randint(0, 5)
                img = cv2.polylines(img, tri(), isClosed_TRI, color, thickness_TRI )

    cv2.imwrite(f'images/black_edited_{num}.jpg', img)


# cv2.imshow("Circle", img)
# k = cv2.waitKey(0) 
# cv2.destroyAllWindows()
#cv2.circle(image, center_coordinates, radius, color, thickness)
#cv2.rectangle(image, start_point, end_point, color, thickness)


