import requests
from bs4 import BeautifulSoup
import time
from email.mime.text import MIMEText
import smtplib

while True:
    r = requests.get("https://www.kuveytturk.com.tr/finans-portali/")
    c = r.content
    soup =  BeautifulSoup(c,"html.parser")
    all = soup.find_all("div",{"class":"box-borderless"})
    usd_alis = float(soup.find("p").text.replace(" ","").replace("\r","").replace("\n","").replace("Alış","").replace(",","."))
    k=[]

    

    for item in all:

        d={}
        d["Doviz"] = item.find("h2").text.replace(" ","").replace("â","a")
        d["Alis"] = item.find_all("p")[0].text.replace(" ","").replace("\r","").replace("\n","").replace("Alış","").replace("Index","").replace("Vade","").replace("SonDeğer","")
        d["Satis"] = item.find_all("p")[1].text.replace(" ","").replace("\r","").replace("\n","").replace("Satış","").replace("Fark","").replace("TL(%)","")
        d["Degisim(%)"] = item.find_all("p")[2].text.replace(" ","").replace("\r","").replace("\n","").replace("Değişim(%)","").replace("\n","").replace("USD(%)","")
        k.append(d)
    
    if float(usd_alis) <= 6.0000:
        from_email = "dolar.gramaltin@gmail.com"
        from_password = "123_qwerty"
        to_email = "ahmetsahiniu@gmail.com", "burak95kaya@gmail.com"
        subject = "Doviz"
        message = "Dolar kuru guncel: %s" % k[0]

        msg = MIMEText(message, 'html')
        msg['Subject'] = subject   
        msg['to'] = to_email
        msg['from'] = from_email

        gmail=smtplib.SMTP('smtp.gmail.com',587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(from_email, from_password)
        gmail.send_message(msg)

 
    time.sleep(300)






        
