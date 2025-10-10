import cv2
import numpy as np
import os

from skimage.filters.rank import threshold

folder = "Files"
file = "moedas.jpg"

image = cv2.imread(os.path.join(folder, file))
cv2.imshow("image", image)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold1 = 100
threshold2 = 200


def do_threshold():
    image_edges = cv2.Canny(image_gray, threshold1=threshold1, threshold2=threshold2)
    cv2.imshow("edges", image_edges)


def on_change_threshold1(val):
    global threshold1
    threshold1 = val
    do_threshold()


def on_change_threshold2(val):
    global threshold2
    threshold2 = val
    do_threshold()


cv2.namedWindow("edges")
cv2.createTrackbar("threshold1",
                   "edges",
                   threshold1,
                   255,
                   on_change_threshold1)
cv2.createTrackbar("threshold2",
                   "edges",
                   threshold2,
                   255,
                   on_change_threshold2)
cv2.waitKey(0)
