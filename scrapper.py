from bs4.builder import HTML
import requests
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-Camera/dp/B07B43WPVK/?_encoding=UTF8&ref_=nav_em_hd_re_signin&'
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}


def check_pice():
    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content,'lxml')

    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()
    print(price)

    price = price[2:-3]
    converted_price = 0
    for i in price:
        if i.isdigit():
            converted_price = converted_price*10+int(i)

    print(converted_price)

    if (converted_price<100000):
        send_mail()

    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()