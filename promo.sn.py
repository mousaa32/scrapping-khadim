import urllib
import urllib.request
from bs4 import BeautifulSoup

grand=[]
def table(url): 
    thepage=urllib.request.urlopen(url)
    soup=BeautifulSoup(thepage,"html.parser")
    return soup
menu=[]                 
soup=table("https://www.promo.sn/") 
menus=soup.findAll('div',{'class':'wrapper_vertical_menu vertical_megamenu'})
for i in menus:
    a=i.findAll('a')
    for href in a:
        menu.append(href.get('href'))
sous_menu = list(filter(None, menu))

for link in sous_menu: 
    nom_produits=[]
    prix=[]
    sources=[]
    images=[]
    soup1=table(link)
    logo="https://www.promo.sn/wp-content/uploads/2020/02/10429565774781552381-150x150.jpg"
    categorie=soup1.find('title').text.replace(' - Promo.sn','')
    limit=soup1.find('div',{'class':'content col-lg-9 col-md-9 col-sm-12'})
    produit=limit.findAll('div',{'class':'products-entry item-wrap clearfix'})
    for info in produit:
        nom_produits.append(info.find('h4').text)
        a=info.find('span',{'class':'item-price'}).text.replace("\xa0"," ")
        if len(a) > 13:
            b=a[len(a)//2:]
            prix.append(b)
        else:
            prix.append(a)
        sources.append(info.find('a').get('href'))
        images.append(info.find('a').find('img').get('data-lazy-src'))

    for i,j,k,l in zip(nom_produits,prix,sources,images): 
        dic = {'nom_produit':i,'prix':j,'source':k,'image':l,'categorie':categorie,'logo':logo}
        grand.append(dic)
    print(grand)

   

 
