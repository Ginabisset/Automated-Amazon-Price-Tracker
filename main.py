import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = input('Please insert the Amazon Product URL')

# Get headers from here https://myhttpheader.com/. Specific to the browser you are using.
headers = {
    "User-Agent": '',
    "Accept-Language": '',
}

response = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

item_price = soup.find(name='span', class_='a-offscreen').getText()[1:]
item_name = soup.find(name='span', id='productTitle').getText()
max_price = input('Please state the max price of the Amazon Product')

# If the Amazon Price drops below the max price, 
if float(item_price) < float(max_price):
    email = ''
    password = ''
    smtp = 'smtp.gmail.com'
    recipient = ''
    subject = 'Subject: Amazon Price Alert!'
    message = f'{item_name[8:-8]}is now ${item_price}\n{URL}'

    with smtplib.SMTP(smtp, port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=recipient,
            msg=f'{subject}\n\n{message}'.encode('utf-8'),
        )
