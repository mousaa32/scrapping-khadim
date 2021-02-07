import urllib
import urllib.request
from bs4 import BeautifulSoup

grand=[]
def table(url): 
    thepage=urllib.request.urlopen(url)
    soup=BeautifulSoup(thepage,"html.parser")
    return soup
                       
soup=table("https://discount-senegal.com/") 
menu=[]
menus=soup.findAll('div',{'class':'mobile-nav-content'})
for i in menus:
    a=i.findAll('a')
    for href in a:
        menu.append(href.get('href'))
# print(menu)
sous_menu = list(filter(None, menu))
for link in sous_menu: 
    nom_produits=[]
    prix=[]
    sources=[]
    images=[]
    soup1=table(link)
    logo="https://discount-senegal.com/wp-content/uploads/2019/04/New-Logo-DISCOUNT-AFRICA-DK.png"
    categorie=soup1.find('title').text.replace(' - Discount Sénégal','')
    produit=soup1.findAll('div',{'class':'product-inner clearfix'})
    for info in produit:
        nom_produits.append(info.find('h2').text)
        prix.append(info.find('span',{'class':'woocommerce-Price-amount amount'}).text.replace("\xa0"," "))
        sources.append(info.find('a').get('href'))
        images.append(info.find('a').find('img').get('data-original'))

    for i,j,k,l in zip(nom_produits,prix,sources,images): 
        dic = {'nom_produit':i,'prix':j,'source':k,'image':l,'categorie':categorie,'logo':logo}
        grand.append(dic)
    print(grand)


