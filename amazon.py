importer  urllib
importer  urllib . demande
de  bs4  import  BeautifulSoup
importer  os
 table def ( url ):
    thepage = urllib . demande . urlopen ( url )
    soup = BeautifulSoup (la page , "html.parser" )
     soupe de retour

soupe = table ( "https://www.amazon.fr/" )
i = 1
a = "amazon"
pour  img  dans la  soupe . findAll ( 'img' ):
    temp = img . get ( 'src' )
    # print (temp)
    si  temp == Aucun :
        temp = "https://images-eu.ssl-images-amazon.com/images/I/71+IZZprWML._AC_SY200_.jpg"
        image = temp
        # print (image)
    sinon :
        image = temp
    # print (image) 
    # print (temp)   
    #
    nametemp = img . get ( 'alt' )
    si  nametemp == Aucun :
        nametemp = a 
    impression ( nametemp )
    si  len ( nametemp ) == 0 :
        nom de fichier = str ( i )
        i + = 1

    sinon :
        filename = nametemp 
           
    fichier image = ouvert ( nom de fichier + ".jpeg" , "wb" )
    fichier image . write ( urllib . request . urlopen ( image ). read ())
    fichier image . close ()