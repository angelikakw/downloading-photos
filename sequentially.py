import urllib.request


def download_photos(photo_urls):
    for i, url in enumerate(photo_urls):
        urllib.request.urlretrieve(url, 'photos/photo_{}.png'.format(i))
