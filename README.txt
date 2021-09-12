Spanish

IMPORTANTE INSTALAR OPEN CV2

Se debe de tener instalado en el celular el droid cam y en el computador droid cam client, 
si quieres utilizar camara externa
Este programa esta con monedas colombianas 

Pero asi se adecuaria a tu pais
1-Hallas el radio de tu moneda, en wikipedia encuentras el diametro de tus monedas y este lo divides entre 2 y 
tienes el Radio
2-Se utiliza una hoja de tamaño A6 que tambien puedes editar en la variable de imagen_a6 ancho=x y alto=x
3-Hallas la area formula= area=pi*radio elevado a la 2
4-Transformar la area a pixeles que se hace= (radio*ancho en centimentros(10,5 en papel A6)/y se divide en 480pixeles
5-Ya tendrian el valor de las monedas en pixeles, falta que las calibren bien y listo
 
if area<13000 and area > 12000: #Aca se cambiaria los valor haciendo el calculo anterior
                font=cv.FONT_HERSHEY_SIMPLEX
                cv.putText(imagen_A6,"$1.000",(x,y),font,0.60,(0,255,0),2)#Para ponerle el texto en el mismo video en vivo del valor de la moneda
                suma1=suma1+1.000 # aca pones el valor de la moneda




English

IMPORTANTE INSTALL OPENCV2

The droid cam must be installed on the cell phone and the droid cam client on the computer,
if you want to use external camera
This program is with Colombian coins

But that's how it would suit your country
1-You find the radius of your coin, in wikipedia you find the diameter of your coins and this you divide between 2 and
you have the radio
2-An A6 size sheet is used that you can also edit in the variable image_a6 width = x and height = x
3-Find the area formula = area = pi * radius raised to 2
4-Transform the area to pixels that is made = (radius * width in centimeters (10.5 on A6 paper) / and it is divided into 480 pixels
5-They would already have the value of the coins in pixels, they need to calibrate them well and that's it
 
if area <13000 and area> 12000: #Aca would change the values ​​doing the previous calculation
                font = cv.FONT_HERSHEY_SIMPLEX
                cv.putText (image_A6, "$ 1.000", (x, y), font, 0.60, (0,255,0), 2) #To put the text in the same live video of the coin value
                sum1 = sum1 + 1.000 # you put the value of the coin
