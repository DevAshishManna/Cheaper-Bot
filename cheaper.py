import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.amazon.in/Seagate-Expansion-Portable-External-Playstation/dp/B007IREFE0/ref=sr_1_1?keywords=hdd&qid=1565958704&s=gateway&smid=A14CZOWI00VEHLG&sr=8-1'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
#Enable  less secure apps for this to work
def check_price():
    page = requests.get(URL,headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id= "productTitle").get_text()
    price = soup2.find(id="priceblock_dealprice").get_text()
    converted_price = price.strip()[2:7]
    converted_list = list(converted_price)
    converted_list.remove(',')
    new_price = int("".join(converted_list))

    if(new_price > 3500):
        send_mail()
        
    print(new_price)
    print(title.strip())
    

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mannad199815@gmail.com','518991dannam')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/Seagate-Expansion-Portable-External-Playstation/dp/B007IREFE0/ref=sr_1_1?keywords=hdd&qid=1565958704&s=gateway&smid=A14CZOWI00VEHLG&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
            'dmanna199815@gmail.com',
            'mannad199815@gmail.com',
            msg
        )
    print("HEY  EMAIL HAS BEEN SENT!")
    server.quit()

check_price()
