# !/usr/bin/env python
import requests


def make_request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


def discover_subdomains(url):
    with open("./subdomainslist.txt", "r") as words_list:
        for line in words_list:
            test_url = line.strip() + "." + url
            response = make_request(test_url)
            if response:
                print("[+] Discovered Subdomain ===> ", test_url)


discover_subdomains("google.com")
