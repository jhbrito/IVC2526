import numpy as np
import cv2
import time


imagem = np.zeros((600, 800), np.uint8)

h, w = imagem.shape
# h = imagem.shape[0]
# w = imagem.shape[1]


start = time.time()
imagem[int(h/2):, int(w/2):] = 255
end = time.time()
print("Elapsed numpy broadcast = %s" % (end - start))

# start = time.time()
# for y in range(300,600):
#     for x in range(400,800):
#         imagem[y, x] = 255
# end = time.time()
# print("Elapsed for = %s" % (end - start))

imagem[0:int(h/2), int(w/2):] = 128
imagem[int(h/2):, 0:int(w/2)] = 128


imagem_cores = np.zeros((600, 800, 3), np.uint8)
h_cores, w_cores, c_cores = imagem_cores.shape
imagem_cores[int(h_cores/2):, int(w_cores/2):, :] = 255
imagem_cores[0:int(h_cores/2), int(w_cores/2):] = [0, 0, 255]
# imagem_cores[0:int(h_cores/2), int(w_cores/2):, 0] = 0
# imagem_cores[0:int(h_cores/2), int(w_cores/2):, 1] = 0
# imagem_cores[0:int(h_cores/2), int(w_cores/2):, 2] = 255
imagem_cores[int(h_cores/2):, 0:int(w_cores/2)] = [0, 255, 255]

cv2.imshow("imagem", imagem)
cv2.imshow("imagem_cores", imagem_cores)

imagem_float = imagem / 255.0
cv2.imshow("imagem_float", imagem_float)

imagem_float_2 = imagem / 1.0
cv2.imshow("imagem_float_2", imagem_float_2)

imagem_cores_float = imagem_cores/255.0
cv2.imshow("imagem_cores_float", imagem_cores_float)

imagem_cores_float_2 = imagem_cores/1.0
cv2.imshow("imagem_cores_float_2", imagem_cores_float_2)

cv2.waitKey(0)
cv2.destroyAllWindows()

