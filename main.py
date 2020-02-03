import time
import urllib.request
import threads
import sequentially
from bs4 import BeautifulSoup


DOWNLOAD_FUNCTIONS = {
    'sequentially': sequentially.download_photos,
    'threads': threads.download_photos
}



def fetch_website(url_address):
    response = urllib.request.urlopen(url_address)
    web_content = response.read()

    return web_content


def take_photos_address(web_content, base_url):
    photo_urls = []
    soup = BeautifulSoup(web_content)
    for img_link in soup.find_all('a'):
        if img_link['href'].endswith('.png'):
            photo_urls.append(base_url + img_link['href'])
    return photo_urls


def main(method='sequntially'):
    url_address = 'http://www.if.pw.edu.pl/~mrow/dyd/wdprir/'
    web_content = fetch_website(url_address)
    photo_urls = take_photos_address(web_content, url_address)

    download_photos = DOWNLOAD_FUNCTIONS[method]

    start_time = time.time()
    download_photos(photo_urls)
    end_time = time.time()
    time_diff = end_time - start_time

    print(time_diff)


if __name__ == '__main__':
    main('threads')
