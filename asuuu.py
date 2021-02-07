from flask import Flask,render_template,request,redirect,url_for

from bs4 import BeautifulSoup
import requests
from datetime import date
import pandas

#***********************************************************************************************************************
#                                                     EXPAT-DAKAR
#***********************************************************************************************************************

# recuperation des urls de chaque publication d'appartement pour 
class Url_expat:
    def __init__(self,url):
        self.soup=BeautifulSoup(requests.get(url).text,'html.parser')

    def url(self):
        div_url=self.soup.findAll('div',class_='listing-thumbnail videoless')
        urls=[]
        for i in div_url:
            try:
                url="https://www.expat-dakar.com"+i.find("a")['href']
                urls.append(url)
            except Exception:   
                continue
        return urls

    def lieu(self):   
        div_lieu=self.soup.findAll('div',class_='picto-block')
        lieux=[]
        for i in div_lieu:
            try:
                lieu=i.find('span',class_='picto picto-place ed-icon-before icon-location').text
                lieux.append(lieu)
            except Exception:
                continue
        return lieux


            

class Appartement_expat:
    def __init__(self,url):
    #r = requests.get('https://www.expat-dakar.com/appartements-a-louer/almadies---appartement-92-1321989')  # permet d'avoir le code source de la page avec r.text
        self.soup=BeautifulSoup(requests.get(url).text,'html.parser')

    def img(self):
        divimg=self.soup.find('div',class_='col-xs-12 col-sm-6 col-md-6 media-wrapper')
        img="https://www.expat-dakar.com"+divimg.find("img",class_='cloudzoom')['src']
        return img

    def info(self):
        title=self.soup.find('div',class_="title-details-wrapper")
        titre=title.find('h1',class_='title').text
        prix=title.find('h2',class_='price').text
        piece=title.find('span',class_="attribute-item").text
        return titre,prix,piece
        
    def post(self):
        div_post=self.soup.find('div',class_="listing-owner-box").text
        p=div_post.strip().split('\n')    #strip enleve les ligne vides et les tabulations et split convertit tout en liste
        poste=p[0].split()
        poste.remove('par')
        posteur=" ".join(poste)
        moment=p[1].strip()
        return posteur,moment

    def details(self):
        description1=self.soup.find('div',class_="details-content text-justify").text
        description=description1.strip()
        return description

    def contact(self):
        div_contact=self.soup.find("div",class_='details-contact-info ')
        ul_contact=div_contact.find("ul",class_='dropdown-menu')
        contact=ul_contact.find("a").text.strip()
        return contact
lieux=[]
urls_expat=[]
for i in range(1,5):
    url=Url_expat("https://www.expat-dakar.com/appartements-a-louer?page="+str(i))
    urls_expat.append(url.url())
    lieux.append(url.lieu())

tab = []
for i, ii in zip(urls_expat,lieux):
    for j,jj in zip(i,ii):
        try:
            app=Appartement_expat(j)
            images=app.img()
            titres,les_prix,pieces=app.info()
            proprietaires,date_posts=app.post()
            descriptions=app.details()
            contacts=app.contact()
            tab.append({'images':images,'url':j,'titres':titres,'proprietaires':proprietaires,'lieu':jj,'pieces':pieces,'date-poste':date_posts,'descriptions':descriptions,'prix':les_prix,'contact':contacts})
        except Exception:
            continue
les_lieux=[]
for i in lieux:
    for j in i:
        les_lieux.append(j)
lieux_dict = {}.fromkeys(set(les_lieux),0)
for valeur in les_lieux:

    lieux_dict[valeur] += 1
list_lieu = list(lieux_dict.keys())

occs=[]
for occ in lieux_dict.values():
    occs.append(occ)
print(lieux)
print(lieux_dict)

# app= Flask(__name__)

# @app.route('/')
# def home():
    
#     return render_template('pages/acc.html',tab=tab)



# @app.route('/listes_app')
# def listes_app():
    
#     return render_template('pages/listes_app.html',tab=tab)

# @app.route('/statistiques')
# def statistiques():
    
#     return render_template('pages/statistiques.html',list_lieu=list_lieu,occs=occs)

# app.run(debug=True)
        



        


    



# today je vais scrapper jumia 
