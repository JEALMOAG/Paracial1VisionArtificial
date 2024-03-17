# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 18:59:52 2024

@author: jama2
"""

import cv2 
import numpy as np 
imagen = cv2.imread("personas.jpg")
m,n,c = imagen.shape
imagenc = imagen.copy()
imagenc = imagenc.astype(np.float32)
imagenc = imagen.astype(np.float32)

for x in range(m):
    for y in range(n):
        imagenc[x,y,0]=imagen[x,y,0]/imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2]
        imagenc[x,y,1]=imagen[x,y,1]/imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2]
        imagenc[x,y,2]=imagen[x,y,2]/imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2]

cv2.imshow("PersonasCromatricas",imagenc)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("personasCr.jpg", imagenc)
