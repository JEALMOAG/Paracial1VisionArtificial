# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 19:26:22 2024

@author: jama2
"""

import cv2
import numpy as np

imagen=cv2.imread("personas.jpg")
cv2.imshow("Personas",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

imagenO1=imagen*0.7
imagenO1=imagenO1.astype(np.uint8)
cv2.imshow("peronasO-30",imagenO1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("personasO-30.jpg", imagenO1)

img = cv2.imread('personasO-30.jpg', 1)
clone = img.copy() 
cv2.waitKey(0)
cv2.destroyAllWindows()
h_start, w_start, h_width, w_width = 312, 773, 5, 5
image = clone
image_patch = image[h_start:h_start+h_width, w_start:w_start+w_width]
image_normalized = image / image_patch.max(axis=(0, 1))
image_balanced = image_normalized.clip(0,1)
cv2.imshow("personasO-30WP", image_balanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
image_balanced_8bit = (image_balanced*255).astype(int)
cv2.imwrite("personasO-30WP.jpg", image_balanced_8bit)

imagenO2=imagen*0.5
imagenO2=imagenO2.astype(np.uint8)
cv2.imshow("personasO-50",imagenO2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("personasO-50.jpg", imagenO2)

img = cv2.imread('personasO-50.jpg', 1)
clone = img.copy() 
cv2.waitKey(0)
cv2.destroyAllWindows()
h_start, w_start, h_width, w_width = 312, 773, 5, 5
image = clone
image_patch = image[h_start:h_start+h_width, w_start:w_start+w_width]
image_normalized = image / image_patch.max(axis=(0, 1))
image_balanced = image_normalized.clip(0,1)
cv2.imshow("personasO-50WP", image_balanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
image_balanced_8bit = (image_balanced*255).astype(int)
cv2.imwrite("personasO-50WP.png", image_balanced_8bit)

imagenc1=imagen.copy()
imagenc1[:,:,0]=imagenc1[:,:,0]+170
cv2.imwrite("personasYellowBackground.jpg", imagenc1)
cv2.imshow("personasYellowBackground",imagenc1)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('personasYellowBackground.jpg', 1)
clone = img.copy() 
cv2.waitKey(0)
cv2.destroyAllWindows()
h_start, w_start, h_width, w_width = 312, 773, 5, 5
image = clone
image_patch = image[h_start:h_start+h_width, w_start:w_start+w_width]
image_normalized = image / image_patch.max(axis=(0, 1))
image_balanced = image_normalized.clip(0,1)
cv2.imshow("personasYellowBackgroundWP", image_balanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
image_balanced_8bit = (image_balanced*255).astype(int)
cv2.imwrite("personasYellowBackgroundWP.jpg", image_balanced_8bit)

imagenc2=imagen.copy()
imagenc2[:,:,1]=imagenc2[:,:,1]+180
cv2.imwrite("personasPurpleBackground.jpg", imagenc2)
cv2.imshow("personasPurpleBackground",imagenc2)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('personasPurpleBackground.jpg', 1)
clone = img.copy() 
cv2.waitKey(0)
cv2.destroyAllWindows()
h_start, w_start, h_width, w_width = 312, 773, 5, 5
image = clone
image_patch = image[h_start:h_start+h_width, w_start:w_start+w_width]
image_normalized = image / image_patch.max(axis=(0, 1))
image_balanced = image_normalized.clip(0,1)
cv2.imshow("personasPurpleBackgroundWP", image_balanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
image_balanced_8bit = (image_balanced*255).astype(int)
cv2.imwrite("personasPurpleBackgroundWP.jpg", image_balanced_8bit)
################

imagenc3=imagen.copy()
imagenc3[:,:,2]=imagenc3[:,:,2]+190
cv2.imwrite("personasBlueBackground.jpg", imagenc3)
cv2.imshow("personasBlueBackground",imagenc3)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('personasBlueBackground.jpg', 1)
clone = img.copy() 
cv2.waitKey(0)
cv2.destroyAllWindows()
h_start, w_start, h_width, w_width = 312, 773, 5, 5
image = clone
image_patch = image[h_start:h_start+h_width, w_start:w_start+w_width]
image_normalized = image / image_patch.max(axis=(0, 1))
image_balanced = image_normalized.clip(0,1)
cv2.imshow("personasBlueBackgroundWP", image_balanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
image_balanced_8bit = (image_balanced*255).astype(int)
cv2.imwrite("personasBlueBackgroundWP.png", image_balanced_8bit)