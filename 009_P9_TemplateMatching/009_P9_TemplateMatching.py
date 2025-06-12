import numpy as np
import cv2

# Cargar imagen y template
img_rgb = cv2.imread('carritos.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('template_casilla.jpg', 0)

# Obtener dimensiones
w, h = template.shape[::-1]

# Realizar match
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.85
loc = np.where(res >= threshold)

# Dibujar rectángulos donde se detecte el ROI
detecciones = 0
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
    detecciones += 1

print(f'Detecciones encontradas con score >= {threshold}: {detecciones}')

# Redimensionar para ver en pantalla
scale_percent = 50
resized = cv2.resize(img_rgb, (int(img_rgb.shape[1]*scale_percent/100), int(img_rgb.shape[0]*scale_percent/100)))
cv2.imshow("Detecciones de ROI", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
