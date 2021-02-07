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
################*******************************************nova**********************************************#######################
soup=table("https://nova.sn/") 
liens_nova=[]
for lien in soup.findAll('li',{'data-depth':'1'}):
    liens_nova.append(lien.find('a').get('href'))
# print(liens_nova[14:16])
for link in liens_nova[14:16]:
    for i in range(1,6):
        nom_produit = list()
        prix_produit = list()
        image_produit = list()
        source_produit = list()
        alt_produit = list()
        soup=table(link+"?page="+str(i))
        categorie=soup.find('title').text
        logo="https://img.comparez.co/logo/sn/novs.jpg"
        for nov in soup.findAll('div',{'class':'second-block'}):
            nom_produit.append(nov.find('h5').text.replace('\n','').replace(',',';').replace('\xa0piece',' piece'))
            prix_produit.append(nov.find('span').text.replace('\xa0000\xa0',' 000'))
        for tof in soup.findAll('div',{'class':'first-block'}):
            source_produit.append(tof.find('img')['src'])
            alt_produit.append(tof.find('img')['alt'].replace(',',';').replace('\xa0piece',' piece'))
            image_produit.append(tof.find('a')['href'])
        for i,j,k,l,m in zip(nom_produit,prix_produit,image_produit,source_produit,alt_produit):
            dic = {'nom_produit':i,'prix_produit':j,'source_produit':k,'image_produit':l,'alt_produit':m,'logo':logo,'categorie':categorie}
            
            api_url = "https://data.comparez.co/api/v1/products"

            data = {
                "name": "nom produit",
                "price": "prix du produit sans CFA",
                "image": "url image",
                "provider": "site scrappé",
                "link": "lien du produit",
                "category": "nom de la categorie",
                "logo": "lien du logo",
                "source": "pays",
            }

            req = requests.post(api_url, json=data)

            print(req.json())
            
            
grand.append(dic)