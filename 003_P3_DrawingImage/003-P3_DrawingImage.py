import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen a color
img_color = cv2.imread('watch.jpg')
if img_color is None:
    print("No se pudo cargar la imagen.")
    exit()

# Convertir a YCrCb
img_ycrcb = cv2.cvtColor(img_color, cv2.COLOR_BGR2YCrCb)
y, cr, cb = cv2.split(img_ycrcb)

# Histograma del canal Y original
hist_y = cv2.calcHist([y], [0], None, [256], [0, 256])

# Ecualización del canal Y
y_eq = cv2.equalizeHist(y)

# Histograma del canal Y ecualizado
hist_y_eq = cv2.calcHist([y_eq], [0], None, [256], [0, 256])

# Recomponer imagen ecualizada en YCrCb y luego a BGR
img_ycrcb_eq = cv2.merge([y_eq, cr, cb])
img_color_eq = cv2.cvtColor(img_ycrcb_eq, cv2.COLOR_YCrCb2BGR)

# Convertir imágenes a RGB para matplotlib (cv2 usa BGR)
img_color_rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
img_color_eq_rgb = cv2.cvtColor(img_color_eq, cv2.COLOR_BGR2RGB)

# Mostrar resultados
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.imshow(img_color_rgb)
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.plot(hist_y, color='black')
plt.title('Histograma Canal Y (Original)')
plt.xlim([0, 256])

plt.subplot(2, 2, 3)
plt.imshow(img_color_eq_rgb)
plt.title('Imagen Ecualizada')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.plot(hist_y_eq, color='black')
plt.title('Histograma Canal Y (Ecualizado)')
plt.xlim([0, 256])

plt.tight_layout()
plt.show()
