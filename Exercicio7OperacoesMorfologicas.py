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

kernel = np.ones((3, 3), np.uint8)

def on_track_bar(value):
    threshold = value/100.0
    ret, image_thresholded = cv2.threshold(image_gray,
                                           threshold,
                                           255,
                                           cv2.THRESH_BINARY)
    cv2.imshow("image_thresholded", image_thresholded)

    image_erode = cv2.erode(image_thresholded, kernel)
    cv2.imshow("image_erode", image_erode)

    image_dilate = cv2.dilate(image_thresholded, kernel)
    cv2.imshow("image_dilate", image_dilate)

    image_erode2 = cv2.morphologyEx(image_thresholded, cv2.MORPH_ERODE, kernel)
    cv2.imshow("image_erode2", image_erode2)

    image_dilate2 = cv2.morphologyEx(image_thresholded, cv2.MORPH_DILATE, kernel)
    cv2.imshow("image_dilate2", image_dilate2)

    image_close = cv2.erode(cv2.dilate(image_thresholded, kernel), kernel)
    cv2.imshow("image_close", image_close)

    image_open = cv2.dilate(cv2.erode(image_thresholded, kernel), kernel)
    cv2.imshow("image_open", image_open)

    image_close2 = cv2.morphologyEx(image_thresholded, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("image_close2", image_close2)

    image_open2 = cv2.morphologyEx(image_thresholded, cv2.MORPH_OPEN, kernel)
    cv2.imshow("image_open2", image_open2)





cv2.namedWindow("image_thresholded")
cv2.createTrackbar("Threshold",
                   "image_thresholded",
                   50,
                   100,
                   on_track_bar)

cv2.waitKey(0)
