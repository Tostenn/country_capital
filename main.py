'''


    Toute amelioration du spcrit sera la BIENVENU
    N'hesite a envoyer vos remaque a cette adresse kouyatosten@gmail.com
    
    description : ce script peut se diver en 2 partir

        - Recuperer des Donners
        - Formatage des Donners
    

'''


from json import dump
from bs4 import BeautifulSoup as be
from requests import get
#  from repertoire import effter ce module n'est pas encore disponible 
from optparse import OptionParser
from threading import Thread
from sys import argv
from os.path import isfile



# aller chercher les donner
def req():
    url = 'https://hors-frontieres.fr/liste-des-capitales-de-tous-les-pays-du-monde/'
    return get(url).text

# recuperation de
def recu():
    r = req()
    b = be(r,features='html.parser')
    return b.findAll('td')


'''

    formatage de donner recuperer sous la forme { pays : capital }

'''


# ajout des pays dans le dictionnaire
def addP():
    data = {}
    st = recu()
    for i in st:
        j = ""
        if int(i['width']) >= 200:
            data[i.text] = ''
    return data

# ajout des capital dans le dictionnaire
def addC(af = False):
    n= 0
    data = addP();st = recu()
    for i,j in data.items():
        c = 0
        for z in st[n:]:
            c +=1
            if 150< int(z['width']) <= 200:
                data[i]  = z.text.strip()
                n += c
                break
    if af== True: 
        for i,j in data.items(): print(f'pays {i} | {j} capital')
    return data

# enredistrement des donner dans un fichier json formatage = { pays : capital }
def enr(ch = False,format= ''):
    data = addC()
    if ch in [False,'false']: ch = 'data.'+format

    if format == 'json':
        with open(ch,"w") as file:
            dump(data,file)
            print(f'enregistrer dans le fichier \\{ch}')
    else:
        with open(ch,"w") as file:
            for i,j in data.items(): file.write(f'{i}:{j}\n')
            print(f'enregistrer dans le fichier \\{ch}')

name = 'main.py'
info = f'''{"mode d'emploi":-^55}
    Usage : 
            {name} -e (json/txt) format d'enregistrement des donner
            {name} -a affichage des donner (true/false)
            {name} -n nom du fichier d'enregistrement par defaut c'est data.json
            {name} -f forcer l'enregistrement dans un fichier exitant

    Exemple : {name} -e json -n index -f _
              {name} -a false -n data -f _
              {name} -e txt -a true -n enregistrement

'''
def print_info():
    print(p.usage)
    exit()
# parametrage des option
p = OptionParser(info)
p.add_option('-e',dest='erg',type='string',help='enregistrement json/txt')
p.add_option('-a',dest='af',type='string',help='affichage {pays : capital} ')
p.add_option('-n',dest='name',type='string',help='nom du fichier')
p.add_option('-f',dest='df',type='string',help='nom du fichier')

# recuperation des option 
res,null = p.parse_args()
erg, aff,name = res.erg,res.af,res.name
force = True if '-f' in argv else False
# dispositif de preparation de l'option -a
t = Thread(target=addC,args=[True])
def _a():
    t.start()
    t.join()

# cet fonction permet de verifier si le nom du fichier indiquer existe
def veri_fch(name,erg):
    if name != False:
        if isfile(name+'.'+erg):

            if force == True:enr(ch=name+'.'+erg,format=erg)
            else:
                verifi = input(f'le fichier {name}.{erg} existe déja voulez vous le réecrire o/n ? ')
                enr(ch=name+'.'+erg,format=erg) if verifi.lower() == 'o' else print_info()
        else:enr(ch=name+'.'+erg,format=erg)
    else :
        if isfile('data.'+erg):

            if force == True:enr(ch=name+'.'+erg,format=erg)
            else:
                verifi = input(f'le data.{erg} existe déja voulez vous le réecrire o/n ? ')
                enr(format=erg) if verifi.lower() == 'o' else print_info()
        else:enr(format=erg)
        
# ---------------------------traitement------------------------------------
try :
    if (name or erg or aff):

        erg = erg if type(erg) != type(None) else 'false' 
        aff = aff if type(aff) != type(None) else 'false' 
        name = name if type(name) != type(None) else False

        if erg.lower() in ['json','txt']:

            if aff.lower() =='true':

                if name != False:
                    veri_fch(name,erg)
                    _a()
                else:
                    veri_fch('data',erg)
                    _a()
            
            else: veri_fch(name,erg)

        else:
            if aff.lower() =='true':
                if name != False:
                    veri_fch(name,erg = 'txt')
                    _a()
                else: _a()
            else:
                if name != False: veri_fch(name,erg = 'txt')

    else :print_info()

except : print('''Vous avez un probleme que faire D'abord
    - Verifier votre connection internet
    - Allons jetter un coup d'oeil a la documentation sur 'https://github.com/Tostenn/country_capital'
    - Si le probleme persiste n'hesite pas a me contacter a cette adresse kouyatosten@gmail.com
''')
    