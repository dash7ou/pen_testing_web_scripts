import requests
import re
import urlparse


url = "https://zsecurity.org"


def get_links_from_url(target_url):

    response = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"', response.content)


href_links = get_links_from_url(url)

for link in href_links:
    link = urlparse.urljoin(url, link)
    if url in link:
        print(link)
