import cv2
import os
import numpy as np

folder = "Files"
file = "moedas.jpg"

image = cv2.imread(os.path.join(folder, file))
cv2.imshow("image", image)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_gray = image_gray/255.0

cv2.imshow("image_gray", image_gray)

def on_track_bar(value):
    threshold = value/100.0
    ret, image_thresholded = cv2.threshold(image_gray,
                                           threshold,
                                           1.0,
                                           cv2.THRESH_BINARY)
    cv2.imshow("image_thresholded", image_thresholded)


cv2.namedWindow("image_thresholded")
cv2.createTrackbar("Threshold",
                   "image_thresholded",
                   50,
                   100,
                   on_track_bar)

threshold_media = np.mean(image_gray)
ret, image_thresholded_media = cv2.threshold(image_gray,
                                             threshold_media,
                                             1.0,
                                             type=cv2.THRESH_BINARY)
cv2.imshow("image_thresholded_media", image_thresholded_media)

ret, image_thresholded_otsu = cv2.threshold((image_gray*255).astype(dtype=np.uint8),
                                            thresh=0,
                                            maxval=255,
                                            type = (cv2.THRESH_BINARY | cv2.THRESH_OTSU))
cv2.imshow("image_thresholded_otsu", image_thresholded_otsu)

image_thres_adapt_mean = cv2.adaptiveThreshold((image_gray*255).astype(dtype=np.uint8),
                                               maxValue=255,
                                               adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
                                               C=-3,
                                               blockSize=11,
                                               thresholdType=cv2.THRESH_BINARY
                                               )
cv2.imshow("image_thres_adapt_mean", image_thres_adapt_mean)

image_thres_adapt_gaussian = cv2.adaptiveThreshold((image_gray*255).astype(dtype=np.uint8),
                                                   maxValue=255,
                                                   adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                   C = -3,
                                                   blockSize=11,
                                                   thresholdType=cv2.THRESH_BINARY)
cv2.imshow("image_thres_adapt_gaussian", image_thres_adapt_gaussian)


cv2.waitKey(0)
