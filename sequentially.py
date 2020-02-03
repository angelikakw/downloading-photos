import urllib.request
import cv2
from gaussian_filter import filter_photo


def download_photos(photo_urls):
    for i, url in enumerate(photo_urls):
        file_name = 'photos/photo_{}.png'.format(i)

        response = urllib.request.urlopen(url)
        blurred_photo = filter_photo(response.read())
        cv2.imwrite(file_name, blurred_photo)
