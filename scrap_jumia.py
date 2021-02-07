from flask import Flask,render_template,request,redirect,url_for

from bs4 import BeautifulSoup
from datetime import date
import requests                                                         
#***********************************************************************************************************************
#                                                     EXPAT-DAKAR
#***********************************************************************************************************************
############################################## Jumia/telephones-smartphones#######################################

class Jumia:
    def __init__(self,url):
        self.soup=BeautifulSoup(requests.get(url).text,'html.parser')

    def url(self):
        div_url=self.soup.findAll('div',class_='sku -gallery')
        urls=[]
        for i in div_url:
            try:
                url=i.find("a")['href']
                urls.append(url)
            except Exception:   
                continue
        return urls


class Portable:
    def __init__(self,url):
        self.soup=BeautifulSoup(requests.get(url).text,'html.parser')

    def img(self):
        divimg=self.soup.find('div',class_='sldr _img _prod -pbs')
        img=divimg.find("img",class_='-fw -fh')['data-src']

        return img  



    
    def info(self):
        #info = self.soup.find('div',class_="col10")
        titre = self.soup.find('h1',class_='-fs20 -pts -pbxs').text
        marque = self.soup.find('a',class_='_more').text
        prix = self.soup.find('span',class_='-b -ltr -tal -fs24').text.replace(' ','').replace('FCFA','')

        return titre,marque,prix
        

urls = []
for i in range(1,5):
    jumia = Jumia("https://www.jumia.sn/electronique/?page="+str(i))
    urls.append(jumia.url())

#print(urls)

    
marques = []
tab = []
for i in urls:
    for j in i:
        portable = Portable(j)
        images = portable.img()
        t, m, p = portable.info()
        marques.append(m)
        logo = "https://static.jumia.sn/cms/logo/jumialogo-x-4.png"
        categorie ="Parfums"
        # tab.append({"images":images, "titres":t, "urls":j})
        dic = {'name':t,'price':p,'link':j,'image':images,'provider':'jumia','logo':logo,'category':categorie,'source':'sn'}
        api_url = "https://data.comparez.co/api/v1/products"

        req = requests.post(api_url, json=dic)

        print(req.json())
        # print(dic)