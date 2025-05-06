import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen
img = cv2.imread('race.jpg')
if img is None:
    print("No se pudo cargar la imagen")
    exit()

# Convertir a diferentes espacios de color
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# Crear rangos de colores en HSV
# --- Filtro ROJO ---
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])
mask_red = cv2.inRange(img_hsv, lower_red1, upper_red1) | cv2.inRange(img_hsv, lower_red2, upper_red2)
red_result = cv2.bitwise_and(img, img, mask=mask_red)

# --- Filtro VERDE ---
lower_green = np.array([40, 40, 40])
upper_green = np.array([70, 255, 255])
mask_green = cv2.inRange(img_hsv, lower_green, upper_green)
green_result = cv2.bitwise_and(img, img, mask=mask_green)

# --- Filtro AZUL ---
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])
mask_blue = cv2.inRange(img_hsv, lower_blue, upper_blue)
blue_result = cv2.bitwise_and(img, img, mask=mask_blue)

# Mostrar todos los resultados con Matplotlib
images = [img, red_result, green_result, blue_result, img_rgb, img_yuv]
titles = ['Original (BGR)', 'Filtro Rojo', 'Filtro Verde', 'Filtro Azul', 'RGB', 'YUV']

plt.figure(figsize=(12, 8))
for i in range(6):
    plt.subplot(2, 3, i+1)
    if titles[i] in ['RGB', 'Original (BGR)']:
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    elif titles[i] == 'YUV':
        plt.imshow(images[i][:,:,0], cmap='gray')  # Mostrar canal Y como intensidad
    else:
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()

