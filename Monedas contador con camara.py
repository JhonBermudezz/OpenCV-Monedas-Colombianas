import cv2 as cv
import numpy as np
from numpy.lib.function_base import iterable
def ordenaspuntos(puntos):
    n_puntos=np.concatenate([puntos[0],puntos[1],puntos[2],puntos[3]]).tolist()
    y_corde=sorted(n_puntos,key=lambda n_puntos: n_puntos[1])
    x1_order=y_corde[:2]
    x1_order=sorted(x1_order,key=lambda x1_order: x1_order[0])
    x2_order=y_corde[2:4]
    x2_order=sorted(x2_order,key=lambda x2_order: x2_order[0])
    return[x1_order[0],x1_order[1],x2_order[0],x2_order[1]]
def aliniamiento(image,ancho,alto):
    image_alineada=None
    grises=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    tipoumbral,umbral=cv.threshold(grises,150,255,cv.THRESH_BINARY)
    cv.imshow("Umbral",umbral)
    contorno=cv.findContours(umbral,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)[0]
    contorno=sorted(contorno,key=cv.contourArea,reverse=True)[:1]
    for c in contorno:
        epsilon=0.01*cv.arcLength(c,True)
        appox=cv.approxPolyDP(c,epsilon,True)
        if len(appox)==4:
            puntos=ordenaspuntos(appox)
            puntos1=np.float32(puntos)
            puntos2=np.float32([[0,0],[ancho,0],[0,alto],[ancho,alto]])#[x,y]
            M = cv.getPerspectiveTransform(puntos1,puntos2)
            image_alineada=cv.warpPerspective(image,M,(ancho,alto))
    return image_alineada
capturevideo=cv.VideoCapture(1)#0= si se utiliza la camra del pc y #1 si se utiliza el celular con droidcam
while True:
    tipocamara,camara=capturevideo.read()
    if tipocamara==False:
        break
    imagen_A6=aliniamiento(camara,ancho=480,alto=677)
    if imagen_A6 is not None:
        puntos=[]
        imagen_gris=cv.cvtColor(imagen_A6,cv.COLOR_BGR2GRAY)
        blur=cv.GaussianBlur(imagen_gris,(5,5),1)
        _,umbral2=cv.threshold(blur,0,255,cv.THRESH_OTSU+cv.THRESH_BINARY_INV)
        cv.imshow("Umbral",umbral2)
        contorno2=cv.findContours(umbral2,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)[0]
        cv.drawContours(imagen_A6,contorno2,-1,(255,0,0),2)#colores rgb
        suma1=0.0
        suma2=0.0
        suma3=0.0
        suma4=0.0
        suma5=0.0
        for c_2 in contorno2:
            area=cv.contourArea(c_2)
            Momentos = cv.moments(c_2)
            if (Momentos["m00"]==0):#momentos estaticos
                Momentos["m00"]=1.0
            x=int(Momentos["m10"]/Momentos["m00"])#momentos de movimiento
            y=int(Momentos["m01"]/Momentos["m00"])
            if area<13000 and area > 12000:#Rango del area de las monedas de 1000 pesos colombianos
                font=cv.FONT_HERSHEY_SIMPLEX
                cv.putText(imagen_A6,"$1.000",(x,y),font,0.60,(0,255,0),2)#Para ponerle el texto en el mismo video en vivo del valor de la moneda
                suma1=suma1+1.000
            if area<10000 and area > 9400:#Rango del area de las monedas de 500 pesos colombianos
                font=cv.FONT_HERSHEY_SIMPLEX
                cv.putText(imagen_A6,"$500",(x,y),font,0.60,(0,255,0),2)
                suma2=suma2+500
            if area<8800 and area > 8000:#Rango del area de las monedas de 200 pesos colombianos
                font=cv.FONT_HERSHEY_SIMPLEX
                cv.putText(imagen_A6,"$200",(x,y),font,0.60,(0,255,0),2)
                suma3=suma3+200
            if area<7400 and area > 6500:#Rango del area de las monedas de 100 pesos colombianos
                font=cv.FONT_HERSHEY_SIMPLEX
                cv.putText(imagen_A6,"$100",(x,y),font,0.60,(0,255,0),2)
                suma4=suma4+100
            if area<5400 and area > 4500:#Rango del area de las monedas de 50 pesos colombianos
                font=cv.FONT_HERSHEY_SIMPLEX
                cv.putText(imagen_A6,"$50",(x,y),font,0.60,(0,255,0),2)
                suma5=suma5+50
        total=suma1+suma2+suma3+suma4+suma5
        print("Sumatoria total",round(total,2))
        cv.imshow("Imagen A6",imagen_A6)
        cv.imshow("Camara",camara)
    if cv.waitKey(1) == ord('q'):#Para para el programa
        break
capturevideo.release()
cv.destroyAllWindows()



 
            



