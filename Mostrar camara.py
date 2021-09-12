import cv2 as cv
#0 para la camara del pc y 1 para camara externa
capturevideo=cv.VideoCapture(1)
if not capturevideo.isOpened():
    print("No se encontro una camara.")
    exit()
while True:
    tipocamara,frame=capturevideo.read()
    grises=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow("Mostra camara",frame)
    if cv.waitKey(1)==ord("q"):
        break
capturevideo.release()
cv.destroyAllWindows()