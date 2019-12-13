import requests
from bs4 import BeautifulSoup
import smtplib
import time

headers = {
    "User-Agent:" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}

URL = "https://www.amazon.com/Pokemon-Platinum-Nintendo-DS/dp/B001O1OBFY/ref=sr_1_1?keywords=pokemon+platinum&qid=1576259789&sr=8-1"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

soup.encode('utf-8')

def check_price():
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text().replace(',', '').replace('$', '').replace(' ', '').strip()

    converted_price = float(price[0:5])
    print(converted_price)
    if(converted_price < 13000):
        send_mail()

    print(title.strip())

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("email@gmail.com", "password")

    subject = "price fell down!"
    body = "check the amazon link https://www.amazon.com/Pokemon-Platinum-Nintendo-DS/dp/B001O1OBFY/ref=sr_1_1?keywords=pokemon+platinum&qid=1576259789&sr=8-1"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "sender@gmail.com",
        "receiving@gmail.com",
        msg
    )
    print("EMAIL HAS BEEN SENT!")

    server.quit()

while(True):
  check_price()
  time.sleep(60 * 60)


