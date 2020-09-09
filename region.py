import numpy as np
import cv2


def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([[(200, height), (1100, height), (550, 250)]])  # Triangle polygon because cv2.fillPoly expects an array of polygons.
    mask = np.zeros_like(image)  # Create a black mask to apply the above Triangle on.
    cv2.fillPoly(mask, polygons, 255)  # A complete white triangle polygon on a black mask.
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # Kernel size is 5x5
    canny = cv2.Canny(blur, 50, 150)
    return canny


image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
canny_image = canny(lane_image)
cropped_image = region_of_interest(canny_image)
cv2.imshow('image', cropped_image)
cv2.waitKey(0)
