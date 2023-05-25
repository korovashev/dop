import requests
import json
import os
import socks
import socket

#session = requests.Session()
#session.proxies = {'http': 'socks5://localhost:9050', 'http': 'socks5://localhost:9050'}

def download_avatar(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    if response.status_code == 200:
        json_data = json.loads(response.text)
        avatar_url = json_data['graphql']['user']['profile_pic_url_hd']
        filename = f"{username}.jpg"

        response = requests.get(avatar_url)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Аватарка {filename} загружена.")
        else:
            print("Не удалось загрузить аватарку.")
    else:
        print("Не удалось получить доступ к Instagram API.")

socks.set_default_proxy(socks.SOCKS5, '184.170.248.5', 4145)
socket.socket = socks.socksocket

username = input("Введите имя пользователя Instagram: ")
download_avatar(username)