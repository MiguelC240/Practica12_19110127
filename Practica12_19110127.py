import numpy as np
import cv2

Img = cv2.imread('Carro.jpg')
Res_Img1 = cv2.resize(Img, (400,400))
gray = cv2.cvtColor(Res_Img1,cv2.COLOR_RGB2GRAY)

forma = np.shape(gray)
Img2 = np.zeros(forma)

h = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])


for x in list(range(1,forma[1]-1)):
    
    for y in list(range(1,forma[1]-1)):
        suma = 0
        
        for i in list(range(-1,2)):

            for j in list(range(-1,2)):
                suma = gray[x-i,y-j]*h[i+1,j+1]+suma

        Img2[x,y] = suma
            
maxs = np.max(Img2) 

                 

Img2 = Img2 * 255 / maxs


Img2 = Img2.astype(np.uint8)

cv2.imshow('Imagen original',gray)
cv2.imshow('Imagen filtrada',Img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
