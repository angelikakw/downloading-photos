import urllib.request
from bs4 import BeautifulSoup


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


def main():
    url_address = 'http://www.if.pw.edu.pl/~mrow/dyd/wdprir/'
    web_content = fetch_website(url_address)
    print(take_photos_address(web_content, url_address))


if __name__ == '__main__':
    main()
