import lxml
import requests
from bs4 import BeautifulSoup as bs
import smtplib as s

books_page = requests.get('http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html')

books = bs(books_page.content , 'lxml')
#print(books.prettify())

# To get a specific price
price = books.find('p' , class_ = 'price_color').text
# To only get the numeric price without $
price_num = float(price[1:])
print(price_num)


# If price is less than 50 then we have to send a mail
# smtplib is used for this
# For gmail the port no is 587
if price_num < 60:
    smt = s.SMTP('smtp.gmail.com' , 587)
    smt.ehlo()
    smt.starttls()
    smt.login('ajinkyasurvep@gmail.com' , 'tlyrmeupyyytkffb')
    smt.sendmail('ajinkyasurvep@gmail.com','ajinkyasurvep@gmail.com',
                 f"Subject : Price Notifier Books\n\nHi, price has dropped to {price_num}\nGo Buy it!")
    smt.quit()

# We can also import time module to run this code after every given interval