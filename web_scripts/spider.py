import requests
import re
import urlparse


url = "https://zsecurity.org"
target_links = []


def get_links_from_url(target_url):
    response = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"', response.content)


def crawl(url):
    href_links = get_links_from_url(url)

    for link in href_links:
        link = urlparse.urljoin(url, link)

        if '#' in link:
            link = link.split("#")[0]

        if url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)


crawl(url)
