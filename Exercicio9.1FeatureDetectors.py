import cv2
import os

folder = "Files"
filename = "Sharbat_Gula.jpg"

image = cv2.imread(os.path.join(folder, filename))
cv2.imshow("Original", image)


image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
harris_cornerness = cv2.cornerHarris(image_gray, 2, 3, 0.04)
harris_cornerness_image = cv2.normalize(src=harris_cornerness,
                                        dst=None,
                                        alpha=0.0,
                                        beta=1.0,
                                        norm_type=cv2.NORM_MINMAX)
cv2.imshow("Harris Cornerness", harris_cornerness_image)

T = harris_cornerness.max() * 0.1

image_with_points = image.copy()
image_with_points[harris_cornerness > T] = [255, 0, 255]
cv2.imshow("Image with Harris Corners", image_with_points)

sift = cv2.SIFT_create()
sift_kp, sift_desc = sift.detectAndCompute(image, None)
image_sift = image.copy()
image_sift = cv2.drawKeypoints(image=image_sift, keypoints=sift_kp, outImage=None)
cv2.imshow("SIFT", image_sift)

# surf = cv2.xfeatures2d.SURF_create()
# surf_kp, surf_desc = surf.detectAndCompute(image, None)
# image_surf = image.copy()
# image_surf = cv2.drawKeypoints(image=image_surf, keypoints=surf_kp, outImage=None)
# cv2.imshow("SURF", image_surf)

orb = cv2.ORB_create()
orb_kp, orb_desc = orb.detectAndCompute(image, None)
image_orb = image.copy()
image_orb = cv2.drawKeypoints(image=image_orb, keypoints=orb_kp, outImage=None)
cv2.imshow("ORB", image_orb)

brisk = cv2.BRISK_create()
brisk_kp, brisk_desc = brisk.detectAndCompute(image, None)
image_brisk = image.copy()
image_brisk = cv2.drawKeypoints(image=image_brisk, keypoints=brisk_kp, outImage=None)
cv2.imshow("BRISK", image_brisk)

kaze = cv2.KAZE_create()
kaze_kp, kaze_desc = kaze.detectAndCompute(image, None)
image_kaze = image.copy()
image_kaze = cv2.drawKeypoints(image=image_kaze, keypoints=kaze_kp, outImage=None)
cv2.imshow("KAZE", image_kaze)

cv2.waitKey(0)