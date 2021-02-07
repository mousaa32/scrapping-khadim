import urllib
import urllib.request
from bs4 import BeautifulSoup
import os,json,csv,pandas,requests
from datetime import datetime

def table(url): 
    thepage=urllib.request.urlopen(url)
    soup=BeautifulSoup(thepage,"html.parser")
    return soup
grand=list()

###############*******************************************coinafrique/immobilier**********************************************#######################


soup=table("https://sn.coinafrique.com/categorie/immobilier")
lien_coin=[]
 
for lien in soup.findAll('li',{'class':'category gtm-sous-category center'}):
    lien_coin.append(lien.find('a').get('href'))
# print(lien_coin)
for link in lien_coin:
    # print(link)
    try:      
        for i in range(1,30):
            nom_produit = list()
            prix_produit = list()
            image_produit = list()
            source_produit = list()
            alt_produit = list()
            soup=table("https://sn.coinafrique.com"+link+"?page="+str(i)+"")
            categorie=soup.find('title').text.replace('CoinAfrique - Petites annonces au Sénégal - ','').replace('Immobilier  - ','')
            logo="https://sn.coinafrique.com/static/images/logo.svg"
            for nov in soup.findAll('div',{'class':'col s6 m4 l3'}):
                # print(nov)
                nom_produit.append(nov.find('p',{'class':'ad__card-description'}).text.replace('\n','').replace(',',';').replace('\xa0piece',' piece'))
                prix_produit.append(nov.find('p',{'class':'ad__card-price'}).text)
                source_produit.append(nov.find('img')['src'])
                alt_produit.append(nov.find('a')['title'].replace(',',';').replace('\xa0piece',' piece'))
                image_produit.append("https://sn.coinafrique.com"+nov.find('a')['href'])
            # print(nom_produit)
            # print(prix_produit)
            # print(source_produit)
            # print(alt_produit)
            # print(image_produit)
            for h,j,k,l,m in zip(nom_produit,prix_produit,image_produit,source_produit,alt_produit):
                dic = {'name':h,'price':j,'link':k,'image':l,'provider':'CoinAfrique','logo':logo,'category':categorie,'source':'sn'}

                print(dic)
    except :
        pass

