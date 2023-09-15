import telebot
import requests
import random, string
from decouple import config


class functions():
    def __init__(self) -> None:
        pass
    """"this is not importaint function it just genrate random function every time"""
    # def photoname():
    #     strings = string.ascii_letters
    #     word = ''.join(random.choice(strings)for i in range(4))
    #     photoname = word
    #     return photoname
    def photosave():
       
        url = "https://meme-api.com/gimme"
        respne = requests.get(url)
        data = respne.json()
        photo = data["url"]
        save = requests.get(photo).content
        flies = open("photo.png", "wb")
        flies.write(save)

        