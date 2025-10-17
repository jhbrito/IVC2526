import cv2
import os
import numpy as np
from networkx.algorithms.distance_measures import center

folder = "Files"
file = "moedas.jpg"

image = cv2.imread(os.path.join(folder, file))
cv2.imshow("image", image)

image_gray = cv2.cvtColor(src=image,code=cv2.COLOR_BGR2GRAY)
image_gray = image_gray/255.0

cv2.imshow(winname="image_gray",mat=image_gray)

def on_track_bar(value):
    threshold = value/100.0
    ret, image_thresholded = cv2.threshold(src=image_gray,
                                           thresh=threshold,
                                           maxval=1,
                                           type=cv2.THRESH_BINARY)
    cv2.imshow(winname="image_thresholded",mat=image_thresholded)

    image_thresholded = (image_thresholded * 255).astype(np.uint8)

    contours, hierarchy = cv2.findContours(image=image_thresholded,
                                           mode=cv2.RETR_EXTERNAL,
                                           method=cv2.CHAIN_APPROX_NONE)
    image_contours = np.zeros(image_thresholded.shape, np.uint8)
    cv2.drawContours(image=image_contours,
                     contours=contours,
                     contourIdx=-1,
                     color=255,
                     thickness=-1)
    cv2.imshow(winname="image_contours", mat=image_contours)

    image_contours2 = np.zeros(image_thresholded.shape, np.uint8)
    image_circles = np.zeros(image.shape, np.uint8)

    for i in range(len(contours)):
        cv2.drawContours(image=image_contours2,
                         contours=contours,
                         contourIdx=i,
                         color=255,
                         thickness=1)
        contour = contours[i]
        c_area = cv2.contourArea(contour=contour)
        p = cv2.arcLength(curve=contour, closed=True)
        print("contour {} area = {}; perimeter={}".format(i, c_area, p))

        cv2.drawContours(image=image_circles,
                         contours=contours,
                         contourIdx=i,
                         color=(0, 255, 255),
                         thickness=1)
        M = cv2.moments(array=contour)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.circle(img=image_circles,
                   center=(cX, cY),
                   radius=5,
                   color=(0, 0, 255),
                   thickness=-1)

    cv2.imshow("image_contours2", image_contours2)
    cv2.imshow("image_circles", image_circles)

    i_max_area = -1
    i_min_area = -1
    max_area = 0
    min_area = np.iinfo(np.int32).max

    for i in range(len(contours)):
        contour = contours[i]
        c_area = cv2.contourArea(contour=contour)
        if c_area > max_area:
            max_area = c_area
            i_max_area = i
        if c_area < min_area:
            min_area = c_area
            i_min_area = i

    image_contours_color = np.zeros(image.shape, np.uint8)

    for i in range(len(contours)):
        if i == i_max_area:
            cv2.drawContours(image=image_contours_color,
                             contours=contours,
                             contourIdx=i,
                             color=(0, 255, 0),
                             thickness=-1)
        elif i == i_min_area:
            cv2.drawContours(image=image_contours_color,
                             contours=contours,
                             contourIdx=i,
                             color=(0, 0, 255),
                             thickness=-1)
        else:
            cv2.drawContours(image=image_contours_color,
                             contours=contours,
                             contourIdx=i,
                             color=(255, 255, 255),
                             thickness=-1)
    cv2.imshow("image_contours_color", image_contours_color)


    image_largest_contour = np.zeros(image.shape, np.uint8)
    cv2.drawContours(image=image_largest_contour,
                     contours=contours,
                     contourIdx=i_max_area,
                     color=(1, 1, 1),
                     thickness=-1)
    image_biggest_coin = image.copy()
    image_biggest_coin = image_biggest_coin * image_largest_contour

    cv2.imshow("image_largest_contour", image_largest_contour*255)
    cv2.imshow("image_biggest_coin", image_biggest_coin)


cv2.namedWindow("image_thresholded")
cv2.createTrackbar("Threshold",
                   "image_thresholded",
                   50,
                   100,
                   on_track_bar)

cv2.waitKey(0)
