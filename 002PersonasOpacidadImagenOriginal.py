# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 09:32:06 2024

@author: jama2
"""
import cv2 
import numpy as np
imagen = cv2.imread("personas.jpg")
imagenO1 = imagen*0.3
imagenO1 = imagenO1.astype(np.uint8)
cv2.imshow("personas o",imagenO1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("personasO.jpg",imagenO1)