import cv2
import os
import numpy as np
from PIL import Image
import skimage
import matplotlib.pyplot as plt


folder = "Files"
file = "Sharbat_Gula.jpg"

file_path = os.path.join(folder, file)

image_opencv = cv2.imread(file_path)
image_pil = Image.open(file_path)
# image_pil.show()
image_pil_np = np.array(image_pil)
image_skimage = skimage.io.imread(file_path)


cv2.imshow("image_opencv imshow", image_opencv)

cv2.imshow("image_pil imshow", image_pil_np)
cv2.imshow("image_pil imshow BGR", cv2.cvtColor(image_pil_np, cv2.COLOR_RGB2BGR))

cv2.imshow("image_skimage imshow", image_skimage)
cv2.imshow("image_skimage imshow BGR", cv2.cvtColor(image_skimage, cv2.COLOR_RGB2BGR))

plt.figure()
plt.subplot(2, 3, 1)
plt.imshow(image_opencv)
plt.axis('off')
plt.title("OpenCV (BGR)")

plt.subplot(2, 3, 2)
plt.imshow(image_pil_np)
plt.title("PIL (RGB)")
plt.axis('off')
plt.subplot(2, 3, 3)
plt.imshow(cv2.cvtColor(image_pil_np, cv2.COLOR_RGB2BGR))
plt.title("PIL->BGR")
plt.axis('off')
plt.subplot(2, 3, 4)
plt.imshow(image_skimage)
plt.title("Skimage (RGB)")
plt.axis('off')
plt.subplot(2, 3, 5)
plt.imshow(cv2.cvtColor(image_skimage, cv2.COLOR_RGB2BGR))
plt.title("Skimage->BGR")
plt.axis('off')
plt.subplot(2, 3, 6)
plt.imshow(image_pil)
plt.title("PIL native")
plt.axis('off')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
