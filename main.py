from datetime import datetime
from bs4 import BeautifulSoup
import time
import requests
import SendMail
# import call
from datetime import datetime

# return a status of availability of a product
def status (url, headers):
    requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
    respond = requests.get(url, headers=headers)

    print('HTTP', respond.status_code)
    if respond.status_code != 200:
        return 'Out of stock'
    else:
        html = respond.content
        soup = BeautifulSoup(html, 'lxml')
        # import pdb; pdb.set_trace()
        match = soup.find('div', class_='product__payment-container')
        status = match.text
        return status

# Start in 2 hours
#time.sleep(7200)
url1 = 'https://store.sony.com.sg/collections/playstation-consoles/products/playstation-5-bundle-black'
url2 = 'https://store.sony.com.sg/collections/playstation-consoles/products/playstation-5-digital-bundle-black'
url3 = 'https://store.sony.com.sg/collections/playstation-consoles/products/playstation-5-bundle'
url4 = 'https://store.sony.com.sg/collections/playstation-consoles/products/playstation-5-digital-bundle'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
counter = 0
status_list = []  # Red, Black, Green color of switch

while True:
    counter += 1
    status_list = [status(url1, headers), status(url2, headers), status(url3, headers), status(url4, headers)]  #[Sold out, Sold out, Add to Cart] could be one of the examples
    time.sleep(1)
    print(datetime.now())
    body = "dual1 is {0}, dual2 is {1}, dual3 is {2}, dual4 is {3}".format(status_list[0], status_list[1], status_list[2], status_list[3]) # Sold Out, Add to Cart, Check Stores
    print(body)

    print('Number of visit: {0}\n'.format(counter))

    if 'Add to cart\n\n' in status_list or any('Add' in state for state in status_list):

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("%r sending your email now....\n" %dt_string)
        SendMail.sentmail()
        # call.call()

    time.sleep(10)