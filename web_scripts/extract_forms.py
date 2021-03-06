import requests
from bs4 import BeautifulSoup
import urlparse


def make_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "http://192.168.57.130/mutillidae/index.php?page=dns-lookup.php"
res = make_request(target_url)

parsed_html = BeautifulSoup(res.content, "html.parser")
forms_list = parsed_html.findAll("form")

for form in forms_list:
    action = form.get("action")
    post_url = urlparse.urljoin(target_url, action)
    method = form.get("method")

    inputs_list = form.findAll("input")
    post_data = {}
    for input in inputs_list:
        input_name = input.get("name")
        input_type = input.get("type")
        input_value = input.get("value")
        if input_type is not "submit":
            input_value = "test"

        post_data[input_name] = input_value
    res = requests.post(post_url, data=post_data)
    print(res.content)
    post_data = {}
