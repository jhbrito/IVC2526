import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

folder = "Files"
files = []
files.append("baboon.png")
files.append("cao.jpg")
files.append("lena.png")
files.append("Sharbat_Gula.jpg")
files.append("moedas.jpg")

for i, file in enumerate(files):
    image = cv2.imread(os.path.join(folder, file))
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_gray = (image_gray/255.0).astype(np.float32)

    image_fft = np.fft.fft2(image_gray)

    image_fft_v = np.abs(image_fft)
    image_fft_v = image_fft_v/ np.mean(image_fft_v)

    image_fft_shift = np.fft.fftshift(image_fft)
    image_fft_shift_v = np.abs(image_fft_shift)
    image_fft_shift_v = image_fft_shift_v / np.mean(image_fft_shift_v)

    filtro_low_pass = np.zeros(image_fft_shift.shape, dtype=np.float32)
    centro_y = image_fft_shift.shape[0] / 2
    centro_x = image_fft_shift.shape[1] / 2

    raio = image_fft_shift.shape[0]/2
    for y in range(image_fft_shift.shape[0]):
        for x in range(image_fft_shift.shape[1]):
            d = np.sqrt((x-centro_x)**2 + (y-centro_y)**2)
            if d < raio:
                filtro_low_pass[y, x] = 1





    plt.subplots(dpi=300, layout='constrained')
    plt.axis('off')

    plt.subplot(5, 4, 1)
    plt.imshow(cv2.cvtColor(image_gray, cv2.COLOR_GRAY2RGB))
    plt.title("image")

    plt.subplot(5, 4, 2)
    plt.imshow(cv2.cvtColor(image_fft_v, cv2.COLOR_GRAY2RGB))
    plt.title("fft")

    plt.subplot(5, 4, 3)
    plt.imshow(cv2.cvtColor(image_fft_shift_v, cv2.COLOR_GRAY2RGB))
    plt.title("fft shift")

    plt.subplot(5, 4, 4)
    plt.imshow(cv2.cvtColor(filtro_low_pass, cv2.COLOR_GRAY2RGB))
    plt.title("filtro low pass")

    plt.show()
