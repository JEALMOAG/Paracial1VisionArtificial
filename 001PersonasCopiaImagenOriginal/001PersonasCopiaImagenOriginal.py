# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:46:29 2024

@author: jama2
"""

import cv2 
import numpy as np

imagen = cv2.imread("personas.jpg")
m,n,c = imagen.shape
cv2.imshow("personas", imagen)# Muestra la imagen, tomando la imgenen de entrada\
    # y mostrandola en otro
cv2.waitKey(0)#hace un delay en microsengundos o hasta que le usuario presiona \
    #una tecla.
cv2.destroyAllWindows()# cierra la ventana emergente cuando el usuario quiera.
cv2.imwrite("personasCopy.jpg",imagen)#guarda la imagen en un archivo. Toma la \
    # imagen y la ruta del archivo.
    
