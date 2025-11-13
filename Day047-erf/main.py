import subprocess; subprocess.call('cls',shell=True), 
from bs4 import BeautifulSoup as BS
import requests as req
import os
from mail_sender import GmailSender
url_product = "https://www.amazon.co.uk/Silver-Buffalo-FRD20133-Friends-Multicolor/dp/B07CBYR1R5/ref=sr_1_4?crid=HN964441CW8Y&dib=eyJ2IjoiMSJ9.2zcJ5sZRHoG2kKJEnP7vCOKYfH9z_ouXuvPWhnayHgaEhnj1a_JLJXFI6Xk22BID9ZHmm7q8OJqNzkMhodwo0FNgCLCmWHn-ZTQEHdeNTca4rRYNXj8RVeFYrmbFyTtQ5CQL_Y4Fy1_bvf1to6BwNlWBkg6ilQRGo5c0nJ3txOWFAcXE3apQnaJVE17EJNaSWXJc-jUj3zH979MOidJa3orsO33g_uDrBla5P1rPUapbv5WaLPGxERQ1QWO5MxsmR67SEsgL3hR-Hdi4RTWT5xob-AhZYm_ujsrBglbKF3g.mICQy-LUgprxAuDld1CHpRE6kmOafytFszDhVGB3uaE&dib_tag=se&keywords=mug&qid=1763033181&sprefix=mug%2B%2Caps%2C248&sr=8-4&th=1"
headers= {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "'Chromium';v='142', 'Google Chrome';v='142', 'Not_A Brand';v='99'",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "'Windows'",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
}
cookies = {
    'i18n-prefs': 'GB' 
}
with req.get(url_product, params={'crid':'HN964441CW8Y'}, headers=headers, cookies=cookies) as res:
    res.raise_for_status()
    web_page = BS(res.text, "html.parser")

current_price = float(web_page.select("span.aok-offscreen")[0].string[2:7])
target_price: float = 100.00 

title_product_1 =" ".join(web_page.select_one("#productTitle").string.split())
title_product_2 = web_page.select_one("#productTitle").string

message_for_mail = f"You are so lucky, the \n\t{title_product_1}\n now hit the target and is below ${target_price} now!!!!\nclick link and catch it fast\n{url_product}"
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