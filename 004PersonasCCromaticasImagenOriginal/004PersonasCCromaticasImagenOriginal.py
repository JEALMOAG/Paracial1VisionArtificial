
import cv2
import numpy as np

def calcular_cromaticidad(imagen):
    # Convertir la imagen a tipo float32 para realizar cálculos precisos
    imagen_float = imagen.astype(np.float32)
    imagen_cromatica = imagen.astype(np.float32)
    
    # Obtener dimensiones de la imagen
    x, y, z = imagen_cromatica.shape
    
    # Calcular la cromaticidad para cada píxel
    for j in range(x):
        for i in range(y):
            suma = imagen_float[j, i, 0] + imagen_float[j, i, 1] + imagen_float[j, i, 2]
            imagen_cromatica[j, i, 0] = imagen_float[j, i, 0] / suma
            imagen_cromatica[j, i, 1] = imagen_float[j, i, 1] / suma
            imagen_cromatica[j, i, 2] = imagen_float[j, i, 2] / suma
    
    # Convertir la imagen a tipo uint8 para su visualización y guardado
    imagen_cromatica = (imagen_cromatica * 255).astype(np.uint8)
    
    return imagen_cromatica


imagen = cv2.imread("personas.jpg")


#IMAGEN 1

imagenCr= calcular_cromaticidad(imagen)
cv2.imshow("personasCrOriginal", imagenCr)
cv2.imwrite("personasCrOriginal.jpg", imagenCr)
cv2.waitKey(0)
cv2.destroyAllWindows()


#IMAGEN 2

imagenO1=imagen*0.6
imagenO1=imagenO1.astype(np.uint8)
cv2.imwrite("personasO1-40.jpg",imagenO1)
cv2.imshow("personasO1-40", imagenO1)
cv2.waitKey(0);
cv2.destroyAllWindows()

imagenCrO1= calcular_cromaticidad(imagenO1)
cv2.imshow("personasCrO1-40", imagenCrO1)
cv2.imwrite("personasCrO1-40.jpg", imagenCrO1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#IMAGEN 3

imagenO2=imagen*0.3
imagenO2=imagenO2.astype(np.uint8)
cv2.imwrite("personasO1-70.jpg",imagenO2)
cv2.imshow("personasO1-70", imagenO2)
cv2.waitKey(0);
cv2.destroyAllWindows()

imagenCrO2= calcular_cromaticidad(imagenO2)
cv2.imshow("personasCrO2-70", imagenCrO2)
cv2.imwrite("personasCrO2-70.jpg", imagenCrO2)
cv2.waitKey(0)
cv2.destroyAllWindows()
