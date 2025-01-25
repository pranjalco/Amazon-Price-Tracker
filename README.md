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

