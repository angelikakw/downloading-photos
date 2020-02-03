import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed


def fetch_image(photo_url):
    response = urllib.request.urlopen(photo_url)
    return response.read()


def save_image(photo, file_name):
    with open(file_name, 'wb') as _file:
        _file.write(photo)


def download_photos(photo_urls):
    pool = ThreadPoolExecutor()
    photos_futures = {}
    for i, url in enumerate(photo_urls):
        file_name = 'photos/photo_{}.png'.format(i)
        fetch_future = pool.submit(fetch_image, url)
        photos_futures[fetch_future] = file_name

    for future in as_completed(photos_futures):
        file_name = photos_futures[future]
        pool.submit(save_image, future.result(), file_name)

    pool.shutdown(wait=True)
