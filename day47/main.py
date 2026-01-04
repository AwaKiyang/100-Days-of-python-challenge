
from bs4 import BeautifulSoup
import os
import smtplib
from selenium import webdriver

driver = webdriver.Chrome()
def price_alert_monitor():
    """
    Monitor product price from an HTML file and send email alert if price drops below threshold.
    This function reads product pricing information from a local HTML file,
    extracts the price, and sends an email notification if the price falls
    below $100. Uses Gmail SMTP server for email delivery.
    Process:
    1. Read HTML content from 'website.html' file
    2. Parse HTML using BeautifulSoup to extract price element by ID
    3. Convert extracted price string to float for numerical comparison
    4. Retrieve Gmail credentials (email and password from environment variables)
    5. If price is below $100 threshold:
       - Establish secure SMTP connection to Gmail's SMTP server on port 587
       - Enable TLS encryption for secure communication
       - Authenticate with Gmail account credentials
       - Compose email with subject line and message body containing current price
       - Send alert email to recipient address
       - Print confirmation message
    6. If price is at or above threshold:
       - Print message indicating price is still high
    Dependencies:
        - BeautifulSoup4: For HTML parsing
        - smtplib: For SMTP email functionality
        - os: For retrieving environment variables
    Files Required:
        - website.html: Local HTML file containing price element with id="price"
    Environment Variables:
        - email_password: Gmail app-specific password for authentication
    Raises:
        FileNotFoundError: If 'website.html' file does not exist
        smtplib.SMTPAuthenticationError: If Gmail credentials are invalid
        ValueError: If price element cannot be converted to float
    Note:
        - Requires Gmail account with app-specific password enabled
        - SMTP connection uses port 587 with STARTTLS encryption
        - Price threshold is hardcoded at $100
    """
    with open('website.html') as file:
        html_ifo = file.read()

    soup = BeautifulSoup(html_ifo, "html.parser")
    price = float(soup.find(id="price").text)

    my_email = "awakiyang9@gmail.com"
    password = os.getenv("email_password")

    if price < 100:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(user=my_email, password=password)

            subject = 'Alert'
            body = f"price of cooker has dropped its  now {price}"

            message = f"Subject: {subject}\n\n{body}"

            smtp.sendmail(
                from_addr=my_email,
                to_addrs="awakiyang4@gmail.com",
                msg=message
            )
        print('price is low')
    else:
        print('sorry price is still high')

