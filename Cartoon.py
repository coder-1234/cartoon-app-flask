#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import os


# In[2]:


def cartoonify(img_rgb,s):    

    numBilateralFilters = 4

    img_color = img_rgb
    #cv2.imshow("Orignal",img_color)
    #cv2.waitKey(0)
    for _ in range(numBilateralFilters):
        img_color = cv2.bilateralFilter(img_color, 15, 30, 20)
        #cv2.imshow("Bilateral Filter",img_color)       
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)
    if(s=="Black&White"):
        cv2.imwrite("Uploads/Black&White.jpg",img_blur)
    
    img_edge = cv2.adaptiveThreshold(img_blur, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 3, 2)
    if(s=="Sketch"):
        cv2.imwrite("Uploads/Sketch.jpg",img_edge)
    #cv2.imshow("Sketch",img_edge)
    #cv2.waitKey(0)
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
    return cv2.bitwise_and(img_color, img_edge)


# In[4]:


real_inputs = []
cartoon_outputs = []

img_rgb = cv2.imread("images/kim.jpg") #input path 
#print(img_rgb.shape)
s=input("Enter the type of image: ")
output = cartoonify(img_rgb,s)
real_inputs.append(img_rgb)
cartoon_outputs.append(output)
if(s=="Painting"):
    cv2.imwrite("Uploads/Painting.jpg",output) #output path 
print("Done")    
#cv2.waitKey(0)
#cv2.destroyAllWindows()





