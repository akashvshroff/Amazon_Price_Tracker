import requests
import smtplib
import time
import sys
from bs4 import BeautifulSoup
from secret import *  # File with all my personal details, user-agent, email and app password


class PriceTracker:
    def __init__(self, url, target, smail):
        self.url = url
        self.target = target
        self.smail = smail
        self.headers = {
            "User-Agent": useragent  # Get yours by searching 'My user agent' on your browser
        }
        self.my_email = my_email
        self.app_password = app_password
        self.conn = smtplib.SMTP('smtp.gmail.com', 587)
        self.conn.ehlo()
        self.conn.starttls()
        # Get your app password from https://support.google.com/accounts/answer/185833?hl=en
        self.conn.login(my_email, app_password)
        self.driver()

    def driver(self):
        while True:
            self.check_price()
            print("Going to check tomorrow")
            time.sleep(24*60*60)

    def check_price(self):
        self.res = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(self.res.content, 'html.parser')
        soup.encode('utf-8')
        self.title = soup.find(id="productTitle").get_text().strip()
        price_elem = soup.find(id="priceblock_ourprice")
        self.price = price_elem.get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
        pf = float(self.price)
        if pf <= self.target:
            self.send_mail()
        else:
            return

    def send_mail(self):
        self.url_encoded = string.encoding('ascii', 'ignore')
        self.msg = 'Subject:Amazon Product Available!\n\nYour product: {} is now available for price: {}.\nBuy now at url: {}'.format(
            self.title, self.price, self.url_encoded)
        self.conn.sendmail('akushroff@gmail.com', self.smail, self.msg)
        self.conn.quit()
        sys.exit()


def main():
    print("WELCOME TO THE AMAZON PRICE TRACKER!")
    print("-"*15)
    print("Enter amazon url to track:")
    while True:
        url = input()
        if 'amazon' not in url.split('.'):
            print("Please enter valid amazon url:")
            continue
        else:
            break
    print("Enter target price:")
    while True:
        p = input()
        pt = p.replace(',', '').replace(' ', '').strip()
        try:
            target = float(pt)
            break
        except:
            print("Please enter valid amount without currency sign and commas:")
            continue
    print("Enter mail to notify:")
    smail = input()
    print("Now checking website once a day.")
    try:
        PriceTracker(url, target, smail)
    except KeyboardInterrupt:
        print("Exiting.")
        sys.exit()


if __name__ == '__main__':
    main()
# check_price('https://www.amazon.in/dp/B01JMEDYCK/ref=psdc_1375248031_t1_B07F1NMKLM?th=1', None)
