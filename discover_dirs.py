# !/usr/bin/env python
import requests


def make_request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


def discover_dirs(url):
    with open("./dir_list.txt", "r") as words_list:
        for line in words_list:
            test_url = url + "/" + line.strip()
            response = make_request(test_url)
            if response:
                print("[+] Discovered URL ===> ", test_url)


discover_dirs("192.168.57.130/mutillidae")
