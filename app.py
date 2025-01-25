import requests
from bs4 import BeautifulSoup
import smtplib
from art import logo

"""
p32 amazon price tracker
25-01-2025

Gmail: smtp.gmail.com
Hotmail: smtp.live.com
Outlook: outlook.office365.com
Yahoo: smtp.mail.yahoo.com
"""

print(logo)
TARGET_PRICE = 200
MY_EMAIL = "Your Email"
MY_PASSWORD = "Your App Password"

amazon_url = "Amazon_url"
header = {
        "Accept": "Your_info",
        "Accept-Encoding": "Your_info",
        "Accept-Language": "Your_info",
        "Priority": "Your_info",
        "Sec-Ch-Ua": "Your_info",
        "Sec-Ch-Ua-Mobile": "Your_info",
        "Sec-Ch-Ua-Platform": "Your_info",
        "Sec-Fetch-Dest": "Your_info",
        "Sec-Fetch-Mode": "Your_info",
        "Sec-Fetch-Site": "Your_info",
        "Sec-Fetch-User": "Your_info",
        "Upgrade-Insecure-Requests": "Your_info",
        "User-Agent": "Your_info",
}
response = requests.get(url=amazon_url, headers=header)
amazon_data = response.text


print(f"{"=" * 15}making soup object{"=" * 15}")
soup = BeautifulSoup(amazon_data, "html.parser")

# ========================== Getting Price ================================

print(f"{"=" * 15}Getting price method 2{"=" * 15}")
price_text = soup.find(class_="a-offscreen").getText()
only_price = price_text.split("$")[1]
price_float = float(only_price)
print(price_float)

# ========================== Getting Product Title =================================

print(f"{"=" * 15}Getting product title{"=" * 15}")
title_text = soup.find(name="span", class_="a-size-large product-title-word-break")
title = title_text.getText().strip()
title = (" ".join(title.split()))
print(title)

# ============================ Sending Email ================================

if price_float < TARGET_PRICE:
    my_message = (f"Subject:Amazon price alert\n\n{title} "
                  f"is available at price ${price_float}\nBuy on this link: {amazon_url}").encode("utf-8")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=my_message)

    print(f"{"=" * 15}Mail sent{"=" * 15}")
else:
    print(f"{"=" * 15}Mail not sent{"=" * 15}")












