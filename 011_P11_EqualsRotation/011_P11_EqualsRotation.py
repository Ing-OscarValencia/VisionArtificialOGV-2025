import cv2 
import numpy as np 
 
cap = cv2.VideoCapture(0)  # Usa la webcam (puedes poner un video .mp4 si quieres) 
 
ret, frame1 = cap.read() 
ret, frame2 = cap.read() 
 
while cap.isOpened(): 
    # Calcular la diferencia absoluta entre dos frames 
    diff = cv2.absdiff(frame1, frame2) 
     
    # Convertir a escala de grises 
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) 
 
    # Aplicar desenfoque para reducir ruido 
    blur = cv2.GaussianBlur(gray, (5,5), 0)

   # Aplicar umbral para binarizar el movimiento 
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) 
 
    # Dilatar para rellenar huecos 
    dilated = cv2.dilate(thresh, None, iterations=3) 
 
    # Encontrar contornos (zonas en movimiento) 
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, 
cv2.CHAIN_APPROX_SIMPLE) 
 
    # Dibujar rectángulos en zonas de movimiento 
    for contour in contours: 
        if cv2.contourArea(contour) < 700:  # Ignorar movimiento pequeño 
            continue 
        x, y, w, h = cv2.boundingRect(contour) 
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2) 
 
    # Mostrar los resultados 
    cv2.imshow("Video original", frame1) 
    cv2.imshow("Movimiento detectado", dilated) 
 
    # Actualizar frames 
    frame1 = frame2 
    ret, frame2 = cap.read() 
 
    # Salir con 'ESC' 
    if cv2.waitKey(30) & 0xFF == 27: 
        break 
 
cap.release() 
cv2.destroyAllWindows()    
