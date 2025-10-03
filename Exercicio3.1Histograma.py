import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

def ivc_gray_pdf(image_gray):
    # histogram = cv2.calcHist(image_gray, [0], None, [256], [0, 256])
    # histogram = histogram / (image_gray.shape[0] * image_gray.shape[1])

    # histogram = np.histogram(image_gray, bins=256)

    histogram = np.zeros((256,), dtype=np.uint32)

    # for i in range(0, 255):
    #     for y in range(image_gray.shape[0]):
    #         for x in range(image_gray.shape[1]):
    #             if image_gray[y][x] == i:
    #                 histogram[i] += 1

    for i in range(0, 255):
        histogram[i] = np.sum(image_gray == i)
    pdf = histogram / (image_gray.shape[0] * image_gray.shape[1])
    return pdf


def ivc_pdf_2_cdf(pdf):
    # cdf = np.cumsum(pdf)
    cdf = np.zeros(pdf.shape, dtype=pdf.dtype)
    cdf[0] = pdf[0]
    for i in range(1, cdf.shape[0]):
        cdf[i] = cdf[i - 1] + pdf[i]

    return cdf


def ivc_equalize_gray(image_gray, cdf):
    cdf_min = cdf[0]
    g = np.zeros(image_gray.shape, dtype=image_gray.dtype)
    for y in range(image_gray.shape[0]):
        for x in range(image_gray.shape[1]):
            g[y, x] = ((cdf[image_gray[y, x]] - cdf_min) / (1 - cdf_min)) * 255
    return g

folder = "Files"
files = []
files.append("baboon.png")
files.append("cao.jpg")
files.append("lena.png")
files.append("Sharbat_Gula.jpg")


for i, file in enumerate(files):
    image = cv2.imread(os.path.join(folder, file))
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    pdf = ivc_gray_pdf(image_gray)
    cdf = ivc_pdf_2_cdf(pdf)
    g = ivc_equalize_gray(image_gray, cdf)
    pdf_g = ivc_gray_pdf(g)
    cdf_g = ivc_pdf_2_cdf(pdf_g)

    plt.subplot(4, 7, i*7+1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("image")
    plt.xticks([])
    plt.yticks([])
    plt.subplot(4, 7, i*7+2)
    plt.imshow(cv2.cvtColor(image_gray, cv2.COLOR_GRAY2RGB))
    plt.title("gray")
    plt.xticks([])
    plt.yticks([])
    plt.subplot(4, 7, i*7+3)
    plt.bar(range(256), pdf)
    plt.title("pdf")
    plt.subplot(4, 7, i*7+4)
    plt.plot(cdf)
    plt.title("cdf")
    plt.subplot(4, 7, i*7+5)
    plt.imshow(cv2.cvtColor(g, cv2.COLOR_GRAY2RGB))
    plt.title("g")
    plt.xticks([])
    plt.yticks([])
    plt.subplot(4, 7, i*7+6)
    plt.bar(range(256), pdf_g)
    plt.title("pdf_g")
    plt.subplot(4, 7, i*7+7)
    plt.plot(cdf_g)
    plt.title("cdf_g")


plt.show()

