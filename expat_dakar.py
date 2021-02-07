import urllib
import urllib.request
from bs4 import BeautifulSoup

grand=[]
def table(url): 
    thepage=urllib.request.urlopen(url)
    soup=BeautifulSoup(thepage,"html.parser")
    return soup   
for link in range(1,5): 
    try:
        logo="https://www.expat-dakar.com/assets/img/logos/logo-immobilier.svg"
        soup=table("https://www.expat-dakar.com/maisons-a-vendre?page="+str(link)+"")
        prix=[]
        nom_produit=[]
        lieux=[]
        images=[]
        source=[]       
        nomexpt=soup.findAll('div',{'class':'listing-details'})
        for i in nomexpt:
            nom_produit.append(i.find('h2').text.strip().replace("Ã\xa0","a"))
            # print(nom_produit)
        for i in nomexpt:
            # print(i)
            lieux.append(i.find('h5',{'class':'ad-item-subtitle d-block'}).text.strip().replace('\t','').replace('\n','').replace('Occasion',''))
        for i in nomexpt:
            prix.append(i.find('p',{'class':'ad-item-price'}).text.strip())
        imgexp=soup.findAll('div',{'class':'listing-thumbnail'})
        for info in imgexp:
            v=info.find('a').get('href')
            http="https://www.expat-dakar.com"
            somme=http+v
            source.append(somme)
            image = info.a.find('img')['src']
            if image == None:
                images.append(logo)
            product_image = http + image
            images.append(product_image) 
    except Exception:
        pass

    for i,j,k,l,m in zip(nom_produit,prix,lieux,source,images): 
        dic = {'nom_produit':i,'prix':j,'lieu':k,'source':l,'image':m,'logo':logo}
        grand.append(dic)
        print(grand)
     