from tkinter import *
from tkinter import ttk

def taille(chaine):
    L=[]
    if len(chaine)>240:
        for i in range (len(chaine)):
            L.append(chaine[i])
        k=0
        
        for i in range (len(L)):
            if (k%240==0) and (k!=0):
                L.insert(k,'\n')
            k=k+1
        chaine="".join(L)
        L=chaine.split("\n")
        del L[-1]
        return L
    else:
        L.append(chaine)
        return L
def searchChichen():
    def tri():
        m=c1.get()
        place=[]
        if m=="prix":
            for i in range (len(Lp)):
                place.append(Lp[i])
            
            place.sort()
            for i in range(len(Lp)):
                if place[0]==Lp[i]:
                    rang1=i
                elif place[1]==Lp[i]:
                    rang2=i
                elif place[2]==Lp[i]:
                    rang3=i
                elif place[3]==Lp[i]:
                    rang4=i
                elif place[4]==Lp[i]:
                    rang5=i
                elif place[5]==Lp[i]:
                    rang6=i
                elif place[6]==Lp[i]:
                    rang7=i
                elif place[7]==Lp[i]:
                    rang8=i
                elif place[8]==Lp[i]:
                    rang9=i
                elif place[9]==Lp[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="note":
            for i in range (len(Ln)):
                place.append(Ln[i])
            
            place.sort(reverse=True)
            for i in range(len(Ln)):
                if place[0]==Ln[i]:
                    rang1=i
                elif place[1]==Ln[i]:
                    rang2=i
                elif place[2]==Ln[i]:
                    rang3=i
                elif place[3]==Ln[i]:
                    rang4=i
                elif place[4]==Ln[i]:
                    rang5=i
                elif place[5]==Ln[i]:
                    rang6=i
                elif place[6]==Ln[i]:
                    rang7=i
                elif place[7]==Ln[i]:
                    rang8=i
                elif place[8]==Ln[i]:
                    rang9=i
                elif place[9]==Ln[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="classement":
            for i in range (len(Lc)):
                place.append(Lc[i])
            
            place.sort()
            for i in range(len(Lc)):
                if place[0]==Lc[i]:
                    rang1=i
                elif place[1]==Lc[i]:
                    rang2=i
                elif place[2]==Lc[i]:
                    rang3=i
                elif place[3]==Lc[i]:
                    rang4=i
                elif place[4]==Lc[i]:
                    rang5=i
                elif place[5]==Lc[i]:
                    rang6=i
                elif place[6]==Lc[i]:
                    rang7=i
                elif place[7]==Lc[i]:
                    rang8=i
                elif place[8]==Lc[i]:
                    rang9=i
                elif place[9]==Lc[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)            
                
    Ln=[]
    Lc=[]
    Lp=[]
    Lpa=[]
    for widget in fenetre.winfo_children():
        widget.destroy()
    fenetre.columnconfigure(0,minsize=1383)
    L1=Label(fenetre, text="Liste des Hotels de Chichen Itza")
    L1.grid(row=0,column=0)
    p1=PanedWindow(fenetre)
    p1.grid(row=1,column=0)
    l1=Label(p1,text="Trier par :")
    l1.grid(row=0,column=0)
    choix=["...","prix","note","classement"]
    c1=ttk.Combobox(p1,values=choix)
    c1.current(0)
    c1.grid(row=0,column=1)
    b1=Button(p1, text="Rechercher",command=tri)
    b1.grid(row=0, column=2)
    
    p2=PanedWindow(fenetre)
    p2.grid(row=2)
    lh=Label(p2,text="Hotel et Bungalows Mayaland")
    lh.grid()
    bc=Button(p2,text="choisir",command=ChBu)
    bc.grid(row=0,column=1)
    Lpa.append(p2)
    pp2=94
    Lp.append(pp2)
    cp2=2
    Lc.append(cp2)
    np2=4.7
    Ln.append(np2)
    
    p3=PanedWindow(fenetre)
    p3.grid(row=3)
    lh=Label(p3,text="La Casa de las Lunas")
    lh.grid()
    bc=Button(p3,text="choisir",command=ChCa)
    bc.grid(row=0,column=1)
    Lpa.append(p3)
    pp3=32
    Lp.append(pp3)
    cp3=100
    Lc.append(cp3)
    np3=4.6
    Ln.append(np3)
    
    p4=PanedWindow(fenetre)
    p4.grid(row=4)
    lh=Label(p4,text="Hacienda Chichen")
    lh.grid()
    bc=Button(p4,text="choisir",command=ChHa)
    bc.grid(row=0,column=1)
    Lpa.append(p4)
    pp4=123
    Lp.append(pp4)
    cp4=1.3
    Lc.append(cp4)
    np4=4.5
    Ln.append(np4)

    p5=PanedWindow(fenetre)
    p5.grid(row=5)
    lh=Label(p5,text="The Lodge at Chichen Itza")
    lh.grid()
    bc=Button(p5,text="choisir",command=ChLo)
    bc.grid(row=0,column=1)
    Lpa.append(p5)
    pp5=185
    Lp.append(pp5)
    cp5=1.2
    Lc.append(cp5)
    np5=4.4
    Ln.append(np5)

    p6=PanedWindow(fenetre)
    p6.grid(row=6)
    lh=Label(p6,text="Hotel Oka'an")
    lh.grid()
    bc=Button(p6,text="choisir",command=ChOk)
    bc.grid(row=0,column=1)
    Lpa.append(p6)
    pp6=56
    Lp.append(pp6)
    cp6=3
    Lc.append(cp6)
    np6=4
    Ln.append(np6)

    p7=PanedWindow(fenetre)
    p7.grid(row=7)
    lh=Label(p7,text="Hotel Chichen Itza")
    lh.grid()
    bc=Button(p7,text="choisir",command=ChCh)
    bc.grid(row=0,column=1)
    Lpa.append(p7)
    pp7=46
    Lp.append(pp7)
    cp7=1.1
    Lc.append(cp7)
    np7=3.9
    Ln.append(np7)

    p8=PanedWindow(fenetre)
    p8.grid(row=8)
    lh=Label(p8,text="Villas Arquelogicas Chichen Itza")
    lh.grid()
    bc=Button(p8,text="choisir",command=ChAr)
    bc.grid(row=0,column=1)
    Lpa.append(p8)
    pp8=77
    Lp.append(pp8)
    cp8=2.3
    Lc.append(cp8)
    np8=3.8
    Ln.append(np8)

    p9=PanedWindow(fenetre)
    p9.grid(row=9)
    lh=Label(p9,text="Hotel DORALBA INN Chichen")
    lh.grid()
    bc=Button(p9,text="choisir",command=ChDo)
    bc.grid(row=0,column=1)
    Lpa.append(p9)
    pp9=39
    Lp.append(pp9)
    cp9=4
    Lc.append(cp9)
    np9=3.4
    Ln.append(np9)

    p10=PanedWindow(fenetre)
    p10.grid(row=10)
    lh=Label(p10,text="Hotel Quinta Marciala")
    lh.grid()
    bc=Button(p10,text="choisir",command=ChQu)
    bc.grid(row=0,column=1)
    Lpa.append(p10)
    pp10=35
    Lp.append(pp10)
    cp10=6
    Lc.append(cp10)
    np10=4.3
    Ln.append(np10)

    p11=PanedWindow(fenetre)
    p11.grid(row=11)
    lh=Label(p11,text="Hotel et Spa Canek")
    lh.grid()
    bc=Button(p11,text="choisir",command=ChRe)
    bc.grid(row=0,column=1)
    Lpa.append(p11)
    pp11=34
    Lp.append(pp11)
    cp11=2.2
    Lc.append(cp11)
    np11=3.6
    Ln.append(np11)

    bretour=Button(fenetre,text="Retour",command=retour)
    bretour.grid(row=12,column=0)
def searchAgra():
    def tri():
        m=c1.get()
        place=[]
        if m=="prix":
            for i in range (len(Lp)):
                place.append(Lp[i])
            
            place.sort()
            for i in range(len(Lp)):
                if place[0]==Lp[i]:
                    rang1=i
                elif place[1]==Lp[i]:
                    rang2=i
                elif place[2]==Lp[i]:
                    rang3=i
                elif place[3]==Lp[i]:
                    rang4=i
                elif place[4]==Lp[i]:
                    rang5=i
                elif place[5]==Lp[i]:
                    rang6=i
                elif place[6]==Lp[i]:
                    rang7=i
                elif place[7]==Lp[i]:
                    rang8=i
                elif place[8]==Lp[i]:
                    rang9=i
                elif place[9]==Lp[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="note":
            for i in range (len(Ln)):
                place.append(Ln[i])
            
            place.sort(reverse=True)
            for i in range(len(Ln)):
                if place[0]==Ln[i]:
                    rang1=i
                elif place[1]==Ln[i]:
                    rang2=i
                elif place[2]==Ln[i]:
                    rang3=i
                elif place[3]==Ln[i]:
                    rang4=i
                elif place[4]==Ln[i]:
                    rang5=i
                elif place[5]==Ln[i]:
                    rang6=i
                elif place[6]==Ln[i]:
                    rang7=i
                elif place[7]==Ln[i]:
                    rang8=i
                elif place[8]==Ln[i]:
                    rang9=i
                elif place[9]==Ln[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="classement":
            for i in range (len(Lc)):
                place.append(Lc[i])
            
            place.sort()
            for i in range(len(Lc)):
                if place[0]==Lc[i]:
                    rang1=i
                elif place[1]==Lc[i]:
                    rang2=i
                elif place[2]==Lc[i]:
                    rang3=i
                elif place[3]==Lc[i]:
                    rang4=i
                elif place[4]==Lc[i]:
                    rang5=i
                elif place[5]==Lc[i]:
                    rang6=i
                elif place[6]==Lc[i]:
                    rang7=i
                elif place[7]==Lc[i]:
                    rang8=i
                elif place[8]==Lc[i]:
                    rang9=i
                elif place[9]==Lc[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)            
                
    Ln=[]
    Lc=[]
    Lp=[]
    Lpa=[]
    for widget in fenetre.winfo_children():
        widget.destroy()
    fenetre.columnconfigure(0,minsize=1383)
    L1=Label(fenetre, text="Liste des Hotels de Agra")
    L1.grid(row=0,column=0)
    p1=PanedWindow(fenetre)
    p1.grid(row=1,column=0)
    l1=Label(p1,text="Trier par :")
    l1.grid(row=0,column=0)
    choix=["...","prix","note","classement"]
    c1=ttk.Combobox(p1,values=choix)
    c1.current(0)
    c1.grid(row=0,column=1)
    b1=Button(p1, text="Rechercher",command=tri)
    b1.grid(row=0, column=2)
    p2=PanedWindow(fenetre)
    p2.grid(row=2)
    lh=Label(p2,text="Tajview")
    lh.grid()
    bc=Button(p2,text="choisir",command=AgTHG)
    bc.grid(row=0,column=1)
    Lpa.append(p2)
    pp2=56
    Lp.append(pp2)
    cp2=11
    Lc.append(cp2)
    np2=4.2
    Ln.append(np2)
    
    p3=PanedWindow(fenetre)
    p3.grid(row=3)
    lh=Label(p3,text="Mansingh Palace")
    lh.grid()
    bc=Button(p3,text="choisir",command=AgMa)
    bc.grid(row=0,column=1)
    Lpa.append(p3)
    pp3=41
    Lp.append(pp3)
    cp3=28
    Lc.append(cp3)
    np3=3.7
    Ln.append(np3)
    
    p4=PanedWindow(fenetre)
    p4.grid(row=4)
    lh=Label(p4,text="Siris 18")
    lh.grid()
    bc=Button(p4,text="choisir",command=AgSi)
    bc.grid(row=0,column=1)
    Lpa.append(p4)
    pp4=23
    Lp.append(pp4)
    cp4=42
    Lc.append(cp4)
    np4=3.6
    Ln.append(np4)

    p5=PanedWindow(fenetre)
    p5.grid(row=5)
    lh=Label(p5,text="Bansi Home Stay")
    lh.grid()
    bc=Button(p5,text="choisir",command=AgBa)
    bc.grid(row=0,column=1)
    Lpa.append(p5)
    pp5=16
    Lp.append(pp5)
    cp5=7
    Lc.append(cp5)
    np5=4.6
    Ln.append(np5)

    p6=PanedWindow(fenetre)
    p6.grid(row=6)
    lh=Label(p6,text="Hotel Clarks shiraz")
    lh.grid()
    bc=Button(p6,text="choisir",command=AgHoc)
    bc.grid(row=0,column=1)
    Lpa.append(p6)
    pp6=40
    Lp.append(pp6)
    cp6=22
    Lc.append(cp6)
    np6=4.1
    Ln.append(np6)

    p7=PanedWindow(fenetre)
    p7.grid(row=7)
    lh=Label(p7,text="Hotel Plaza The Fern")
    lh.grid()
    bc=Button(p7,text="choisir",command=AgHow)
    bc.grid(row=0,column=1)
    Lpa.append(p7)
    pp7=47
    Lp.append(pp7)
    cp7=17
    Lc.append(cp7)
    np7=4
    Ln.append(np7)

    p8=PanedWindow(fenetre)
    p8.grid(row=8)
    lh=Label(p8,text="The Retreat")
    lh.grid()
    bc=Button(p8,text="choisir",command=AgRea)
    bc.grid(row=0,column=1)
    Lpa.append(p8)
    pp8=24
    Lp.append(pp8)
    cp8=27
    Lc.append(cp8)
    np8=3.9
    Ln.append(np8)

    p9=PanedWindow(fenetre)
    p9.grid(row=9)
    lh=Label(p9,text="Crystal Sarovar Premiere")
    lh.grid()
    bc=Button(p9,text="choisir",command=AgCr)
    bc.grid(row=0,column=1)
    Lpa.append(p9)
    pp9=60
    Lp.append(pp9)
    cp9=8
    Lc.append(cp9)
    np9=4.5
    Ln.append(np9)

    p10=PanedWindow(fenetre)
    p10.grid(row=10)
    lh=Label(p10,text="Taj Villa")
    lh.grid()
    bc=Button(p10,text="choisir",command=AgTaj)
    bc.grid(row=0,column=1)
    Lpa.append(p10)
    pp10=25
    Lp.append(pp10)
    cp10=29
    Lc.append(cp10)
    np10=3.8
    Ln.append(np10)

    p11=PanedWindow(fenetre)
    p11.grid(row=11)
    lh=Label(p11,text="Double Tree by Hilton Hotel ")
    lh.grid()
    bc=Button(p11,text="choisir",command=AgDo)
    bc.grid(row=0,column=1)
    Lpa.append(p11)
    pp11=48
    Lp.append(pp11)
    cp11=6
    Lc.append(cp11)
    np11=4.4
    Ln.append(np11)

    bretour=Button(fenetre,text="Retour",command=retour)
    bretour.grid(row=12,column=0)

def searchCaire():
    def tri():
        m=c1.get()
        place=[]
        if m=="prix":
            for i in range (len(Lp)):
                place.append(Lp[i])
            
            place.sort()
            for i in range(len(Lp)):
                if place[0]==Lp[i]:
                    rang1=i
                elif place[1]==Lp[i]:
                    rang2=i
                elif place[2]==Lp[i]:
                    rang3=i
                elif place[3]==Lp[i]:
                    rang4=i
                elif place[4]==Lp[i]:
                    rang5=i
                elif place[5]==Lp[i]:
                    rang6=i
                elif place[6]==Lp[i]:
                    rang7=i
                elif place[7]==Lp[i]:
                    rang8=i
                elif place[8]==Lp[i]:
                    rang9=i
                elif place[9]==Lp[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="note":
            for i in range (len(Ln)):
                place.append(Ln[i])
            
            place.sort(reverse=True)
            for i in range(len(Ln)):
                if place[0]==Ln[i]:
                    rang1=i
                elif place[1]==Ln[i]:
                    rang2=i
                elif place[2]==Ln[i]:
                    rang3=i
                elif place[3]==Ln[i]:
                    rang4=i
                elif place[4]==Ln[i]:
                    rang5=i
                elif place[5]==Ln[i]:
                    rang6=i
                elif place[6]==Ln[i]:
                    rang7=i
                elif place[7]==Ln[i]:
                    rang8=i
                elif place[8]==Ln[i]:
                    rang9=i
                elif place[9]==Ln[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="classement":
            for i in range (len(Lc)):
                place.append(Lc[i])
            
            place.sort()
            for i in range(len(Lc)):
                if place[0]==Lc[i]:
                    rang1=i
                elif place[1]==Lc[i]:
                    rang2=i
                elif place[2]==Lc[i]:
                    rang3=i
                elif place[3]==Lc[i]:
                    rang4=i
                elif place[4]==Lc[i]:
                    rang5=i
                elif place[5]==Lc[i]:
                    rang6=i
                elif place[6]==Lc[i]:
                    rang7=i
                elif place[7]==Lc[i]:
                    rang8=i
                elif place[8]==Lc[i]:
                    rang9=i
                elif place[9]==Lc[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)            
                
    Ln=[]
    Lc=[]
    Lp=[]
    Lpa=[]
    for widget in fenetre.winfo_children():
        widget.destroy()
    fenetre.columnconfigure(0,minsize=1383)
    L1=Label(fenetre, text="Liste des Hotels de Le Caire")
    L1.grid(row=0,column=0)
    p1=PanedWindow(fenetre)
    p1.grid(row=1,column=0)
    l1=Label(p1,text="Trier par :")
    l1.grid(row=0,column=0)
    choix=["...","prix","note","classement"]
    c1=ttk.Combobox(p1,values=choix)
    c1.current(0)
    c1.grid(row=0,column=1)
    b1=Button(p1, text="Rechercher",command=tri)
    b1.grid(row=0, column=2)
    
    p2=PanedWindow(fenetre)
    p2.grid(row=2)
    lh=Label(p2,text="Capital Hotel")
    lh.grid()
    bc=Button(p2,text="choisir",command=CaCah)
    bc.grid(row=0,column=1)
    Lpa.append(p2)
    pp2=33
    Lp.append(pp2)
    cp2=26
    Lc.append(cp2)
    np2=3.5
    Ln.append(np2)
    
    p3=PanedWindow(fenetre)
    p3.grid(row=3)
    lh=Label(p3,text="Baron Hotel Heliopolis Cairo")
    lh.grid()
    bc=Button(p3,text="choisir",command=CaBa)
    bc.grid(row=0,column=1)
    Lpa.append(p3)
    pp3=60
    Lp.append(pp3)
    cp3=34
    Lc.append(cp3)
    np3=3.9
    Ln.append(np3)
    
    p4=PanedWindow(fenetre)
    p4.grid(row=4)
    lh=Label(p4,text="Tiba Pyramids Hotel")
    lh.grid()
    bc=Button(p4,text="choisir",command=CaTi)
    bc.grid(row=0,column=1)
    Lpa.append(p4)
    pp4=23
    Lp.append(pp4)
    cp4=126
    Lc.append(cp4)
    np4=2.5
    Ln.append(np4)

    p5=PanedWindow(fenetre)
    p5.grid(row=5)
    lh=Label(p5,text="The Nile Ritz-Carlton")
    lh.grid()
    bc=Button(p5,text="choisir",command=CaThe)
    bc.grid(row=0,column=1)
    Lpa.append(p5)
    pp5=253
    Lp.append(pp5)
    cp5=10
    Lc.append(cp5)
    np5=4.7
    Ln.append(np5)

    p6=PanedWindow(fenetre)
    p6.grid(row=6)
    lh=Label(p6,text="Steigenberger Hotel El Tahrir")
    lh.grid()
    bc=Button(p6,text="choisir",command=CaSte)
    bc.grid(row=0,column=1)
    Lpa.append(p6)
    pp6=123
    Lp.append(pp6)
    cp6=11
    Lc.append(cp6)
    np6=4.6
    Ln.append(np6)

    p7=PanedWindow(fenetre)
    p7.grid(row=7)
    lh=Label(p7,text="Hilton Cairo World Trade Center Residences")
    lh.grid()
    bc=Button(p7,text="choisir",command=CaHil)
    bc.grid(row=0,column=1)
    Lpa.append(p7)
    pp7=165
    Lp.append(pp7)
    cp7=25
    Lc.append(cp7)
    np7=4.1
    Ln.append(np7)

    p8=PanedWindow(fenetre)
    p8.grid(row=8)
    lh=Label(p8,text="Kempinski Nile Hotel Cairo")
    lh.grid()
    bc=Button(p8,text="choisir",command=CaKem)
    bc.grid(row=0,column=1)
    Lpa.append(p8)
    pp8=169
    Lp.append(pp8)
    cp8=8
    Lc.append(cp8)
    np8=4.5
    Ln.append(np8)

    p9=PanedWindow(fenetre)
    p9.grid(row=9)
    lh=Label(p9,text="Sonesta Hotel, Tower et Casino")
    lh.grid()
    bc=Button(p9,text="choisir",command=CaSon)
    bc.grid(row=0,column=1)
    Lpa.append(p9)
    pp9=107
    Lp.append(pp9)
    cp9=18
    Lc.append(cp9)
    np9=4
    Ln.append(np9)

    p10=PanedWindow(fenetre)
    p10.grid(row=10)
    lh=Label(p10,text="Cairo Mariott Hotel et Omar Khayyaw Caisno")
    lh.grid()
    bc=Button(p10,text="choisir",command=CaMa)
    bc.grid(row=0,column=1)
    Lpa.append(p10)
    pp10=136
    Lp.append(pp10)
    cp10=15
    Lc.append(cp10)
    np10=4.4
    Ln.append(np10)

    p11=PanedWindow(fenetre)
    p11.grid(row=11)
    lh=Label(p11,text="Intercontinental Cairo Semiramis")
    lh.grid()
    bc=Button(p11,text="choisir",command=CaInt)
    bc.grid(row=0,column=1)
    Lpa.append(p11)
    pp11=154
    Lp.append(pp11)
    cp11=19
    Lc.append(cp11)
    np11=4.3
    Ln.append(np11)

    bretour=Button(fenetre,text="Retour",command=retour)
    bretour.grid(row=12,column=0)
def searchRio():
    def tri():
        m=c1.get()
        place=[]
        if m=="prix":
            for i in range (len(Lp)):
                place.append(Lp[i])
            
            place.sort()
            for i in range(len(Lp)):
                if place[0]==Lp[i]:
                    rang1=i
                elif place[1]==Lp[i]:
                    rang2=i
                elif place[2]==Lp[i]:
                    rang3=i
                elif place[3]==Lp[i]:
                    rang4=i
                elif place[4]==Lp[i]:
                    rang5=i
                elif place[5]==Lp[i]:
                    rang6=i
                elif place[6]==Lp[i]:
                    rang7=i
                elif place[7]==Lp[i]:
                    rang8=i
                elif place[8]==Lp[i]:
                    rang9=i
                elif place[9]==Lp[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="note":
            for i in range (len(Ln)):
                place.append(Ln[i])
            
            place.sort(reverse=True)
            for i in range(len(Ln)):
                if place[0]==Ln[i]:
                    rang1=i
                elif place[1]==Ln[i]:
                    rang2=i
                elif place[2]==Ln[i]:
                    rang3=i
                elif place[3]==Ln[i]:
                    rang4=i
                elif place[4]==Ln[i]:
                    rang5=i
                elif place[5]==Ln[i]:
                    rang6=i
                elif place[6]==Ln[i]:
                    rang7=i
                elif place[7]==Ln[i]:
                    rang8=i
                elif place[8]==Ln[i]:
                    rang9=i
                elif place[9]==Ln[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="classement":
            for i in range (len(Lc)):
                place.append(Lc[i])
            
            place.sort()
            for i in range(len(Lc)):
                if place[0]==Lc[i]:
                    rang1=i
                elif place[1]==Lc[i]:
                    rang2=i
                elif place[2]==Lc[i]:
                    rang3=i
                elif place[3]==Lc[i]:
                    rang4=i
                elif place[4]==Lc[i]:
                    rang5=i
                elif place[5]==Lc[i]:
                    rang6=i
                elif place[6]==Lc[i]:
                    rang7=i
                elif place[7]==Lc[i]:
                    rang8=i
                elif place[8]==Lc[i]:
                    rang9=i
                elif place[9]==Lc[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)            
                
    Ln=[]
    Lc=[]
    Lp=[]
    Lpa=[]
    for widget in fenetre.winfo_children():
        widget.destroy()
    fenetre.columnconfigure(0,minsize=1383)
    L1=Label(fenetre, text="Liste des Hotels de Rio de Janeiro")
    L1.grid(row=0,column=0)
    p1=PanedWindow(fenetre)
    p1.grid(row=1,column=0)
    l1=Label(p1,text="Trier par :")
    l1.grid(row=0,column=0)
    choix=["...","prix","note","classement"]
    c1=ttk.Combobox(p1,values=choix)
    c1.current(0)
    c1.grid(row=0,column=1)
    b1=Button(p1, text="Rechercher",command=tri)
    b1.grid(row=0, column=2)
    
    p2=PanedWindow(fenetre)
    p2.grid(row=2)
    lh=Label(p2,text="Altos de Santa Teresa")
    lh.grid()
    bc=Button(p2,text="choisir",command=RiAlto)
    bc.grid(row=0,column=1)
    Lpa.append(p2)
    pp2=80
    Lp.append(pp2)
    cp2=48
    Lc.append(cp2)
    np2=4.3
    Ln.append(np2)
    
    p3=PanedWindow(fenetre)
    p3.grid(row=3)
    lh=Label(p3,text="Les Jardins de Rio")
    lh.grid()
    bc=Button(p3,text="choisir",command=RiJardin)
    bc.grid(row=0,column=1)
    Lpa.append(p3)
    pp3=62
    Lp.append(pp3)
    cp3=56
    Lc.append(cp3)
    np3=4.6
    Ln.append(np3)
    
    p4=PanedWindow(fenetre)
    p4.grid(row=4)
    lh=Label(p4,text="Prodigy Hotel Santos Dumont Airport")
    lh.grid()
    bc=Button(p4,text="choisir",command=RiPro)
    bc.grid(row=0,column=1)
    Lpa.append(p4)
    pp4=52
    Lp.append(pp4)
    cp4=16
    Lc.append(cp4)
    np4=4.7
    Ln.append(np4)

    p5=PanedWindow(fenetre)
    p5.grid(row=5)
    lh=Label(p5,text="Quality Suits")
    lh.grid()
    bc=Button(p5,text="choisir",command=RiQua)
    bc.grid(row=0,column=1)
    Lpa.append(p5)
    pp5=6
    Lp.append(pp5)
    cp5=148
    Lc.append(cp5)
    np5=3.5
    Ln.append(np5)

    p6=PanedWindow(fenetre)
    p6.grid(row=6)
    lh=Label(p6,text="O Veleiro Bed and Breakfast")
    lh.grid()
    bc=Button(p6,text="choisir",command=RiVe)
    bc.grid(row=0,column=1)
    Lpa.append(p6)
    pp6=69
    Lp.append(pp6)
    cp6=12
    Lc.append(cp6)
    np6=4.5
    Ln.append(np6)

    p7=PanedWindow(fenetre)
    p7.grid(row=7)
    lh=Label(p7,text="Mirador Rio Hotel")
    lh.grid()
    bc=Button(p7,text="choisir",command=RiMirador)
    bc.grid(row=0,column=1)
    Lpa.append(p7)
    pp7=61
    Lp.append(pp7)
    cp7=81
    Lc.append(cp7)
    np7=4.1
    Ln.append(np7)

    p8=PanedWindow(fenetre)
    p8.grid(row=8)
    lh=Label(p8,text="Novotel RJ Praia")
    lh.grid()
    bc=Button(p8,text="choisir",command=RiNovotel)
    bc.grid(row=0,column=1)
    Lpa.append(p8)
    pp8=63
    Lp.append(pp8)
    cp8=67
    Lc.append(cp8)
    np8=4.2
    Ln.append(np8)

    p9=PanedWindow(fenetre)
    p9.grid(row=9)
    lh=Label(p9,text="Atlantico Copacabana Hotel")
    lh.grid()
    bc=Button(p9,text="choisir",command=RiAtla)
    bc.grid(row=0,column=1)
    Lpa.append(p9)
    pp9=65
    Lp.append(pp9)
    cp9=261
    Lc.append(cp9)
    np9=3
    Ln.append(np9)

    p10=PanedWindow(fenetre)
    p10.grid(row=10)
    lh=Label(p10,text="PortoBay Rio de Janeiro Hotel ")
    lh.grid()
    bc=Button(p10,text="choisir",command=RiPo)
    bc.grid(row=0,column=1)
    Lpa.append(p10)
    pp10=128
    Lp.append(pp10)
    cp10=21
    Lc.append(cp10)
    np10=4.4
    Ln.append(np10)

    p11=PanedWindow(fenetre)
    p11.grid(row=11)
    lh=Label(p11,text="Windsor Martinique Hotel")
    lh.grid()
    bc=Button(p11,text="choisir",command=RiWi)
    bc.grid(row=0,column=1)
    Lpa.append(p11)
    pp11=62.5
    Lp.append(pp11)
    cp11=35
    Lc.append(cp11)
    np11=4
    Ln.append(np11)
    
    bretour=Button(fenetre,text="Retour",command=retour)
    bretour.grid(row=12,column=0)

    
def searchRome():
    def tri():
        m=c1.get()
        place=[]
        if m=="prix":
            for i in range (len(Lp)):
                place.append(Lp[i])
            
            place.sort()
            for i in range(len(Lp)):
                if place[0]==Lp[i]:
                    rang1=i
                elif place[1]==Lp[i]:
                    rang2=i
                elif place[2]==Lp[i]:
                    rang3=i
                elif place[3]==Lp[i]:
                    rang4=i
                elif place[4]==Lp[i]:
                    rang5=i
                elif place[5]==Lp[i]:
                    rang6=i
                elif place[6]==Lp[i]:
                    rang7=i
                elif place[7]==Lp[i]:
                    rang8=i
                elif place[8]==Lp[i]:
                    rang9=i
                elif place[9]==Lp[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="note":
            for i in range (len(Ln)):
                place.append(Ln[i])
            
            place.sort(reverse=True)
            for i in range(len(Ln)):
                if place[0]==Ln[i]:
                    rang1=i
                elif place[1]==Ln[i]:
                    rang2=i
                elif place[2]==Ln[i]:
                    rang3=i
                elif place[3]==Ln[i]:
                    rang4=i
                elif place[4]==Ln[i]:
                    rang5=i
                elif place[5]==Ln[i]:
                    rang6=i
                elif place[6]==Ln[i]:
                    rang7=i
                elif place[7]==Ln[i]:
                    rang8=i
                elif place[8]==Ln[i]:
                    rang9=i
                elif place[9]==Ln[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="classement":
            for i in range (len(Lc)):
                place.append(Lc[i])
            
            place.sort()
            for i in range(len(Lc)):
                if place[0]==Lc[i]:
                    rang1=i
                elif place[1]==Lc[i]:
                    rang2=i
                elif place[2]==Lc[i]:
                    rang3=i
                elif place[3]==Lc[i]:
                    rang4=i
                elif place[4]==Lc[i]:
                    rang5=i
                elif place[5]==Lc[i]:
                    rang6=i
                elif place[6]==Lc[i]:
                    rang7=i
                elif place[7]==Lc[i]:
                    rang8=i
                elif place[8]==Lc[i]:
                    rang9=i
                elif place[9]==Lc[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)            
                
    Ln=[]
    Lc=[]
    Lp=[]
    Lpa=[]
    for widget in fenetre.winfo_children():
        widget.destroy()
    fenetre.columnconfigure(0,minsize=1383)
    L1=Label(fenetre, text="Liste des Hotels de Rome")
    L1.grid(row=0,column=0)
    p1=PanedWindow(fenetre)
    p1.grid(row=1,column=0)
    l1=Label(p1,text="Trier par :")
    l1.grid(row=0,column=0)
    choix=["...","prix","note","classement"]
    c1=ttk.Combobox(p1,values=choix)
    c1.current(0)
    c1.grid(row=0,column=1)
    b1=Button(p1, text="Rechercher",command=tri)
    b1.grid(row=0, column=2)
    
    p2=PanedWindow(fenetre)
    p2.grid(row=2)
    lh=Label(p2,text="Hotel Artemide")
    lh.grid()
    bc=Button(p2,text="choisir",command=RoArtemide)
    bc.grid(row=0,column=1)
    Lpa.append(p2)
    pp2=216
    Lp.append(pp2)
    cp2=3
    Lc.append(cp2)
    np2=5
    Ln.append(np2)
    
    p3=PanedWindow(fenetre)
    p3.grid(row=3)
    lh=Label(p3,text="The Independente Hotel")
    lh.grid()
    bc=Button(p3,text="choisir",command=RoTI)
    bc.grid(row=0,column=1)
    Lpa.append(p3)
    pp3=131
    Lp.append(pp3)
    cp3=26
    Lc.append(cp3)
    np3=4.9
    Ln.append(np3)
    
    p4=PanedWindow(fenetre)
    p4.grid(row=4)
    lh=Label(p4,text="NH Collection Roma Palazzo Cinquelento")
    lh.grid()
    bc=Button(p4,text="choisir",command=RoNH)
    bc.grid(row=0,column=1)
    Lpa.append(p4)
    pp4=184
    Lp.append(pp4)
    cp4=98
    Lc.append(cp4)
    np4=4.8
    Ln.append(np4)

    p5=PanedWindow(fenetre)
    p5.grid(row=5)
    lh=Label(p5,text="Domus Liberis")
    lh.grid()
    bc=Button(p5,text="choisir",command=RoDomus)
    bc.grid(row=0,column=1)
    Lpa.append(p5)
    pp5=85
    Lp.append(pp5)
    cp5=209
    Lc.append(cp5)
    np5=4.7
    Ln.append(np5)

    p6=PanedWindow(fenetre)
    p6.grid(row=6)
    lh=Label(p6,text="Ariston Hotel")
    lh.grid()
    bc=Button(p6,text="choisir",command=RoAriston)
    bc.grid(row=0,column=1)
    Lpa.append(p6)
    pp6=86
    Lp.append(pp6)
    cp6=200
    Lc.append(cp6)
    np6=4.1
    Ln.append(np6)

    p7=PanedWindow(fenetre)
    p7.grid(row=7)
    lh=Label(p7,text="The K Boutique Hotel")
    lh.grid()
    bc=Button(p7,text="choisir",command=RoTKB)
    bc.grid(row=0,column=1)
    Lpa.append(p7)
    pp7=100
    Lp.append(pp7)
    cp7=160
    Lc.append(cp7)
    np7=4.6
    Ln.append(np7)

    p8=PanedWindow(fenetre)
    p8.grid(row=8)
    lh=Label(p8,text="UNAHOTELS Deco Roma")
    lh.grid()
    bc=Button(p8,text="choisir",command=RoUN)
    bc.grid(row=0,column=1)
    Lpa.append(p8)
    pp8=225
    Lp.append(pp8)
    cp8=159
    Lc.append(cp8)
    np8=4.5
    Ln.append(np8)

    p9=PanedWindow(fenetre)
    p9.grid(row=9)
    lh=Label(p9,text="Rome Times Hotel")
    lh.grid()
    bc=Button(p9,text="choisir",command=RoRome)
    bc.grid(row=0,column=1)
    Lpa.append(p9)
    pp9=124
    Lp.append(pp9)
    cp9=100
    Lc.append(cp9)
    np9=4.5
    Ln.append(np9)

    p10=PanedWindow(fenetre)
    p10.grid(row=10)
    lh=Label(p10,text="Boutique Hotel Campo de Fiori")
    lh.grid()
    bc=Button(p10,text="choisir",command=RoBoutique)
    bc.grid(row=0,column=1)
    Lpa.append(p10)
    pp10=212
    Lp.append(pp10)
    cp10=20
    Lc.append(cp10)
    np10=4.3
    Ln.append(np10)

    p11=PanedWindow(fenetre)
    p11.grid(row=11)
    lh=Label(p11,text="Hotel Alexandra")
    lh.grid()
    bc=Button(p11,text="choisir",command=RoAlex)
    bc.grid(row=0,column=1)
    Lpa.append(p11)
    pp11=118
    Lp.append(pp11)
    cp11=202
    Lc.append(cp11)
    np11=4
    Ln.append(np11)

    bretour=Button(fenetre,text="Retour",command=retour)
    bretour.grid(row=12,column=0)

def afficher(nom,fonction):
    def trie():
        r=Cc.get()
        if (r == 'date'):
            p2=PanedWindow(fenetre)
            p2.grid(row=1,column=0)
            scrollbar = Scrollbar(p2)
            scrollbar.grid(row=0,column=1, sticky=N+S)
            mylist = Listbox(p2 ,width=230,height=35,yscrollcommand = scrollbar.set)
            F=open(str(nom)+'Com.txt','r')
            L=[]
            L1=[]
            k=0
            for i in F.readlines():
                if(k%6==0)and (k!=0):
                    mylist.insert(ANCHOR," "+'')
                    chaine=i
                    L=taille(chaine)
                    for i in range(len(L)):
                        mylist.insert(ANCHOR," "+ L[i])
                else:
                    chaine=i
                    L=taille(chaine)
                    for i in range(len(L)):
                        mylist.insert(END, " "+L[i])    
                k=k+1
            mylist.grid(row=0, column=0, sticky=N+S)
            scrollbar.config(command = mylist.yview)
        
        elif (r == 'contributions'):
            p2=PanedWindow(fenetre)
            p2.grid(row=1,column=0)
            scrollbar = Scrollbar(p2)
            scrollbar.grid(row=0,column=1, sticky=N+S)
            mylist = Listbox(p2 ,width=230,height=35,yscrollcommand = scrollbar.set)
            F=open(str(nom)+'Comcont.txt','r')
            L=[]
            L1=[]
            k=0
            for i in F.readlines():
                if(k%6==0)and (k!=0):
                    mylist.insert(ANCHOR," "+'')
                    chaine=i
                    L=taille(chaine)
                    for i in range(len(L)):
                        mylist.insert(ANCHOR, " "+L[i])
                else:
                    chaine=i
                    L=taille(chaine)
                    for i in range(len(L)):
                        mylist.insert(END, " "+L[i])    
                k=k+1
            mylist.grid(row=0, column=0, sticky=N+S)
            scrollbar.config(command = mylist.yview)

            
        elif (r == 'utilité'):
            p2=PanedWindow(fenetre)
            p2.grid(row=1,column=0)
            scrollbar = Scrollbar(p2)
            scrollbar.grid(row=0,column=1, sticky=N+S)
            mylist = Listbox(p2 ,width=230,height=35,yscrollcommand = scrollbar.set)
            F=open(str(nom)+'Comvot.txt','r')
            L=[]
            L1=[]
            k=0
            for i in F.readlines():
                if(k%6==0)and (k!=0):
                    mylist.insert(ANCHOR," "+'')
                    chaine=i
                    L=taille(chaine)
                    for i in range(len(L)):
                        mylist.insert(ANCHOR, " "+L[i])
                else:
                    chaine=i
                    L=taille(chaine)
                    for i in range(len(L)):
                        mylist.insert(END, " "+L[i])    
                k=k+1
            mylist.grid(row=0, column=0, sticky=N+S)
            scrollbar.config(command = mylist.yview)
        elif (r == 'efficace'):
            p2=PanedWindow(fenetre)
            p2.grid(row=1,column=0)
            scrollbar = Scrollbar(p2)
            scrollbar.grid(row=0,column=1, sticky=N+S)
            mylist = Listbox(p2 ,width=230,height=35,yscrollcommand = scrollbar.set)
            F=open(str(nom)+'Comeff.txt','r')
            L=[]
            L1=[]
            k=0
            for i in F.readlines():
                if(k%6==0)and (k!=0):
                    mylist.insert(ANCHOR," "+'')
                    chaine=i
                    L=taille(chaine)
                    for i in range(len(L)):
                        mylist.insert(ANCHOR, " "+L[i])
                else:
                    chaine=i
                    L=taille(chaine)
                    for i in range(len(L)):
                        mylist.insert(END, " "+L[i])    
                k=k+1
            mylist.grid(row=0, column=0, sticky=N+S)
            scrollbar.config(command = mylist.yview)
    for widget in fenetre.winfo_children():
        widget.destroy()
    fenetre.columnconfigure(0,minsize=1383)
    p1=PanedWindow(fenetre)
    p1.grid(row=0,column=0)
    l=Label(p1,text="Commentaires")
    l.grid(row=0,column=1)
    lc=Label(p1,text="Trier par:")
    lc.grid(row=1,column=0)
    choix=['date','contributions','utilité','efficace']
    Cc=ttk.Combobox(p1,values=choix)
    Cc.grid(row=1,column=1)
    Cc.current(0)
    p2=PanedWindow(fenetre)
    p2.grid(row=1,column=0)
    scrollbar = Scrollbar(p2)
    scrollbar.grid(row=0,column=1, sticky=N+S)
    mylist = Listbox(p2 ,width=230,height=35,yscrollcommand = scrollbar.set)
    p3=PanedWindow(fenetre)
    p3.grid(row=2,column=0)
    F=open(str(nom)+'Com.txt','r')
    L=[]
    k=0
    for i in F.readlines():
        if(k%6==0)and (k!=0):
            mylist.insert(ANCHOR," "+'')
            chaine=i
            L=taille(chaine)
            for i in range(len(L)):
                mylist.insert(ANCHOR, " "+L[i])
        else:
            chaine=i
            L=taille(chaine)
            for i in range(len(L)):
                mylist.insert(END, " "+L[i])    
        k=k+1
    mylist.grid(row=0, column=0, sticky=N+S)
    scrollbar.config(command = mylist.yview)        
    Bc=Button(p1, text="Rechercher",command=trie)
    Bc.grid(row=1,column=2)
    Br=Button(p3,text="Retour",command=fonction)
    Br.grid(row=1,column=0)


    
def ChHa():
    afficher('ChichenHacienda_Chichen',searchChichen)
    
def ChBu():
    afficher('ChichenHotel_Bungalows_Mayaland',searchChichen)

def ChCh():
    afficher('ChichenHotel_Chichen_Itza',searchChichen)

def ChDo():
    afficher('ChichenHotel_DORALBA_INN_Chichen',searchChichen)

def ChOk():
    afficher('ChichenHotel_Oka_an',searchChichen)

def ChQu():
    afficher('ChichenHotel_Quinta_Marciala',searchChichen)

def ChRe():
    afficher('ChichenHotel_Real_Mayab',searchChichen)
    
def ChCa():
    afficher('ChichenLa_Casa_de_las_Lunas',searchChichen)

def ChLo():
    afficher('ChichenThe_Lodge_at_Chichen_Itza',searchChichen)

def ChAr():
    afficher('ChichenVillas_Arqueologicas_Chichen_Itza',searchChichen)
    
def searchChichen():
    def tri():
        m=c1.get()
        place=[]
        if m=="prix":
            for i in range (len(Lp)):
                place.append(Lp[i])
            
            place.sort()
            for i in range(len(Lp)):
                if place[0]==Lp[i]:
                    rang1=i
                elif place[1]==Lp[i]:
                    rang2=i
                elif place[2]==Lp[i]:
                    rang3=i
                elif place[3]==Lp[i]:
                    rang4=i
                elif place[4]==Lp[i]:
                    rang5=i
                elif place[5]==Lp[i]:
                    rang6=i
                elif place[6]==Lp[i]:
                    rang7=i
                elif place[7]==Lp[i]:
                    rang8=i
                elif place[8]==Lp[i]:
                    rang9=i
                elif place[9]==Lp[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="note":
            for i in range (len(Ln)):
                place.append(Ln[i])
            
            place.sort(reverse=True)
            for i in range(len(Ln)):
                if place[0]==Ln[i]:
                    rang1=i
                elif place[1]==Ln[i]:
                    rang2=i
                elif place[2]==Ln[i]:
                    rang3=i
                elif place[3]==Ln[i]:
                    rang4=i
                elif place[4]==Ln[i]:
                    rang5=i
                elif place[5]==Ln[i]:
                    rang6=i
                elif place[6]==Ln[i]:
                    rang7=i
                elif place[7]==Ln[i]:
                    rang8=i
                elif place[8]==Ln[i]:
                    rang9=i
                elif place[9]==Ln[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="classement":
            for i in range (len(Lc)):
                place.append(Lc[i])
            
            place.sort()
            for i in range(len(Lc)):
                if place[0]==Lc[i]:
                    rang1=i
                elif place[1]==Lc[i]:
                    rang2=i
                elif place[2]==Lc[i]:
                    rang3=i
                elif place[3]==Lc[i]:
                    rang4=i
                elif place[4]==Lc[i]:
                    rang5=i
                elif place[5]==Lc[i]:
                    rang6=i
                elif place[6]==Lc[i]:
                    rang7=i
                elif place[7]==Lc[i]:
                    rang8=i
                elif place[8]==Lc[i]:
                    rang9=i
                elif place[9]==Lc[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)            
                
    Ln=[]
    Lc=[]
    Lp=[]
    Lpa=[]
    for widget in fenetre.winfo_children():
        widget.destroy()
    fenetre.columnconfigure(0,minsize=1383)
    L1=Label(fenetre, text="Liste des Hotels de Chichen Itza")
    L1.grid(row=0,column=0)
    p1=PanedWindow(fenetre)
    p1.grid(row=1,column=0)
    l1=Label(p1,text="Trier par :")
    l1.grid(row=0,column=0)
    choix=["...","prix","note","classement"]
    c1=ttk.Combobox(p1,values=choix)
    c1.current(0)
    c1.grid(row=0,column=1)
    b1=Button(p1, text="Rechercher",command=tri)
    b1.grid(row=0, column=2)
    
    p2=PanedWindow(fenetre)
    p2.grid(row=2)
    lh=Label(p2,text="Hotel et Bungalows Mayaland")
    lh.grid()
    bc=Button(p2,text="choisir",command=ChBu)
    bc.grid(row=0,column=1)
    Lpa.append(p2)
    pp2=94
    Lp.append(pp2)
    cp2=2
    Lc.append(cp2)
    np2=4.7
    Ln.append(np2)
    
    p3=PanedWindow(fenetre)
    p3.grid(row=3)
    lh=Label(p3,text="La Casa de las Lunas")
    lh.grid()
    bc=Button(p3,text="choisir",command=ChCa)
    bc.grid(row=0,column=1)
    Lpa.append(p3)
    pp3=32
    Lp.append(pp3)
    cp3=100
    Lc.append(cp3)
    np3=4.6
    Ln.append(np3)
    
    p4=PanedWindow(fenetre)
    p4.grid(row=4)
    lh=Label(p4,text="Hacienda Chichen")
    lh.grid()
    bc=Button(p4,text="choisir",command=ChHa)
    bc.grid(row=0,column=1)
    Lpa.append(p4)
    pp4=123
    Lp.append(pp4)
    cp4=1.3
    Lc.append(cp4)
    np4=4.5
    Ln.append(np4)

    p5=PanedWindow(fenetre)
    p5.grid(row=5)
    lh=Label(p5,text="The Lodge at Chichen Itza")
    lh.grid()
    bc=Button(p5,text="choisir",command=ChLo)
    bc.grid(row=0,column=1)
    Lpa.append(p5)
    pp5=185
    Lp.append(pp5)
    cp5=1.2
    Lc.append(cp5)
    np5=4.4
    Ln.append(np5)

    p6=PanedWindow(fenetre)
    p6.grid(row=6)
    lh=Label(p6,text="Hotel Oka'an")
    lh.grid()
    bc=Button(p6,text="choisir",command=ChOk)
    bc.grid(row=0,column=1)
    Lpa.append(p6)
    pp6=56
    Lp.append(pp6)
    cp6=3
    Lc.append(cp6)
    np6=4
    Ln.append(np6)

    p7=PanedWindow(fenetre)
    p7.grid(row=7)
    lh=Label(p7,text="Hotel Chichen Itza")
    lh.grid()
    bc=Button(p7,text="choisir",command=ChCh)
    bc.grid(row=0,column=1)
    Lpa.append(p7)
    pp7=46
    Lp.append(pp7)
    cp7=1.1
    Lc.append(cp7)
    np7=3.9
    Ln.append(np7)

    p8=PanedWindow(fenetre)
    p8.grid(row=8)
    lh=Label(p8,text="Villas Arquelogicas Chichen Itza")
    lh.grid()
    bc=Button(p8,text="choisir",command=ChAr)
    bc.grid(row=0,column=1)
    Lpa.append(p8)
    pp8=77
    Lp.append(pp8)
    cp8=2.3
    Lc.append(cp8)
    np8=3.8
    Ln.append(np8)

    p9=PanedWindow(fenetre)
    p9.grid(row=9)
    lh=Label(p9,text="Hotel DORALBA INN Chichen")
    lh.grid()
    bc=Button(p9,text="choisir",command=ChDo)
    bc.grid(row=0,column=1)
    Lpa.append(p9)
    pp9=39
    Lp.append(pp9)
    cp9=4
    Lc.append(cp9)
    np9=3.4
    Ln.append(np9)

    p10=PanedWindow(fenetre)
    p10.grid(row=10)
    lh=Label(p10,text="Hotel Quinta Marciala")
    lh.grid()
    bc=Button(p10,text="choisir",command=ChQu)
    bc.grid(row=0,column=1)
    Lpa.append(p10)
    pp10=35
    Lp.append(pp10)
    cp10=6
    Lc.append(cp10)
    np10=4.3
    Ln.append(np10)

    p11=PanedWindow(fenetre)
    p11.grid(row=11)
    lh=Label(p11,text="Hotel et Spa Canek")
    lh.grid()
    bc=Button(p11,text="choisir",command=ChRe)
    bc.grid(row=0,column=1)
    Lpa.append(p11)
    pp11=34
    Lp.append(pp11)
    cp11=2.2
    Lc.append(cp11)
    np11=3.6
    Ln.append(np11)

    bretour=Button(fenetre,text="Retour",command=retour)
    bretour.grid(row=12,column=0)

def AgBa():
    afficher('AgraBansi_Home_Stay',searchAgra)
    
def AgCr():
    afficher('AgraCrystal_Sarovar_Premiere',searchAgra)

def AgDo():
    afficher('AgraDoubleTree_by_Hilton_Hotel_Agra',searchAgra)
    
def AgHoc():
    afficher('AgraHotel_Clarks_Shiraz',searchAgra)
    
def AgHow():
    afficher('AgraHoward_Plaza_The_Fern_Agra',searchAgra)
    
def AgMa():
    afficher('AgraMansingh_Palace_Agra',searchAgra)
    
def AgSi():
    afficher('AgraSiris_18',searchAgra)
    
def AgTaj():
    afficher('AgraTaj_Villa',searchAgra)
    
def AgTHG():
    afficher('AgraThe_Gateway_Hotel_Fatehabad_Road_Agra',searchAgra)
    
def AgRea():
    afficher('AgraThe_Retreat',searchAgra)
            
def searchAgra():
    def tri():
        m=c1.get()
        place=[]
        if m=="prix":
            for i in range (len(Lp)):
                place.append(Lp[i])
            
            place.sort()
            for i in range(len(Lp)):
                if place[0]==Lp[i]:
                    rang1=i
                elif place[1]==Lp[i]:
                    rang2=i
                elif place[2]==Lp[i]:
                    rang3=i
                elif place[3]==Lp[i]:
                    rang4=i
                elif place[4]==Lp[i]:
                    rang5=i
                elif place[5]==Lp[i]:
                    rang6=i
                elif place[6]==Lp[i]:
                    rang7=i
                elif place[7]==Lp[i]:
                    rang8=i
                elif place[8]==Lp[i]:
                    rang9=i
                elif place[9]==Lp[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="note":
            for i in range (len(Ln)):
                place.append(Ln[i])
            
            place.sort(reverse=True)
            for i in range(len(Ln)):
                if place[0]==Ln[i]:
                    rang1=i
                elif place[1]==Ln[i]:
                    rang2=i
                elif place[2]==Ln[i]:
                    rang3=i
                elif place[3]==Ln[i]:
                    rang4=i
                elif place[4]==Ln[i]:
                    rang5=i
                elif place[5]==Ln[i]:
                    rang6=i
                elif place[6]==Ln[i]:
                    rang7=i
                elif place[7]==Ln[i]:
                    rang8=i
                elif place[8]==Ln[i]:
                    rang9=i
                elif place[9]==Ln[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="classement":
            for i in range (len(Lc)):
                place.append(Lc[i])
            
            place.sort()
            for i in range(len(Lc)):
                if place[0]==Lc[i]:
                    rang1=i
                elif place[1]==Lc[i]:
                    rang2=i
                elif place[2]==Lc[i]:
                    rang3=i
                elif place[3]==Lc[i]:
                    rang4=i
                elif place[4]==Lc[i]:
                    rang5=i
                elif place[5]==Lc[i]:
                    rang6=i
                elif place[6]==Lc[i]:
                    rang7=i
                elif place[7]==Lc[i]:
                    rang8=i
                elif place[8]==Lc[i]:
                    rang9=i
                elif place[9]==Lc[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)            
                
    Ln=[]
    Lc=[]
    Lp=[]
    Lpa=[]
    for widget in fenetre.winfo_children():
        widget.destroy()
    fenetre.columnconfigure(0,minsize=1383)
    L1=Label(fenetre, text="Liste des Hotels de Agra")
    L1.grid(row=0,column=0)
    p1=PanedWindow(fenetre)
    p1.grid(row=1,column=0)
    l1=Label(p1,text="Trier par :")
    l1.grid(row=0,column=0)
    choix=["...","prix","note","classement"]
    c1=ttk.Combobox(p1,values=choix)
    c1.current(0)
    c1.grid(row=0,column=1)
    b1=Button(p1, text="Rechercher",command=tri)
    b1.grid(row=0, column=2)
    p2=PanedWindow(fenetre)
    p2.grid(row=2)
    lh=Label(p2,text="Tajview")
    lh.grid()
    bc=Button(p2,text="choisir",command=AgTHG)
    bc.grid(row=0,column=1)
    Lpa.append(p2)
    pp2=56
    Lp.append(pp2)
    cp2=11
    Lc.append(cp2)
    np2=4.2
    Ln.append(np2)
    
    p3=PanedWindow(fenetre)
    p3.grid(row=3)
    lh=Label(p3,text="Mansingh Palace")
    lh.grid()
    bc=Button(p3,text="choisir",command=AgMa)
    bc.grid(row=0,column=1)
    Lpa.append(p3)
    pp3=41
    Lp.append(pp3)
    cp3=28
    Lc.append(cp3)
    np3=3.7
    Ln.append(np3)
    
    p4=PanedWindow(fenetre)
    p4.grid(row=4)
    lh=Label(p4,text="Siris 18")
    lh.grid()
    bc=Button(p4,text="choisir",command=AgSi)
    bc.grid(row=0,column=1)
    Lpa.append(p4)
    pp4=23
    Lp.append(pp4)
    cp4=42
    Lc.append(cp4)
    np4=3.6
    Ln.append(np4)

    p5=PanedWindow(fenetre)
    p5.grid(row=5)
    lh=Label(p5,text="Bansi Home Stay")
    lh.grid()
    bc=Button(p5,text="choisir",command=AgBa)
    bc.grid(row=0,column=1)
    Lpa.append(p5)
    pp5=16
    Lp.append(pp5)
    cp5=7
    Lc.append(cp5)
    np5=4.6
    Ln.append(np5)

    p6=PanedWindow(fenetre)
    p6.grid(row=6)
    lh=Label(p6,text="Hotel Clarks shiraz")
    lh.grid()
    bc=Button(p6,text="choisir",command=AgHoc)
    bc.grid(row=0,column=1)
    Lpa.append(p6)
    pp6=40
    Lp.append(pp6)
    cp6=22
    Lc.append(cp6)
    np6=4.1
    Ln.append(np6)

    p7=PanedWindow(fenetre)
    p7.grid(row=7)
    lh=Label(p7,text="Hotel Plaza The Fern")
    lh.grid()
    bc=Button(p7,text="choisir",command=AgHow)
    bc.grid(row=0,column=1)
    Lpa.append(p7)
    pp7=47
    Lp.append(pp7)
    cp7=17
    Lc.append(cp7)
    np7=4
    Ln.append(np7)

    p8=PanedWindow(fenetre)
    p8.grid(row=8)
    lh=Label(p8,text="The Retreat")
    lh.grid()
    bc=Button(p8,text="choisir",command=AgRea)
    bc.grid(row=0,column=1)
    Lpa.append(p8)
    pp8=24
    Lp.append(pp8)
    cp8=27
    Lc.append(cp8)
    np8=3.9
    Ln.append(np8)

    p9=PanedWindow(fenetre)
    p9.grid(row=9)
    lh=Label(p9,text="Crystal Sarovar Premiere")
    lh.grid()
    bc=Button(p9,text="choisir",command=AgCr)
    bc.grid(row=0,column=1)
    Lpa.append(p9)
    pp9=60
    Lp.append(pp9)
    cp9=8
    Lc.append(cp9)
    np9=4.5
    Ln.append(np9)

    p10=PanedWindow(fenetre)
    p10.grid(row=10)
    lh=Label(p10,text="Taj Villa")
    lh.grid()
    bc=Button(p10,text="choisir",command=AgTaj)
    bc.grid(row=0,column=1)
    Lpa.append(p10)
    pp10=25
    Lp.append(pp10)
    cp10=29
    Lc.append(cp10)
    np10=3.8
    Ln.append(np10)

    p11=PanedWindow(fenetre)
    p11.grid(row=11)
    lh=Label(p11,text="Double Tree by Hilton Hotel ")
    lh.grid()
    bc=Button(p11,text="choisir",command=AgDo)
    bc.grid(row=0,column=1)
    Lpa.append(p11)
    pp11=48
    Lp.append(pp11)
    cp11=6
    Lc.append(cp11)
    np11=4.4
    Ln.append(np11)

    bretour=Button(fenetre,text="Retour",command=retour)
    bretour.grid(row=12,column=0)

def CaBa():
    afficher('CaireBaron_Hotel_Heliopolis_Cairo',searchCaire)
    
def CaMa():
    afficher('CaireCairo_Marriott_Hotel_Omar_Khayyam_Casino',searchCaire)
    
def CaCah():
    afficher('CaireCapital_Hotel',searchCaire)
    
def CaHil():
    afficher('CaireHilton_Cairo_World_Trade_Center_Residences',searchCaire)
    
def CaInt():
    afficher('CaireInterContinental_Cairo_Semiramis',searchCaire)
    
def CaKem():
    afficher('CaireKempinski_Nile_Hotel_Cairo',searchCaire)
    
def CaSon():
    afficher('CaireSonesta_Hotel_Tower_Casino_Cairo',searchCaire)
    
def CaSte():
    afficher('CaireSteigenberger_Hotel_El_Tahrir',searchCaire)
    
def CaThe():
    afficher('CaireThe_Nile_Ritz_Carlton_Cairo',searchCaire)
    
def CaTi():
    afficher('CaireTiba_Pyramids_Hotel',searchCaire)
    
def searchCaire():
    def tri():
        m=c1.get()
        place=[]
        if m=="prix":
            for i in range (len(Lp)):
                place.append(Lp[i])
            
            place.sort()
            for i in range(len(Lp)):
                if place[0]==Lp[i]:
                    rang1=i
                elif place[1]==Lp[i]:
                    rang2=i
                elif place[2]==Lp[i]:
                    rang3=i
                elif place[3]==Lp[i]:
                    rang4=i
                elif place[4]==Lp[i]:
                    rang5=i
                elif place[5]==Lp[i]:
                    rang6=i
                elif place[6]==Lp[i]:
                    rang7=i
                elif place[7]==Lp[i]:
                    rang8=i
                elif place[8]==Lp[i]:
                    rang9=i
                elif place[9]==Lp[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="note":
            for i in range (len(Ln)):
                place.append(Ln[i])
            
            place.sort(reverse=True)
            for i in range(len(Ln)):
                if place[0]==Ln[i]:
                    rang1=i
                elif place[1]==Ln[i]:
                    rang2=i
                elif place[2]==Ln[i]:
                    rang3=i
                elif place[3]==Ln[i]:
                    rang4=i
                elif place[4]==Ln[i]:
                    rang5=i
                elif place[5]==Ln[i]:
                    rang6=i
                elif place[6]==Ln[i]:
                    rang7=i
                elif place[7]==Ln[i]:
                    rang8=i
                elif place[8]==Ln[i]:
                    rang9=i
                elif place[9]==Ln[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="classement":
            for i in range (len(Lc)):
                place.append(Lc[i])
            
            place.sort()
            for i in range(len(Lc)):
                if place[0]==Lc[i]:
                    rang1=i
                elif place[1]==Lc[i]:
                    rang2=i
                elif place[2]==Lc[i]:
                    rang3=i
                elif place[3]==Lc[i]:
                    rang4=i
                elif place[4]==Lc[i]:
                    rang5=i
                elif place[5]==Lc[i]:
                    rang6=i
                elif place[6]==Lc[i]:
                    rang7=i
                elif place[7]==Lc[i]:
                    rang8=i
                elif place[8]==Lc[i]:
                    rang9=i
                elif place[9]==Lc[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)            
                
    Ln=[]
    Lc=[]
    Lp=[]
    Lpa=[]
    for widget in fenetre.winfo_children():
        widget.destroy()
    fenetre.columnconfigure(0,minsize=1383)
    L1=Label(fenetre, text="Liste des Hotels de Le Caire")
    L1.grid(row=0,column=0)
    p1=PanedWindow(fenetre)
    p1.grid(row=1,column=0)
    l1=Label(p1,text="Trier par :")
    l1.grid(row=0,column=0)
    choix=["...","prix","note","classement"]
    c1=ttk.Combobox(p1,values=choix)
    c1.current(0)
    c1.grid(row=0,column=1)
    b1=Button(p1, text="Rechercher",command=tri)
    b1.grid(row=0, column=2)
    
    p2=PanedWindow(fenetre)
    p2.grid(row=2)
    lh=Label(p2,text="Capital Hotel")
    lh.grid()
    bc=Button(p2,text="choisir",command=CaCah)
    bc.grid(row=0,column=1)
    Lpa.append(p2)
    pp2=33
    Lp.append(pp2)
    cp2=26
    Lc.append(cp2)
    np2=3.5
    Ln.append(np2)
    
    p3=PanedWindow(fenetre)
    p3.grid(row=3)
    lh=Label(p3,text="Baron Hotel Heliopolis Cairo")
    lh.grid()
    bc=Button(p3,text="choisir",command=CaBa)
    bc.grid(row=0,column=1)
    Lpa.append(p3)
    pp3=60
    Lp.append(pp3)
    cp3=34
    Lc.append(cp3)
    np3=3.9
    Ln.append(np3)
    
    p4=PanedWindow(fenetre)
    p4.grid(row=4)
    lh=Label(p4,text="Tiba Pyramids Hotel")
    lh.grid()
    bc=Button(p4,text="choisir",command=CaTi)
    bc.grid(row=0,column=1)
    Lpa.append(p4)
    pp4=23
    Lp.append(pp4)
    cp4=126
    Lc.append(cp4)
    np4=2.5
    Ln.append(np4)

    p5=PanedWindow(fenetre)
    p5.grid(row=5)
    lh=Label(p5,text="The Nile Ritz-Carlton")
    lh.grid()
    bc=Button(p5,text="choisir",command=CaThe)
    bc.grid(row=0,column=1)
    Lpa.append(p5)
    pp5=253
    Lp.append(pp5)
    cp5=10
    Lc.append(cp5)
    np5=4.7
    Ln.append(np5)

    p6=PanedWindow(fenetre)
    p6.grid(row=6)
    lh=Label(p6,text="Steigenberger Hotel El Tahrir")
    lh.grid()
    bc=Button(p6,text="choisir",command=CaSte)
    bc.grid(row=0,column=1)
    Lpa.append(p6)
    pp6=123
    Lp.append(pp6)
    cp6=11
    Lc.append(cp6)
    np6=4.6
    Ln.append(np6)

    p7=PanedWindow(fenetre)
    p7.grid(row=7)
    lh=Label(p7,text="Hilton Cairo World Trade Center Residences")
    lh.grid()
    bc=Button(p7,text="choisir",command=CaHil)
    bc.grid(row=0,column=1)
    Lpa.append(p7)
    pp7=165
    Lp.append(pp7)
    cp7=25
    Lc.append(cp7)
    np7=4.1
    Ln.append(np7)

    p8=PanedWindow(fenetre)
    p8.grid(row=8)
    lh=Label(p8,text="Kempinski Nile Hotel Cairo")
    lh.grid()
    bc=Button(p8,text="choisir",command=CaKem)
    bc.grid(row=0,column=1)
    Lpa.append(p8)
    pp8=169
    Lp.append(pp8)
    cp8=8
    Lc.append(cp8)
    np8=4.5
    Ln.append(np8)

    p9=PanedWindow(fenetre)
    p9.grid(row=9)
    lh=Label(p9,text="Sonesta Hotel, Tower et Casino")
    lh.grid()
    bc=Button(p9,text="choisir",command=CaSon)
    bc.grid(row=0,column=1)
    Lpa.append(p9)
    pp9=107
    Lp.append(pp9)
    cp9=18
    Lc.append(cp9)
    np9=4
    Ln.append(np9)

    p10=PanedWindow(fenetre)
    p10.grid(row=10)
    lh=Label(p10,text="Cairo Mariott Hotel et Omar Khayyaw Caisno")
    lh.grid()
    bc=Button(p10,text="choisir",command=CaMa)
    bc.grid(row=0,column=1)
    Lpa.append(p10)
    pp10=136
    Lp.append(pp10)
    cp10=15
    Lc.append(cp10)
    np10=4.4
    Ln.append(np10)

    p11=PanedWindow(fenetre)
    p11.grid(row=11)
    lh=Label(p11,text="Intercontinental Cairo Semiramis")
    lh.grid()
    bc=Button(p11,text="choisir",command=CaInt)
    bc.grid(row=0,column=1)
    Lpa.append(p11)
    pp11=154
    Lp.append(pp11)
    cp11=19
    Lc.append(cp11)
    np11=4.3
    Ln.append(np11)

    bretour=Button(fenetre,text="Retour",command=retour)
    bretour.grid(row=12,column=0)

def RiAlto():
    afficher('RioAltos_de_Santa_Teresa',searchRio)
    
def RiAtla():
    afficher('RioAtlantico_Copacabana_Hotel',searchRio)
    
def RiJardin():
    afficher('RioLes_Jardins_de_Rio',searchRio)
    
def RiMirador():
    afficher('RioMirador_Rio_Hotel',searchRio)
    
def RiNovotel():
    afficher('RioNovotel_RJ_Praia_de_Botafogo',searchRio)
    
def RiVe():
    afficher('RioO_Veleiro_Bed_and_Breakfast',searchRio)
    
def RiPo():
    afficher('RioPortoBay_Rio_de_Janeiro_Hotel',searchRio)
    
def RiPro():
    afficher('RioProdigy_Hotel_Santos_Dumont_Airport',searchRio)

def RiQua():
    afficher('RioQuality_Suites_Rio_de_Janeiro_Botafogo',searchRio)
    
def RiWi():
    afficher('RioWindsor_Martinique_Hotel',searchRio)
    
def searchRio():
    def tri():
        m=c1.get()
        place=[]
        if m=="prix":
            for i in range (len(Lp)):
                place.append(Lp[i])
            
            place.sort()
            for i in range(len(Lp)):
                if place[0]==Lp[i]:
                    rang1=i
                elif place[1]==Lp[i]:
                    rang2=i
                elif place[2]==Lp[i]:
                    rang3=i
                elif place[3]==Lp[i]:
                    rang4=i
                elif place[4]==Lp[i]:
                    rang5=i
                elif place[5]==Lp[i]:
                    rang6=i
                elif place[6]==Lp[i]:
                    rang7=i
                elif place[7]==Lp[i]:
                    rang8=i
                elif place[8]==Lp[i]:
                    rang9=i
                elif place[9]==Lp[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="note":
            for i in range (len(Ln)):
                place.append(Ln[i])
            
            place.sort(reverse=True)
            for i in range(len(Ln)):
                if place[0]==Ln[i]:
                    rang1=i
                elif place[1]==Ln[i]:
                    rang2=i
                elif place[2]==Ln[i]:
                    rang3=i
                elif place[3]==Ln[i]:
                    rang4=i
                elif place[4]==Ln[i]:
                    rang5=i
                elif place[5]==Ln[i]:
                    rang6=i
                elif place[6]==Ln[i]:
                    rang7=i
                elif place[7]==Ln[i]:
                    rang8=i
                elif place[8]==Ln[i]:
                    rang9=i
                elif place[9]==Ln[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="classement":
            for i in range (len(Lc)):
                place.append(Lc[i])
            
            place.sort()
            for i in range(len(Lc)):
                if place[0]==Lc[i]:
                    rang1=i
                elif place[1]==Lc[i]:
                    rang2=i
                elif place[2]==Lc[i]:
                    rang3=i
                elif place[3]==Lc[i]:
                    rang4=i
                elif place[4]==Lc[i]:
                    rang5=i
                elif place[5]==Lc[i]:
                    rang6=i
                elif place[6]==Lc[i]:
                    rang7=i
                elif place[7]==Lc[i]:
                    rang8=i
                elif place[8]==Lc[i]:
                    rang9=i
                elif place[9]==Lc[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)            
                
    Ln=[]
    Lc=[]
    Lp=[]
    Lpa=[]
    for widget in fenetre.winfo_children():
        widget.destroy()
    fenetre.columnconfigure(0,minsize=1383)
    L1=Label(fenetre, text="Liste des Hotels de Rio de Janeiro")
    L1.grid(row=0,column=0)
    p1=PanedWindow(fenetre)
    p1.grid(row=1,column=0)
    l1=Label(p1,text="Trier par :")
    l1.grid(row=0,column=0)
    choix=["...","prix","note","classement"]
    c1=ttk.Combobox(p1,values=choix)
    c1.current(0)
    c1.grid(row=0,column=1)
    b1=Button(p1, text="Rechercher",command=tri)
    b1.grid(row=0, column=2)
    
    p2=PanedWindow(fenetre)
    p2.grid(row=2)
    lh=Label(p2,text="Altos de Santa Teresa")
    lh.grid()
    bc=Button(p2,text="choisir",command=RiAlto)
    bc.grid(row=0,column=1)
    Lpa.append(p2)
    pp2=80
    Lp.append(pp2)
    cp2=48
    Lc.append(cp2)
    np2=4.3
    Ln.append(np2)
    
    p3=PanedWindow(fenetre)
    p3.grid(row=3)
    lh=Label(p3,text="Les Jardins de Rio")
    lh.grid()
    bc=Button(p3,text="choisir",command=RiJardin)
    bc.grid(row=0,column=1)
    Lpa.append(p3)
    pp3=62
    Lp.append(pp3)
    cp3=56
    Lc.append(cp3)
    np3=4.6
    Ln.append(np3)
    
    p4=PanedWindow(fenetre)
    p4.grid(row=4)
    lh=Label(p4,text="Prodigy Hotel Santos Dumont Airport")
    lh.grid()
    bc=Button(p4,text="choisir",command=RiPro)
    bc.grid(row=0,column=1)
    Lpa.append(p4)
    pp4=52
    Lp.append(pp4)
    cp4=16
    Lc.append(cp4)
    np4=4.7
    Ln.append(np4)

    p5=PanedWindow(fenetre)
    p5.grid(row=5)
    lh=Label(p5,text="Quality Suits")
    lh.grid()
    bc=Button(p5,text="choisir",command=RiQua)
    bc.grid(row=0,column=1)
    Lpa.append(p5)
    pp5=6
    Lp.append(pp5)
    cp5=148
    Lc.append(cp5)
    np5=3.5
    Ln.append(np5)

    p6=PanedWindow(fenetre)
    p6.grid(row=6)
    lh=Label(p6,text="O Veleiro Bed and Breakfast")
    lh.grid()
    bc=Button(p6,text="choisir",command=RiVe)
    bc.grid(row=0,column=1)
    Lpa.append(p6)
    pp6=69
    Lp.append(pp6)
    cp6=12
    Lc.append(cp6)
    np6=4.5
    Ln.append(np6)

    p7=PanedWindow(fenetre)
    p7.grid(row=7)
    lh=Label(p7,text="Mirador Rio Hotel")
    lh.grid()
    bc=Button(p7,text="choisir",command=RiMirador)
    bc.grid(row=0,column=1)
    Lpa.append(p7)
    pp7=61
    Lp.append(pp7)
    cp7=81
    Lc.append(cp7)
    np7=4.1
    Ln.append(np7)

    p8=PanedWindow(fenetre)
    p8.grid(row=8)
    lh=Label(p8,text="Novotel RJ Praia")
    lh.grid()
    bc=Button(p8,text="choisir",command=RiNovotel)
    bc.grid(row=0,column=1)
    Lpa.append(p8)
    pp8=63
    Lp.append(pp8)
    cp8=67
    Lc.append(cp8)
    np8=4.2
    Ln.append(np8)

    p9=PanedWindow(fenetre)
    p9.grid(row=9)
    lh=Label(p9,text="Atlantico Copacabana Hotel")
    lh.grid()
    bc=Button(p9,text="choisir",command=RiAtla)
    bc.grid(row=0,column=1)
    Lpa.append(p9)
    pp9=65
    Lp.append(pp9)
    cp9=261
    Lc.append(cp9)
    np9=3
    Ln.append(np9)

    p10=PanedWindow(fenetre)
    p10.grid(row=10)
    lh=Label(p10,text="PortoBay Rio de Janeiro Hotel ")
    lh.grid()
    bc=Button(p10,text="choisir",command=RiPo)
    bc.grid(row=0,column=1)
    Lpa.append(p10)
    pp10=128
    Lp.append(pp10)
    cp10=21
    Lc.append(cp10)
    np10=4.4
    Ln.append(np10)

    p11=PanedWindow(fenetre)
    p11.grid(row=11)
    lh=Label(p11,text="Windsor Martinique Hotel")
    lh.grid()
    bc=Button(p11,text="choisir",command=RiWi)
    bc.grid(row=0,column=1)
    Lpa.append(p11)
    pp11=62.5
    Lp.append(pp11)
    cp11=35
    Lc.append(cp11)
    np11=4
    Ln.append(np11)
    
    bretour=Button(fenetre,text="Retour",command=retour)
    bretour.grid(row=12,column=0)


def RoAlex():
    afficher('RomeHotel_Alexandra',searchRome)
    
def RoAriston():
    afficher('RomeAriston_Hotel',searchRome)
    
def RoBoutique():
    afficher('RomeBoutique_Hotel_Campo_de_Fiori',searchRome)
    
def RoDomus():
    afficher('RomeDomus_Liberius',searchRome)
    
def RoArtemide():
    afficher('RomeHotel_Artemide',searchRome)
    
def RoNH():
    afficher('RomeNH_Collection_Roma_Palazzo_Cinquecento',searchRome)
    
def RoRome():
    afficher('RomeRome_Times_Hotel',searchRome)
    
def RoTI():
    afficher('RomeThe_Independent_Hotel',searchRome)
    
def RoTKB():
    afficher('RomeThe_K_Boutique_Hotel',searchRome)
    
def RoUN():
    afficher('RomeUNAHOTELS_Deco_Roma',searchRome)
    
    
def searchRome():
    def tri():
        m=c1.get()
        place=[]
        if m=="prix":
            for i in range (len(Lp)):
                place.append(Lp[i])
            
            place.sort()
            for i in range(len(Lp)):
                if place[0]==Lp[i]:
                    rang1=i
                elif place[1]==Lp[i]:
                    rang2=i
                elif place[2]==Lp[i]:
                    rang3=i
                elif place[3]==Lp[i]:
                    rang4=i
                elif place[4]==Lp[i]:
                    rang5=i
                elif place[5]==Lp[i]:
                    rang6=i
                elif place[6]==Lp[i]:
                    rang7=i
                elif place[7]==Lp[i]:
                    rang8=i
                elif place[8]==Lp[i]:
                    rang9=i
                elif place[9]==Lp[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            print(rang)
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="note":
            for i in range (len(Ln)):
                place.append(Ln[i])
            
            place.sort(reverse=True)
            for i in range(len(Ln)):
                if place[0]==Ln[i]:
                    rang1=i
                elif place[1]==Ln[i]:
                    rang2=i
                elif place[2]==Ln[i]:
                    rang3=i
                elif place[3]==Ln[i]:
                    rang4=i
                elif place[4]==Ln[i]:
                    rang5=i
                elif place[5]==Ln[i]:
                    rang6=i
                elif place[6]==Ln[i]:
                    rang7=i
                elif place[7]==Ln[i]:
                    rang8=i
                elif place[8]==Ln[i]:
                    rang9=i
                elif place[9]==Ln[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)
        elif m=="classement":
            for i in range (len(Lc)):
                place.append(Lc[i])
            
            place.sort()
            for i in range(len(Lc)):
                if place[0]==Lc[i]:
                    rang1=i
                elif place[1]==Lc[i]:
                    rang2=i
                elif place[2]==Lc[i]:
                    rang3=i
                elif place[3]==Lc[i]:
                    rang4=i
                elif place[4]==Lc[i]:
                    rang5=i
                elif place[5]==Lc[i]:
                    rang6=i
                elif place[6]==Lc[i]:
                    rang7=i
                elif place[7]==Lc[i]:
                    rang8=i
                elif place[8]==Lc[i]:
                    rang9=i
                elif place[9]==Lc[i]:
                    rang10=i
            rang=[rang1,rang2,rang3,rang4,rang5,rang6,rang7,rang8,rang9,rang10]
            for i in range(len(rang)):
                r=Lpa[rang[i]]
                n=2+i
                r.grid(row=n,column=0)            
                
    Ln=[]
    Lc=[]
    Lp=[]
    Lpa=[]
    for widget in fenetre.winfo_children():
        widget.destroy()
    fenetre.columnconfigure(0,minsize=1383)
    L1=Label(fenetre, text="Liste des Hotels de Rome")
    L1.grid(row=0,column=0)
    p1=PanedWindow(fenetre)
    p1.grid(row=1,column=0)
    l1=Label(p1,text="Trier par :")
    l1.grid(row=0,column=0)
    choix=["...","prix","note","classement"]
    c1=ttk.Combobox(p1,values=choix)
    c1.current(0)
    c1.grid(row=0,column=1)
    b1=Button(p1, text="Rechercher",command=tri)
    b1.grid(row=0, column=2)
    
    p2=PanedWindow(fenetre)
    p2.grid(row=2)
    lh=Label(p2,text="Hotel Artemide")
    lh.grid()
    bc=Button(p2,text="choisir",command=RoArtemide)
    bc.grid(row=0,column=1)
    Lpa.append(p2)
    pp2=216
    Lp.append(pp2)
    cp2=3
    Lc.append(cp2)
    np2=5
    Ln.append(np2)
    
    p3=PanedWindow(fenetre)
    p3.grid(row=3)
    lh=Label(p3,text="The Independente Hotel")
    lh.grid()
    bc=Button(p3,text="choisir",command=RoTI)
    bc.grid(row=0,column=1)
    Lpa.append(p3)
    pp3=131
    Lp.append(pp3)
    cp3=26
    Lc.append(cp3)
    np3=4.9
    Ln.append(np3)
    
    p4=PanedWindow(fenetre)
    p4.grid(row=4)
    lh=Label(p4,text="NH Collection Roma Palazzo Cinquelento")
    lh.grid()
    bc=Button(p4,text="choisir",command=RoNH)
    bc.grid(row=0,column=1)
    Lpa.append(p4)
    pp4=184
    Lp.append(pp4)
    cp4=98
    Lc.append(cp4)
    np4=4.8
    Ln.append(np4)

    p5=PanedWindow(fenetre)
    p5.grid(row=5)
    lh=Label(p5,text="Domus Liberis")
    lh.grid()
    bc=Button(p5,text="choisir",command=RoDomus)
    bc.grid(row=0,column=1)
    Lpa.append(p5)
    pp5=85
    Lp.append(pp5)
    cp5=209
    Lc.append(cp5)
    np5=4.7
    Ln.append(np5)

    p6=PanedWindow(fenetre)
    p6.grid(row=6)
    lh=Label(p6,text="Ariston Hotel")
    lh.grid()
    bc=Button(p6,text="choisir",command=RoAriston)
    bc.grid(row=0,column=1)
    Lpa.append(p6)
    pp6=86
    Lp.append(pp6)
    cp6=200
    Lc.append(cp6)
    np6=4.1
    Ln.append(np6)

    p7=PanedWindow(fenetre)
    p7.grid(row=7)
    lh=Label(p7,text="The K Boutique Hotel")
    lh.grid()
    bc=Button(p7,text="choisir",command=RoTKB)
    bc.grid(row=0,column=1)
    Lpa.append(p7)
    pp7=100
    Lp.append(pp7)
    cp7=160
    Lc.append(cp7)
    np7=4.6
    Ln.append(np7)

    p8=PanedWindow(fenetre)
    p8.grid(row=8)
    lh=Label(p8,text="UNAHOTELS Deco Roma")
    lh.grid()
    bc=Button(p8,text="choisir",command=RoUN)
    bc.grid(row=0,column=1)
    Lpa.append(p8)
    pp8=225
    Lp.append(pp8)
    cp8=159
    Lc.append(cp8)
    np8=4.5
    Ln.append(np8)

    p9=PanedWindow(fenetre)
    p9.grid(row=9)
    lh=Label(p9,text="Rome Times Hotel")
    lh.grid()
    bc=Button(p9,text="choisir",command=RoRome)
    bc.grid(row=0,column=1)
    Lpa.append(p9)
    pp9=124
    Lp.append(pp9)
    cp9=100
    Lc.append(cp9)
    np9=4.5
    Ln.append(np9)

    p10=PanedWindow(fenetre)
    p10.grid(row=10)
    lh=Label(p10,text="Boutique Hotel Campo de Fiori")
    lh.grid()
    bc=Button(p10,text="choisir",command=RoBoutique)
    bc.grid(row=0,column=1)
    Lpa.append(p10)
    pp10=212
    Lp.append(pp10)
    cp10=20
    Lc.append(cp10)
    np10=4.3
    Ln.append(np10)

    p11=PanedWindow(fenetre)
    p11.grid(row=11)
    lh=Label(p11,text="Hotel Alexandra")
    lh.grid()
    bc=Button(p11,text="choisir",command=RoAlex)
    bc.grid(row=0,column=1)
    Lpa.append(p11)
    pp11=118
    Lp.append(pp11)
    cp11=202
    Lc.append(cp11)
    np11=4
    Ln.append(np11)

    bretour=Button(fenetre,text="Retour",command=retour)
    bretour.grid(row=12,column=0)
def recherche():
    m=c1.get()
    if m=="Agra":
        searchAgra()
    elif m=="Chichén Itzá":
        searchChichen()
    elif m=="Le Caire":
        searchCaire()
    elif m=="Rio de Janeiro":
        searchRio()
    elif m=="Rome":
        searchRome()
def questionnaire():
    master= Toplevel(fenetre)
    master.title("Questionnaire de voyage")
    master.configure(bg='black')
    p1=PanedWindow(master,bg ='black')
    p1.grid(row=0,column=0)
    p2=PanedWindow(master,bg ='grey')
    p2.grid(row=1,column=0)
    p3=PanedWindow(master,bg ='black')
    p3.grid(row=2,column=0)
    p4=PanedWindow(master,bg ='grey')
    p4.grid(row=3,column=0)
    p7=PanedWindow(master,bg ='black')
    p7.grid(row=4,column=0)
    p8=PanedWindow(master,bg ='grey')
    p8.grid(row=5,column=0)
    p9=PanedWindow(master,bg ='black')
    p9.grid(row=6,column=0)
    p10=PanedWindow(master,bg ='grey')
    p10.grid(row=7,column=0)
    p11=PanedWindow(master,bg='black')
    p11.grid(row=8,column=0)
    p12=PanedWindow(master,bg ='grey')
    p12.grid(row=9,column=0)
    p13=PanedWindow(master,bg ='black')
    p13.grid(row=10,column=0)
    label=Label(p1,text='Quel continent voudriez-vous visiter ?',bg='black',fg='white',font='size 15')
    s1 = IntVar()
    s2 = IntVar()
    s3 = IntVar()
    s4 = IntVar()
    s5 = IntVar()
    rad1 = Checkbutton(p2,text='Europe',activeforeground="gold",overrelief=SUNKEN,variable=s1,bg ='grey',font='size 12')
    rad2 = Checkbutton(p2,text='Asie',activeforeground="gold",overrelief=SUNKEN,variable=s2,bg ='grey',font='size 12')
    rad3 = Checkbutton(p2,text='Amérique du nord',activeforeground="gold",overrelief=SUNKEN,variable=s3,bg ='grey',font='size 12')
    rad4 = Checkbutton(p2,text='Afrique',activeforeground="gold",overrelief=SUNKEN,variable=s4,bg ='grey',font='size 12')
    rad44 = Checkbutton(p2,text='Amérique du sud',activeforeground="gold",overrelief=SUNKEN,variable=s5,bg ='grey',font='size 12')
    label1=Label(p3,text='Quel est votre élément ?',bg='black',fg='white',font='size 15')
    a1 = IntVar()
    a2 = IntVar()
    a3 = IntVar()
    a4 = IntVar()
    rad5 = Checkbutton(p4,text='Eau',activeforeground="gold",overrelief=SUNKEN,variable=a1,bg ='grey',font='size 12')
    rad6 = Checkbutton(p4,text='Feu',activeforeground="gold",overrelief=SUNKEN,variable=a2,bg ='grey',font='size 12')
    rad7 = Checkbutton(p4,text='Terre',activeforeground="gold",overrelief=SUNKEN,variable=a3,bg ='grey',font='size 12')
    rad8 = Checkbutton(p4,text='Air',activeforeground="gold",overrelief=SUNKEN,variable=a4,bg ='grey',font='size 12')
    label3=Label(p7,text='De quelle nature êtes-vous ?',bg='black',fg='white',font='size 15')
    w1 = IntVar()
    w4 = IntVar()
    rad13 = Checkbutton(p8,text='Calme et patient',activeforeground="gold",overrelief=SUNKEN,variable=w1,bg ='grey',font='size 12')
    rad16 = Checkbutton(p8,text='Speed et impatient',activeforeground="gold",overrelief=SUNKEN,variable=w4,bg ='grey',font='size 12')
    label4=Label(p9,text='Localisation',bg='black',fg='white',font='size 15')
    q1 = IntVar()
    q2 = IntVar()
    q3 = IntVar()
    rad17 = Checkbutton(p10,text='En ville',activeforeground="gold",overrelief=SUNKEN,variable=q1,bg ='grey',font='size 12')
    rad18 = Checkbutton(p10,text='Campagne',activeforeground="gold",overrelief=SUNKEN,variable=q2,bg ='grey',font='size 12')
    rad19 = Checkbutton(p10,text='Intermédiaire',activeforeground="gold",overrelief=SUNKEN,variable=q3,bg ='grey',font='size 12')
    label5=Label(p11,text='Plage',bg='black',fg='white',font='size 15')
    o1 = IntVar()
    o2 = IntVar()
    o3 = IntVar()
    o4 = IntVar()
    rad21 = Checkbutton(p12,text='Avec',activeforeground="gold",overrelief=SUNKEN,variable=o1,bg ='grey',font='size 12')
    rad22 = Checkbutton(p12,text='Sans',activeforeground="gold",overrelief=SUNKEN,variable=o2,bg ='grey',font='size 12')
    label.grid(row=0)
    rad1.grid(column=0, row=1)
    rad2.grid(column=1, row=1)
    rad3.grid(column=2, row=1)
    rad4.grid(column=3, row=1)
    rad44.grid(column=4, row=1)
    label1.grid(row=0)
    rad5.grid(column=0, row=3)
    rad6.grid(column=1, row=3)
    rad7.grid(column=2, row=3)
    rad8.grid(column=3, row=3)
    label3.grid(row=0)
    rad13.grid(column=0, row=1)
    rad16.grid(column=3, row=1)
    label4.grid(row=0)
    rad17.grid(column=0, row=3)
    rad18.grid(column=1, row=3)
    rad19.grid(column=2, row=3)
    label5.grid(row=0)
    rad21.grid(column=0, row=5)
    rad22.grid(column=1, row=5)

    def bonjour():
        global P       
        P=[]
        L=[]
        Caire = int(s4.get())+ int(a2.get())+int(w4.get())+int(q3.get())+int(o2.get())
        Chichén = int(s3.get())+ int(a4.get())+int(w1.get())+int(q2.get())+int(o2.get())
        Rome = int(s1.get())+ int(a3.get())+int(w1.get())+int(q1.get())+int(o2.get())
        Agra = int(s2.get())+ int(a3.get())+int(w4.get())+int(q3.get())+int(o2.get())
        Rio = int(s5.get())+ int(a1.get())+int(w4.get())+int(q1.get())+int(o1.get())
        L.append(Caire)
        L.append(Chichén)
        L.append(Rome)
        L.append(Agra)
        L.append(Rio)
        K=[]
        K.append('Caire')
        K.append('Chichén-itzà')
        K.append('Rome')
        K.append('Agra')
        K.append('Rio')
        for i in range(5):
            if L[i] == max(L):
                P.append(K[i])
        if max(L)==0:
            bj.config(text="(Répondez pour voir votre / vos préférence(s) s'afficher ici)",bg ='black',font='size 13 bold italic',fg='white')
            bja.config(text='')
        elif len(P)==1:
            bj.config(text="Votre choix est",fg='white',font='size 13 bold italic')
            bja.config(text=P,fg='white',font='size 13 bold italic')
        else:
            R=''
            bj.config(text="Vos choix sont",fg='white',font='size 13 bold italic')
            for i in range (len(P)):
                R=R+P[i]
                if i!=(len(P)-1):
                    R=R+' et '
            bja.config(text=R,fg='white',font='size 13 bold italic')
    
    img =PhotoImage(file="tktt.png")
    """image=img"""
    btn = Button(master,command=bonjour,text="afficher" ,bd=7,overrelief=GROOVE) 
    btn.grid(column=4, row=10)
    bttn = Button(master,command=master.destroy,text='Annuler',bd=7,overrelief=GROOVE,bg='red',font='size 12 italic') 
    bttn.grid(column=4, row=0)
    bj=Label(p13, text="(Répondez pour voir votre / vos préférence(s) s'afficher ici)",bg ='black',font='size 13 bold italic',fg='white') 
    bj.grid(column=0, row=0)
    bja=Label(p13, text="",bg ='black') 
    bja.grid(column=1, row=0)
    
def retour():
    def recherche():
        m=c1.get()
        if m=="Agra":
            searchAgra()
        elif m=="Chichén Itzá":
            searchChichen()
        elif m=="Le Caire":
            searchCaire()
        elif m=="Rio de Janeiro":
            searchRio()
        elif m=="Rome":
            searchRome()
    for widget in fenetre.winfo_children():
        widget.destroy()
    p1=PanedWindow(fenetre)
    p1.configure(bg="black")
    p1.place(x=200,y=200)
    l1=Label(p1, text="Veuillez choisir une destination",fg="white",bg="black",font="-size 15")
    l1.grid(row=0,columnspan=2)
    ville=["Agra","Chichén Itzá","Le Caire","Rio de Janeiro","Rome"]
    c1=ttk.Combobox(p1, values=ville)
    c1.current(0)
    c1.grid(row=1)
    b1=Button(p1, text="Rechercher",command=recherche)
    b1.grid(row=2,column=0)
    b2=Button(p1, text="Besoin d'une idée",command=questionnaire)
    b2.grid(row=2,column=1)    

    
fenetre=Tk()
fenetre.geometry("1400x700+40+40")
fenetre.title(" Titre")
fenetre.configure(bg="yellow")
p1=PanedWindow(fenetre)
p1.configure(bg="black")
p1.place(x=200,y=200)
l1=Label(p1, text="Veuillez choisir une destination",fg="white",bg="black",font="-size 15")
l1.grid(row=0,columnspan=2)
ville=["Agra","Chichén Itzá","Le Caire","Rio de Janeiro","Rome"]
c1=ttk.Combobox(p1, values=ville)
c1.current(0)
c1.grid(row=1)
b1=Button(p1, text="Rechercher",command=recherche)
b1.grid(row=2,column=0)
b2=Button(p1, text="Besoin d'une idée",command=questionnaire)
b2.grid(row=2,column=1)

fenetre.mainloop()




