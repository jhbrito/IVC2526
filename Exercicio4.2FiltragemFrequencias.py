import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

folder = "Files"
files = []
files.append("riscas horizontais")
files.append("riscas verticais")
files.append("quadrado")
files.append("baboon.png")
files.append("cao.jpg")
files.append("lena.png")
files.append("Sharbat_Gula.jpg")
files.append("moedas.jpg")

for i, file in enumerate(files):
    if file == "riscas horizontais":
        image = np.zeros((256,256,3), np.uint8)
        image[0:32, :, :] = 255
        image[64:96, :, :] = 255
        image[128:160, :, :] = 255
        image[192:224, :, :] = 255
    elif file == "riscas verticais":
        image = np.zeros((256, 256, 3), np.uint8)
        image[:, 0:64, :] = 255
        image[:, 128:196, :] = 255
    elif file == "quadrado":
        image = np.zeros((256, 256, 3), np.uint8)
        image[64:128, 64:128, :] = 255
    else:
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

    raio = np.min(image_fft_shift.shape)/ 2
    raio /= 4

    for y in range(filtro_low_pass.shape[0]):
        for x in range(filtro_low_pass.shape[1]):
            d = np.sqrt((x-centro_x)**2 + (y-centro_y)**2)
            if d < raio:
                filtro_low_pass[y, x] = 1

    image_fft_shift_filtered = image_fft_shift * filtro_low_pass
    image_fft_shift_filtered_v = np.abs(image_fft_shift_filtered)
    image_fft_shift_filtered_v = image_fft_shift_filtered_v / np.mean(image_fft_shift_filtered_v)

    image_fft_shift_filtered_unshift = np.fft.ifftshift(image_fft_shift_filtered)
    image_fft_shift_filtered_unshift_v = np.abs(image_fft_shift_filtered_unshift)
    image_fft_shift_filtered_unshift_v = image_fft_shift_filtered_unshift_v / np.mean(image_fft_shift_filtered_unshift_v)

    image_fft_shift_filtered_unshift_ifft = np.fft.ifft2(image_fft_shift_filtered_unshift)
    image_filtered = np.abs(image_fft_shift_filtered_unshift_ifft)


    plt.subplots(dpi=300, layout='constrained')
    plt.axis('off')

    plt.subplot(3, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Imagem original")
    plt.axis('off')

    plt.subplot(3, 3, 4)
    plt.imshow(cv2.cvtColor(image_gray, cv2.COLOR_GRAY2RGB))
    plt.title("Imagem grayscale")
    plt.axis('off')

    plt.subplot(3, 3, 5)
    plt.imshow(cv2.cvtColor(image_fft_v, cv2.COLOR_GRAY2RGB))
    plt.title("Espectro")
    plt.axis('off')

    plt.subplot(3, 3, 6)
    plt.imshow(cv2.cvtColor(image_fft_shift_v, cv2.COLOR_GRAY2RGB))
    plt.title("Espectro shift")
    plt.axis('off')

    plt.subplot(3, 3, 3)
    plt.imshow(cv2.cvtColor(filtro_low_pass, cv2.COLOR_GRAY2RGB))
    plt.title("Filtro low pass")
    plt.axis('off')

    plt.subplot(3, 3, 9)
    plt.imshow(cv2.cvtColor(image_fft_shift_filtered_v, cv2.COLOR_GRAY2RGB))
    plt.title("Espectro filtrado")
    plt.axis('off')
    #
    plt.subplot(3, 3, 8)
    plt.imshow(cv2.cvtColor(image_fft_shift_filtered_unshift_v, cv2.COLOR_GRAY2RGB))
    plt.title("Espectro filtrado unshift")
    plt.axis('off')

    plt.subplot(3, 3, 7)
    plt.imshow(cv2.cvtColor(image_filtered, cv2.COLOR_GRAY2RGB))
    plt.title("Imagem filtrada")
    plt.axis('off')

    plt.show()
