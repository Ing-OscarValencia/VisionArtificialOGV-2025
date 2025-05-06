import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leer imagen
img = cv2.imread('watch.jpg')
if img is None:
    print("No se pudo cargar la imagen.")
    exit()

# Dibujo sobre la imagen
cv2.line(img, (0, 0), (150, 150), (255, 0, 0), 5)              # Línea azul
cv2.rectangle(img, (50, 50), (200, 150), (0, 255, 0), 3)       # Rectángulo verde
cv2.circle(img, (300, 100), 40, (0, 0, 255), -1)               # Círculo rojo lleno
cv2.putText(img, 'OpenCV Demo', (10, 250), cv2.FONT_HERSHEY_SIMPLEX,
            1, (255, 255, 255), 2, cv2.LINE_AA)                # Texto blanco

# Región de interés (ROI)
roi = img[50:150, 50:150]      # ROI de 100x100
img[0:100, 200:300] = roi     # Pegamos la ROI en otra parte

# Convertir a RGB para mostrar con matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Mostrar imagen con matplotlib
plt.figure(figsize=(8, 6))
plt.imshow(img_rgb)
plt.title('Dibujo y ROI sobre la Imagen')
plt.axis('off')
plt.tight_layout()
plt.show()
