import cv2
import numpy as np


def filter_photo(raw_image):
    np_image = np.asarray(bytearray(raw_image), dtype='uint8')
    cv2_object = cv2.imdecode(np_image, cv2.IMREAD_COLOR)
    blurred_image = cv2.GaussianBlur(cv2_object, (3, 3), 0)
    return blurred_image
