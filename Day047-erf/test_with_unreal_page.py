import subprocess; subprocess.call('cls',shell=True), 
from bs4 import BeautifulSoup as BS
import requests as req
import os
from mail_sender import GmailSender
test_url_for_amazon = "https://appbrewery.github.io/instant_pot/"
with req.get(test_url_for_amazon) as res:
    res.raise_for_status()
    web_page = BS(res.text, "html.parser")

current_price = float(web_page.select("span.aok-offscreen")[0].string[2:7])
target_price: float = 100.00 

title_product_1 =" ".join(web_page.select_one("#productTitle").string.split())
title_product_2 = web_page.select_one("#productTitle").string

message_for_mail = f"You are so lucky, the \n\t{title_product_1}\n now hit the target and is below ${target_price} now!!!!\nclick link and catch it fast\n{test_url_for_amazon}"
print(message_for_mail)

gmail = GmailSender()
if current_price <= target_price:
    gmail.send(
        "erfawn.h@gmail.com",
        os.environ.get("gmail_key"),
        "erfawn.h@gmail.com",
        "AMAZON PRICE ALERT!",
        message_for_mail.replace('\xe9', ' ')
    )