import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Kernel para operaciones morfológicas
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # ----- RANGO COMPLETO PARA COLOR ROJO -----
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([179, 255, 255])

    # Crear las dos máscaras y unirlas
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Aplicar máscara a la imagen original
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # ----- FILTRADO PARA REMOVER RUIDO LINEAL -----
    blurred = cv2.GaussianBlur(res, (7, 7), 0)

    # Convertir a escala de grises para morfología
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

    # ----- OPERACIONES MORFOLÓGICAS -----
    tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
    blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

    # Mejorar imagen combinando resultados
    enhanced = cv2.add(gray, tophat)
    enhanced = cv2.subtract(enhanced, blackhat)

    # Mostrar resultados
    cv2.imshow('Original', frame)
    cv2.imshow('Mascara Roja', mask)
    cv2.imshow('Filtrado Gaussiano', blurred)
    cv2.imshow('TopHat', tophat)
    cv2.imshow('BlackHat', blackhat)
    cv2.imshow('Imagen Mejorada', enhanced)

    # Salir con ESC
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

