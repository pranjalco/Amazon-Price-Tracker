import requests
from bs4 import BeautifulSoup
import smtplib
from art import logo

"""
# Project 32: Amazon Price Tracker

## Author
- **Name**: Pranjal Sarnaik
- **Date**: 25 Jan 2025

## Description
This project tracks the price of a specific product on Amazon. Users set a target price for the product, and the program scrapes the current price and title of the product using the BeautifulSoup library. If the current price falls below the target price, an automatic email notification is sent to the user with the subject "Amazon Price Alert." The email includes the product name, the updated lower price, and a link to the product.

> **Note**: For security purposes, sensitive information such as email addresses, app passwords, and header info have been removed. Additionally, Amazon may periodically update its URL structure, which might require adjustments to the scraping logic. Please update sensitive details and test the program with the latest Amazon URL structure before running.

## How to Use
1. Set up the following libraries in your Python environment:
   - `requests`
   - `BeautifulSoup` (from `bs4`)
   - `smtplib`
   - `art`
2. Provide the Amazon product URL and set your target price in the `app.py` file.
3. Add your email credentials and SMTP configuration for notifications.
4. Run the program to track price changes.

## Level
- **Level**: Intermediate
- **Skills**: Web scraping, automation, SMTP email setup
- **Domain**: E-commerce automation

## Features
- Scrapes product title and current price from Amazon.
- Sends email alerts if the product price is below the target.
- Allows integration with various SMTP providers:
  - Gmail: `smtp.gmail.com`
  - Hotmail: `smtp.live.com`
  - Outlook: `outlook.office365.com`
  - Yahoo: `smtp.mail.yahoo.com`

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/pranjalco/Amazon-Price-Tracker.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Amazon-Price-Tracker
   ```

## Running the Program
1. Ensure Python 3.9 or later is installed on your system.
2. To run the program:
   - **Using PyCharm**: Open the project in PyCharm and run `app.py`.
   - **Using Terminal/Command Prompt**: Navigate to the project folder and execute:
     ```bash
     python app.py
     ```
   - **By Double-Clicking**: You can double-click `app.py` to run it directly, provided Python is set up to execute `.py` files on your system.
3. If the console window closes immediately, run the program from the terminal/command prompt or IDE to see the output.

## File Structure
```
project-root
|
|-- app.py                 # Main program file
|-- requirements.txt       # List of Python dependencies
|-- experiments/           # Temporary files and practice scripts
|-- screenshots/           # Screenshots of the program in action
```

---
**Created by Pranjal Sarnaik**  
*© 2024. All rights reserved.*
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












