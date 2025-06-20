from ultralytics import YOLO
import cv2
import serial
import time

# Inicializar Arduino (ajusta COM si es diferente)
arduino = serial.Serial('COM3', 9600)
time.sleep(2)

# Cargar modelo YOLO
model = YOLO("best.pt")

# Cámara
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Espejo
    frame = cv2.flip(frame, 1)

    # Detección
    results = model(frame)
    annotated_frame = results[0].plot()

    # Inicializamos los estados
    redbull_detected = False
    porsche_detected = False
    bmw_detected = False

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            class_name = model.names[cls_id].strip()

            if class_name == "Red Bull RB18":
                redbull_detected = True
            elif class_name == "Porsche 911 GT3 RS":
                porsche_detected = True
            elif class_name == "BMW M4 DTM":
                bmw_detected = True

    # Comunicación con Arduino
    if redbull_detected:
        arduino.write(b'R')  # LED azul
    elif porsche_detected:
        arduino.write(b'P')  # LED rojo
    elif bmw_detected:
        arduino.write(b'B')  # LED verde
    else:
        arduino.write(b'N')  # Nada detectado

    # Mostrar
    cv2.imshow("F1 Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
arduino.close()
cv2.destroyAllWindows()
