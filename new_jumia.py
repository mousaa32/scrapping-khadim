import urllib
import urllib.request
from bs4 import BeautifulSoup

grand=[]
def table(url): 
    thepage=urllib.request.urlopen(url)
    soup=BeautifulSoup(thepage,"html.parser")
    return soup 
soup=table("https://www.jumia.sn/electronique/?page=1") 
# for link in range(1,2): 
#     soup=table("https://www.jumia.sn/electronique/?page="+str(link)+"")
#     prix=[]
#     nom_produit=[]
#     lieux=[]
#     images=[]
#     source=[]     
    
#     nomexpt=soup.findAll('div',{'class':'-paxs row _no-g _4cl-3cm-shs'})
#     for i in nomexpt:
#         print(i)
        # nom_produit.append(i.find('h2').text.strip())
        # print(nom_produit)
    # for i in nomexpt:
    #     print(i)
    #     lieux.append(i.find('h5',{'class':'ad-item-subtitle d-block'}).text.strip().replace('\t','').replace('\n','').replace('Occasion',''))
    # for i in nomexpt:
    #     prix.append(i.find('p',{'class':'ad-item-price'}).text.strip())
    # imgexp=soup.findAll('div',{'class':'listing-thumbnail'})
    # for info in imgexp:
    #     v=info.find('a').get('href')
    #     http="https://www.expat-dakar.com"
    #     somme=http+v
    #     source.append(somme)
    #     image = info.a.find('img')['src']
    #     product_image = http + image
    #     images.append(product_image) 