import requests
from bs4 import BeautifulSoup
import socks
import socket

socks.set_default_proxy(socks.SOCKS5, '184.170.248.5', 4145)
socket.socket = socks.socksocket

username = input("Введите ник в Instagram: ")
url = f"https://www.instagram.com/{username}/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

img_tag = soup.find("img", class_="_6q-tv")

if img_tag:
    img_url = img_tag["src"]
    img_url_hd = img_url.replace("s150x150", "s1080x1080")
    response = requests.get(img_url_hd)
    with open(f"{username}.jpg", "wb") as f:
        f.write(response.content)
        print(f"Аватарка {username} сохранена в файле {username}.jpg")
else:
    print("Пользователь не найден")