from PIL import Image
import numpy as np
import time
from cv2 import *
from playsound import playsound


st = time.time()
y = 0
x = 0
percentage_changed = 10


cam = VideoCapture(0)
s, img = cam.read()
if s:
    imwrite("image.PNG",img) #save image


img1 = Image.open('image.PNG').resize((320, 240))

ary = np.array(img1)

s, img = cam.read()
if s:
    imwrite("image2.PNG", img)  # save image

img2 = Image.open('image2.PNG').resize((320, 240))
ary2 = np.array(img2)
for i in range(0, len(ary) - 1):
    for b in range(0, len(ary[i]) - 1):
        if abs(float(ary[i][b][0]) - float(ary2[i][b][0])) + abs(float(ary[i][b][1]) - float(ary2[i][b][1])) + abs(
                float(ary[i][b][2]) - float(ary2[i][b][2])) > 100:
            x += 1
        y += 1

if x / y > 0.1:
    print("True, " + str(x / y))
else:
    print("False, " + str(x / y))
print("x = " + str(x))

y = 0
x = 0
while True:


    s, img = cam.read()
    if s:
        imwrite("image.PNG",img) #save image


    img1 = Image.open('image.PNG').resize((320, 240))

    ary = np.array(img1)


    print("first image taken")

    time.sleep(2)


    s, img = cam.read()
    if s:
        imwrite("image2.PNG",img) #save image


    img2 = Image.open('image2.PNG').resize((320, 240))
    ary2 = np.array(img2)

    print("second image taken")

    for i in range(0, len(ary)-1):
        for b in range(0, len(ary[i])-1):
            if abs(float(ary[i][b][0]) - float(ary2[i][b][0])) + abs(float(ary[i][b][1]) - float(ary2[i][b][1])) + abs(float(ary[i][b][2]) - float(ary2[i][b][2])) > 100:
                x += 1
            y += 1


    if x / y > percentage_changed / 100:
        print("True, " + str(x/y))
        playsound('obiwan.wav')
    else:
        print("False, " + str(x/y))
    y = 0
    x = 0



print("It took: " + str(time.time() - st))
