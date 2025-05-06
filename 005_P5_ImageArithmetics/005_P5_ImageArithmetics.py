import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leer imagen en escala de grises
img = cv2.imread('bookpage.jpg', cv2.IMREAD_GRAYSCALE)

# Verifica si cargó bien la imagen
if img is None:
    print("No se pudo cargar la imagen")
    exit()

# 1-5: Métodos de thresholding simples
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, binary_inv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, trunc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, tozero = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, tozero_inv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

# 6-7: Umbrales adaptativos
mean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                             cv2.THRESH_BINARY, 11, 2)
gaussian = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 11, 2)

# 8: Otsu (automático)
_, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Mostrar todo con Matplotlib
titles = ['Original', 'Binary', 'Binary Inv', 'Trunc',
          'ToZero', 'ToZero Inv', 'Adaptive Mean', 'Adaptive Gaussian', 'Otsu']
images = [img, binary, binary_inv, trunc,
          tozero, tozero_inv, mean, gaussian, otsu]

plt.figure(figsize=(15, 10))
for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
