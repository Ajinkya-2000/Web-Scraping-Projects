import requests
from bs4 import BeautifulSoup as bs
import csv


def Amazon_Phone_Data_Scraping():

    # User agent of my system - Site: whatismyborwser.com
    # Inside the site -> Detect my settings -> What is my user agent -> Copy Agent from there
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'

    # Header for request
    Headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48' , 
            'Accept-Language' : 'en-US, en;q=0.5'})

    # amazon website 
    url = 'https://www.amazon.com/s?k=mobile+phone+under+30000+rupees&crid=2XJKFPV6UMY13&sprefix=phones+under+30000+ru%2Caps%2C273&ref=nb_sb_ss_ts-doa-p_1_21'

    # Requesting the amazon page
    amazon = requests.get(url , headers=Headers)

    # Creating soup object
    amazon_page = bs(amazon.content , 'html.parser')
    #print(amazon_page.prettify())

    a_tag = amazon_page.find_all('a' , attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
    #print(a_tag[0].get('href'))

    # We have extracted all the links for the products
    links = [i.get('href') for i in a_tag ]


    main_url = 'https://amazon.com/'

    # Lists for storing the Description and Prices
    descriptions = []
    prices = []

    c = 0

    # Loop to request each link to open and fetch required data
    for link in links:
        url1 = main_url + link
        page = requests.get(url1 , headers=Headers)

        soup = bs(page.content , 'html.parser')
        
        # Getting the Name Description and Price of the phone
        description = soup.find('span' , attrs={'class':'a-size-large product-title-word-break'})
        price = soup.find('span' , attrs={'class':'a-size-medium a-color-price'})
        
        # Since I was unable to use '.text' on None Type We only get the data that does not have any None type of value
        if (description is None) or (price is None):
            print("None values")
        else:
            descriptions.append(description.text)
            prices.append(price.text)

        c += 1
        if c > 6:
            break

    raw_info = []

    # This Raw_info stores Name_Description Price_in_dollars Price_in_rupees
    for a,b in zip(descriptions , prices):
        c = float(b.replace('$',''))
        raw_info.append([a,b,c*81])

    # This Code was only for creating of headers in the csv file
    ''''
    fields = ['Name and Description' , 'Price in Dollars' , 'Price in Rupees']
    # Opening a csv file 
    with open ('Amazon data Scraping/Phones_Scraping.csv' , mode='w') as f:
        a = csv.writer(f)
        a.writerow(fields)
    '''

    with open ('Amazon data Scraping/Phones_Scraping.csv' , mode='a') as f1:
        b = csv.writer(f1)
        for data in raw_info:
            b.writerow(data)


# Calling the function
Amazon_Phone_Data_Scraping()