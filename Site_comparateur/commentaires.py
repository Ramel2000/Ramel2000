from lxml import html
import requests
from bs4 import BeautifulSoup

def npage(a):
    if a==0:
        num=""
    else:
        p=a*5
        num="-or"+str(p)
    return num
def adresse(lien,num):
    lien=lien.split("-") 
    for i in range (len(lien)):
        if (lien[i]=="Reviews"):
            lien[i]="Reviews"+str(num)
            lien="-".join(lien)
            return lien
            break
def nomdoc(lien):
    lien=lien.split("-")
    for i in range (len(lien)):
        if (lien[i]=="Reviews"):
            nom=lien[i+1]
    return nom
def commentairesdate(nombredepage, lien):
    L1=[]
    L2=[]
    L3=[]
    L4=[]
    L5=[]
    Ldate=[]
    Lcont=[]
    Lvote=[]
    Lcom=[]
    Ltitre=[]
    Lpers=[]
    for a in range (nombredepage):
        num=npage(a)
        liennouveau=adresse(lien,num)
        page = requests.get(liennouveau)
        soup = BeautifulSoup(page.text, 'html.parser')
        for sub_heading0 in soup.find_all('q'):
            L1.append(sub_heading0.text)
            
        for sub_heading in soup.find_all('span',class_='social-member-MemberHeaderStats__stat_item--34E1r'):
            L3.append(sub_heading.text)
            
        for sub_heading2 in soup.find_all('div',class_='hotels-review-list-parts-EventDate__event_date--CRXs4'):
            L2.append(sub_heading2.text)
        for sub_heading2 in soup.find_all('a',class_='hotels-review-list-parts-ReviewTitle__reviewTitleText--3QrTy'):
            L4.append(sub_heading2.text)
        for sub_heading2 in soup.find_all('div',class_='social-member-event-MemberEventOnObjectBlock__event_type--3njyv'):
            L5.append(sub_heading2.text)    
        for i in range(len(L1)):
            Lcom.append(L1[i])
        for i in range(len(L2)):
            Ldate.append(L2[i])
        for i in range(len(L1)*2):
            
            if "contribution" in L3[i]:
                Lcont.append(L3[i])
                if "contribution" in L3[i+1]:
                    L3.insert(i+1,'0 votes utiles')
            elif "vote"  in L3[i]:
                Lvote.append(L3[i])
            elif " "  in L3[i]:
                Lvote.append(L3[i])
        for i in range (len(L1)):
            Ltitre.append(L4[i])
        for i in range (len(L1)):
            Lpers.append(L5[i])
        L1=[]
        L2=[]
        L3=[]
        L4=[]
        L5=[]
            
    
    return Lcom,Ldate,Lcont,Lvote,Ltitre,Lpers
        
def mettredansdoc(lien):
    print(lien)
    ville=input("ville:")
    nombredepage=int(input("nb de pages:"))
    Lcom,Ldate,Lcont,Lvote,Ltitre,Lpers=commentairesdate(nombredepage, lien)
    nom=nomdoc(lien)
    F=open(str(ville)+str(nom)+'Com.txt','w+')
    h=10
    for i in range (h):
        try:
            ajout=Lpers[i]+"\n"+Ltitre[i]+"\n"+Lcom[i]+"\n"+Ldate[i]+"\n"+Lcont[i]+"\n"+Lvote[i]+"\n"
            print(ajout)
            F.write(ajout)
        except:
            h=h+1
    utilite=ratio(Lcont,Lvote)
    mettreenfctderatio(Lpers,Ltitre,Lcom,Ldate,Lcont,Lvote,utilite,nom,ville)
    F.close()
    mettreenfctdecontri(Lpers,Ltitre,Lcom,Ldate,Lcont,Lvote,nom,ville)
    mettreenfctdevoteu(Lpers,Ltitre,Lcom,Ldate,Lcont,Lvote,nom,ville)

def ratio(Lcont,Lvote):
    choix="0123456789"
    L3=[]
    L4=[]
    Lratio=[]
    m=" ".join(Lcont)
    n=" ".join(Lvote)
    L1=m.split(" ")
    L2=n.split(" ")
    for i in range (len(L1)):
        for j in range(len(L1[i])):
            if L1[i][j] in choix:
                L3.append(L1[i])
                break
    for i in range (len(L2)):
         for j in range(len(L2[i])):
            if L2[i][j] in choix:
                L4.append(L2[i])
                break
    for j in range (len(L3)):
        if "\xa0" in L3[j]:
            L3[j]= L3[j].replace('\xa0', '')
    for j in range (len(L4)):
        if "\xa0" in L4[j]:
            L4[j]= L4[j].replace('\xa0', '')
            
    for i in range (len(L4)):
        ratiof=L4[i]+"/"+L3[i]
        Lratio.append(ratiof)
        Lratio[i]=eval(Lratio[i])
    return Lratio
    

def mettreenfctderatio(Lpers,Ltitre,Lcom,Ldate,Lcont,Lvote,utilite,nom,ville):
    place=[]
    rang1=rang2=rang3=rang4=rang5=rang6=rang7=rang8=rang9=rang10=rang11=-1
    for i in range (len(utilite)):
        place.append(utilite[i])
    place.sort(reverse=True)
    for i in range(len(utilite)):
        if place[0]==utilite[i]:
            if rang1==-1:
                rang1=i
            else:
                rang2=i
        elif place[1]==utilite[i]:
            if rang2==-1:
                rang2=i
            else:
                rang3=i
        elif place[2]==utilite[i]:
            if rang3==-1:
                rang3=i
            else:
                rang4=i
        elif place[3]==utilite[i]:
            if rang4==-1:
                rang4=i
            else:
                rang5=i
        elif place[4]==utilite[i]:
            if rang5==-1:
                rang5=i
            else:
                rang6=i
        elif place[5]==utilite[i]:
            if rang6==-1:
                rang6=i
            else:
                rang7=i
        elif place[6]==utilite[i]:
            if rang7==-1:
                rang7=i
            else:
                rang8=i
        elif place[7]==utilite[i]:
            if rang8==-1:
                rang8=i
            else:
                rang9=i
        elif place[8]==utilite[i]:
            if rang9==-1:
                rang9=i
            else:
                rang10=i
        elif place[9]==utilite[i]:
            if rang10==-1:
                rang10=i
            else:
                rang11=i
        elif place[10]==utilite[i]:
            if rang11==-1:
                rang11=i
                
            
    rang=[]
    rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10,rang11]
    P=open(str(ville)+str(nom)+'Comeff.txt','w+')
    h=10
    for i in range (h):
        try:
            ajout=Lpers[rang[i]]+"\n"+Ltitre[rang[i]]+"\n"+Lcom[rang[i]]+"\n"+Ldate[rang[i]]+"\n"+Lcont[rang[i]]+"\n"+Lvote[rang[i]]+"\n"
            P.write(ajout)
        except:
            h=h+1
            
    P.close()
def mettreenfctdecontri(Lpers,Ltitre,Lcom,Ldate,Lcont,Lvote,nom,ville):
    choix="0123456789"
    L3=[]
    m=" ".join(Lcont)
    L1=m.split(" ")
    for i in range (len(L1)):
        for j in range(len(L1[i])):
            if L1[i][j] in choix:
                L3.append(L1[i])
                break
    for j in range (len(L3)):
        if "\xa0" in L3[j]:
            L3[j]= L3[j].replace('\xa0', '')
    for i in range (len(L3)):
        L3[i]=eval(L3[i])
    place=[]
    rang1=rang2=rang3=rang4=rang5=rang6=rang7=rang8=rang9=rang10=rang11=-1
    for i in range (len(L3)):
        place.append(L3[i])
    place.sort(reverse=True)
    for i in range(len(L3)):
        if place[0]==L3[i]:
            if rang1==-1:
                rang1=i
            else:
                rang2=i
        elif place[1]==L3[i]:
            if rang2==-1:
                rang2=i
            else:
                rang3=i
        elif place[2]==L3[i]:
            if rang3==-1:
                rang3=i
            else:
                rang4=i
        elif place[3]==L3[i]:
            if rang4==-1:
                rang4=i
            else:
                rang5=i
        elif place[4]==L3[i]:
            if rang5==-1:
                rang5=i
            else:
                rang6=i
        elif place[5]==L3[i]:
            if rang6==-1:
                rang6=i
            else:
                rang7=i
        elif place[6]==L3[i]:
            if rang7==-1:
                rang7=i
            else:
                rang8=i
        elif place[7]==L3[i]:
            if rang8==-1:
                rang8=i
            else:
                rang9=i
        elif place[8]==L3[i]:
            if rang9==-1:
                rang9=i
            else:
                rang10=i
        elif place[9]==L3[i]:
            if rang10==-1:
                rang10=i
            else:
                rang11=i
        elif place[10]==L3[i]:
            if rang11==-1:
                rang11=i
            
    rang=[]
    rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10,rang11]
    h=10
    Q=open(str(ville)+str(nom)+'Comcont.txt','w+')
    for i in range (h):
        try:
            ajout=Lpers[rang[i]]+"\n"+Ltitre[rang[i]]+"\n"+Lcom[rang[i]]+"\n"+Ldate[rang[i]]+"\n"+Lcont[rang[i]]+"\n"+Lvote[rang[i]]+"\n"
            Q.write(ajout)
        except:
            h=h+1
    Q.close()

def mettreenfctdevoteu(Lpers,Ltitre,Lcom,Ldate,Lcont,Lvote,nom,ville):
    choix="0123456789"
    L3=[]
    m=" ".join(Lvote)
    L1=m.split(" ")
    for i in range (len(L1)):
        for j in range(len(L1[i])):
            if L1[i][j] in choix:
                L3.append(L1[i])
                break
    for j in range (len(L3)):
        if "\xa0" in L3[j]:
            L3[j]= L3[j].replace('\xa0', '')
    for i in range (len(L3)):
        L3[i]=eval(L3[i])
    place=[]
    rang1=rang2=rang3=rang4=rang5=rang6=rang7=rang8=rang9=rang10=rang11=-1
    for i in range (len(L3)):
        place.append(L3[i])
    place.sort(reverse=True)
    for i in range(len(L3)):
        if place[0]==L3[i]:
            if rang1==-1:
                rang1=i
            else:
                rang2=i
        elif place[1]==L3[i]:
            if rang2==-1:
                rang2=i
            else:
                rang3=i
        elif place[2]==L3[i]:
            if rang3==-1:
                rang3=i
            else:
                rang4=i
        elif place[3]==L3[i]:
            if rang4==-1:
                rang4=i
            else:
                rang5=i
        elif place[4]==L3[i]:
            if rang5==-1:
                rang5=i
            else:
                rang6=i
        elif place[5]==L3[i]:
            if rang6==-1:
                rang6=i
            else:
                rang7=i
        elif place[6]==L3[i]:
            if rang7==-1:
                rang7=i
            else:
                rang8=i
        elif place[7]==L3[i]:
            if rang8==-1:
                rang8=i
            else:
                rang9=i
        elif place[8]==L3[i]:
            if rang9==-1:
                rang9=i
            else:
                rang10=i
        elif place[9]==L3[i]:
            if rang10==-1:
                rang10=i
            else:
                rang11=i
        elif place[10]==L3[i]:
            if rang11==-1:
                rang11=i
            
    rang=[]
    rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10,rang11]
    print(rang)
    h=10
    R=open(str(ville)+str(nom)+'Comvot.txt','w+')
    for i in range (h):
        try:
            ajout=Lpers[rang[i]]+"\n"+Ltitre[rang[i]]+"\n"+Lcom[rang[i]]+"\n"+Ldate[rang[i]]+"\n"+Lcont[rang[i]]+"\n"+Lvote[rang[i]]+"\n"
            R.write(ajout)
        except:
            h=h+1
    R.close()
lesliens=['https://www.tripadvisor.fr/Hotel_Review-g303506-d299463-Reviews-Quality_Suites_Rio_de_Janeiro_Botafogo-Rio_de_Janeiro_State_of_Rio_de_Janeiro.html']
          
for i in range (len(lesliens)):
    mettredansdoc(lesliens[i])


