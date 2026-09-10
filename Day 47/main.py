import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

# Headers to avoid false flagging as a bot
headers = { 'Accept-Language': "en-US,en;q=0.5",
            'User-Agent': "CCBot/2.0 (https://commoncrawl.org/faq/)"}

URL = "https://www.amazon.com/Instant-Pot-Duo-Mini-Programmable/dp/B06Y1YD5W7/130-5821141-3303860?pd_rd_w=kV2O7&content-id=amzn1.sym.74460d31-be51-4fd6-8e92-500ccd4514c4&pf_rd_p=74460d31-be51-4fd6-8e92-500ccd4514c4&pf_rd_r=JCZZJX06EQ11RCDEB69R&pd_rd_wg=1RffQ&pd_rd_r=b8306d42-9850-4c27-81a8-08525a750960&pd_rd_i=B06Y1YD5W7&th=1"

# Scraping the site
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

# Grabbing price and stripping it down to numbers only
soup_price = soup.find("span", class_="a-price-whole")
price = soup_price.text.replace("$", "").replace(" ", "")
price = float(price)

# If price is below our target, send an e-mail to ourselves
if price < 100:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
            msg=f"Subject:Price Alert!\n\nInstant Pot has dropped below $100 on Amazon.\nLink:{URL}")