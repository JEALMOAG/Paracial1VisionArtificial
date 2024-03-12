# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:57:16 2024

@author: jama2
"""

import cv2 
import numpy as np

def clasificador(imagen):
    m,n,c = imagen.shape
    imagenBn = np.zeros((m,n))
    for x in range(m):
        for y in range(n):
            if 15<imagen[x,y,0]<132 and 20<imagen[x,y,1]<175 and 50<imagen[x,y,2]<225:
                imagenBn[x,y]=255
    cv2.imwrite("personasBn2.jpg", imagenBn)
    return imagenBn

imagen = cv2.imread("personas.jpg")
imagenBn = clasificador(imagen)
cv2.imshow("peronasBN2",imagenBn)
cv2.waitKey(0)
cv2.destroyAllWindows()
