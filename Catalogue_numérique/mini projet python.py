##Voici le mini projet du groupe de Thégat Thya-Marie et El zenary Ramel


from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
p=0
r=0

def pa():
    prix=prix+3
    print(prix)

def fenetre (r):
    img =tk.PhotoImage(file="r")
    label=Label(p1,image=img,)
    label.grid(row=0,column=0)
def pri ():
    global prix
    pricelabel.config(text=prix)

def aide():
    global p
    if p<20:
        if (p%2)==0:
            ade.config(text= "Bienvenue sur Lemon TV \n Sélectionner vos épisodes\n pour en avoir un résumé et \n si il vous plait ajoutez le \n à votre panier en cliquant \n sur le sablier\n (Prix 3€ / épisode)",font = "Arial 9 italic")
            p=p+1
        else:
            ade.config(text='')
            p=p+1
    else:
        ade.config(text="Arrete de cliquer ça sert à rien")
        
def s(r):
    global prix

    if r==1:
        global prix
        imgg = PhotoImage(file="1.png")
        label=Label(p9,image=imgg)
        label.grid(row=0,column=0)
    
        l1.config(text= "Dans un pays où l'été peut durer plusieurs années et l'hiver toute une vie,\ndes forces sinistres et surnaturelles se pressent aux portes du Royaume des Sept \nCouronnes,pendant ce temps, complots et rivalités se jouent sur le continent pour \ns'emparer du Trône de Fer, le symbole du pouvoir absolu.")

        L= ['Saison 1', 'Saison 2','Saison 3']
        c1= ttk.Combobox(p11, values= L)
        c1.grid(row = 0, column = 1)

        def Got ():
            global prix
            def pa():
                global prix
                prix=prix+3
            r=c1.get()
            if r=='Saison 1':
                global r1
                global r2
                global r3
                global r4
                global r5
                global r6
                global r7
                global r8
                global r9
                global r10
                r1=0
                r2=0
                r3=0
                r4=0
                r5=0
                r6=0
                r7=0
                r8=0
                r9=0
                r10=0
                def R1 ():
                    global r1
                    if r1%2==0:
                        r1=r1+1
                        R.config(text="Au delà d'un gigantesque mur de protection \nde glace dans le nord de Westeros. Robert \nBaratheon, le roi, arrive avec son cortège \nau sud du mur de Winterfell pour demander de \nl'aide à son vieil ami Eddard Stark.")
                    else:
                        r1=r1+1
                        R.config(text="")
                def R2 ():
                    global r2
                    if r2%2==0:
                        r2=r2+1
                        R.config(text="Le roi Robert Baratheon et son entourage\n prennent la direction du Sud avec Eddard Stark\net ses filles Sansa et Arya. Sur la route, Arya\na des ennuis avec le prince Joffrey, ce qui laisse\nà Eddard une décision difficile à prendre.")
                    else:
                        r2=r2+1
                        R.config(text="")
                       
                def R3 ():
                    global r3
                    if r3%2==0:
                        r3=r3+1
                        R.config(text="Eddard Stark arrive à Port-Réal et ce\nqu'il découvre le laisse en état de choc.\nA Castle Black, Jon Snow débute sa formation\n pour devenir un homme de la Garde de Nuit.")
                    else:
                        r3=r3+1
                        R.config(text="")

                def R4 ():
                    global r4
                    if r4%2==0:
                        r4=r4+1
                        R.config(text="A Port-Réal, Eddard Stark commence son\nenquête pour savoir qui est impliqué dans la mort\nsubite de son prédécesseur. Un important tournoi est\norganisé en l'honneur de la nouvelle Main du Roi.\nAu Nord, Jon Snow se prend de sympathie pour Samwell\nTarly, une nouvelle recrue de la Garde de Nuit.")
                    else:
                        r4=r4+1
                        R.config(text="")
                def R5 ():
                    global r5
                    if r5%2==0:
                        r5=r5+1
                        R.config(text="A Port-Réal, les affaires politiques reprennent\nde plus belle. Sur la grande route qui menait à la\ncapitale des Sept Royaumes, le roi avait fait part\nà Eddard Stark de ses craintes sur l'avenir et sur\nles intentions des survivants de la dynastie des Targaryen.")
                    else:
                        r5=r5+1
                        R.config(text="")

                def R6 ():
                    global r6
                    if r6%2==0:
                        r6=r6+1
                        R.config(text="Après avoir rendu public son profond désaccord\navec le roi Robert Baratheon au sujet de l'organisation\nde l'assassinat de Daenerys Targaryen, Eddard Stark a été\nattaqué par Jaime Lannister. L'atmosphère à Port-Réal est\nplus que tendue et Eddard doit maintenant gérer \nde nouveaux problèmes.")
                    else:
                        r6=r6+1
                        R.config(text="")

                def R7 ():
                    global r7
                    if r7%2==0:
                        r7=r7+1
                        R.config(text="Eddard décide qu'il est temps d'annoncer\nl'identité du véritable père du prince Joffrey.\nSes révélations accusent directement Cersei d'avoir\nentretenu une relation incestueuse avec son frère jumeau.\nNed entend en informer le roi Robert mais, pris de pitié,\nil conseille à Cersei et à son rejeton de prendre la\nfuite sans tarder.")
                    else:
                        r7=r7+1
                        R.config(text="")

                def R8 ():
                    global r8
                    if r8%2==0:
                        r8=r8+1
                        R.config(text="Eddard se retrouve dans une geôle et accusé\nde trahison envers Joffrey, intronisé roi. Le clan\nLannister informe Robb Stark que son père est prisonnier\net qu'il doit se rendre à Port-Réal pour faire allégeance\nà la nouvelle couronne.")
                    else:
                        r8=r8+1
                        R.config(text="")

                def R9 ():
                    global r9
                    if r9%2==0:
                        r9=r9+1
                        R.config(text="Eddard Stark est inquiet pour le sort de sa\nfille. Il doit prendre une décision difficile.\nDe son côté, Catelyn conclut un arrangement avec\nlord Walder Frey, à ses risques et périls. Tyrion\nLannister, qui se réconforte dans les bras d'une\nmaîtresse, est forcé par son père Tywin à aller\ncombattre la maison Stark.")           
                    else:
                        r9=r9+1
                        R.config(text="")


                def R10 ():
                    global r10
                    if r10%2==0:
                        r10=r10+1
                        R.config(text="La nouvelle de la mort d'Eddard se propage\nà travers les Sept Royaumes. Catelyn interroge Jaime\nLannister à propos de la chute de son fils Bran alors\nque les seigneurs du Nord choisissent Robb comme nouveau roi.")
                    else:
                        r10=r10+1
                        R.config(text="")

                global prix
                maste1=Tk()
                maste1.title('Got S1')
        
                m1=PanedWindow(maste1,bg='black')
                m1.grid(row=0,column=0)

                m2=PanedWindow(maste1)
                m2.grid(row=1,column=0)
        
                rem1 = Button(m1, text='Episode 1',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R1,overrelief=GROOVE)
                rem1.grid(row=0,column=0)

                rem2 = Button(m1, text='Episode 2',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R2,overrelief=GROOVE)
                rem2.grid(row=1,column=0)

                rem3 = Button(m1, text='Episode 3',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R3,overrelief=GROOVE)
                rem3.grid(row=2,column=0)

                rem4 = Button(m1, text='Episode 4',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R4,overrelief=GROOVE)
                rem4.grid(row=3,column=0)
        
                rem5 = Button(m1, text='Episode 5',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R5,overrelief=GROOVE)
                rem5.grid(row=4,column=0)

                rem6 = Button(m1, text='Episode 6',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R6,overrelief=GROOVE)
                rem6.grid(row=5,column=0)

                rem7 = Button(m1, text='Episode 7',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R7,overrelief=GROOVE)
                rem7.grid(row=6,column=0)

                rem8 = Button(m1, text='Episode 8',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R8,overrelief=GROOVE)
                rem8.grid(row=7,column=0)

                rem9 = Button(m1, text='Episode 9',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R9,overrelief=GROOVE)
                rem9.grid(row=8,column=0)

                rem10 = Button(m1, text='Episode 10',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R10,overrelief=GROOVE)
                rem10.grid(row=9,column=0)

                em1 = Label(m1, text='L’hiver vient', font ='Arial 11 bold italic',bg='white')
                em1.grid(row=0,column=1)

                em2 = Label(m1, text='La route royale',font ='Arial 11 bold italic',bg='white')
                em2.grid(row=1,column=1)

                em3 = Label(m1, text='Lord snow',font ='Arial 11 bold italic',bg='white')
                em3.grid(row=2,column=1)

                em4 = Label(m1, text='Infirmes, bâtards et choses brisées',font ='Arial 11 bold italic',bg='white')
                em4.grid(row=3,column=1)
        
                em5 = Label(m1, text='Le loup et le lion',font ='Arial 11 bold italic',bg='white')
                em5.grid(row=4,column=1)

                em6 = Label(m1, text='Une couronne dorée',font ='Arial 11 bold italic',bg='white')
                em6.grid(row=5,column=1)

                em7 = Label(m1, text='Gagner ou mourir',font ='Arial 11 bold italic',bg='white')
                em7.grid(row=6,column=1)

                em8 = Label(m1, text="Frapper d'estoc",font ='Arial 11 bold italic',bg='white')
                em8.grid(row=7,column=1)

                em9 = Label(m1, text='Baelor',font ='Arial 11 bold italic',bg='white')
                em9.grid(row=8,column=1)

                em10 = Label(m1, text='De feu et de sang',font ='Arial 11 bold italic',bg='white')
                em10.grid(row=9,column=1)

                mp1 = Button(m1, bitmap='hourglass',command=pa)
                mp1.grid(row=0,column=2)

                mp2 = Button(m1, bitmap='hourglass',command=pa)
                mp2.grid(row=1,column=2)

                mp3 = Button(m1, bitmap='hourglass',command=pa)
                mp3.grid(row=2,column=2)

                mp4 = Button(m1,bitmap='hourglass',command=pa)
                mp4.grid(row=3,column=2)
                
                mp5 = Button(m1, bitmap='hourglass',command=pa)
                mp5.grid(row=4,column=2)

                mp6 = Button(m1, bitmap='hourglass',command=pa)
                mp6.grid(row=5,column=2)

                mp7 = Button(m1, bitmap='hourglass',command=pa)
                mp7.grid(row=6,column=2)

                mp8 = Button(m1, bitmap='hourglass',command=pa)
                mp8.grid(row=7,column=2)

                mp9 = Button(m1, bitmap='hourglass',command=pa)
                mp9.grid(row=8,column=2)

                mp10 = Button(m1, bitmap='hourglass',command=pa)
                mp10.grid(row=9,column=2)

                R = Label(m2,text='')
                R.grid(row=0,column=0)


            elif r=='Saison 2':
                global f1
                global f2
                global f3
                global f4
                global f5
                global f6
                global f7
                global f8
                global f9
                global f10
                f1=0
                f2=0
                f3=0
                f4=0
                f5=0
                f6=0
                f7=0
                f8=0
                f9=0
                f10=0
                def R1 ():
                    global f1
                    if f1%2==0:
                        f1=f1+1
                        R.config(text="L'exécution d'Eddard Stark a plongé Westeros\ndans la guerre. Dans le Nord, pendant que Jon Snow\net la Garde de Nuit poursuivent leur expédition\nau-delà du Mur, les Stark, menés par Robb, qui veut\nvenger la mort de son père, poursuivent leur\noffensive contre les Lannister. Ils veulent\nrenverser Joffrey, discrètement surveillé par\nTyrion, la nouvelle Main du Roi.")
                    else:
                        f1=f1+1
                        R.config(text="")
                def R2 ():
                    global f2
                    if f2%2==0:
                        f2=f2+1
                        R.config(text="Pour contrer le clan Lannister, Stannis\nBaratheon pousse Davos à trouver de nouveaux\nalliés. Sur la route du Nord, Arya Stark, qui\nfuit Port-Réal depuis l'exécution de son père,\nse confie à Gendry.")
                    else:
                        f2=f2+1
                        R.config(text="")
                       
                def R3 ():
                    global f3
                    if f3%2==0:
                        f3=f3+1
                        R.config(text="Dans le conflit qui oppose les Stark aux\nLannister, Catelyn tente de nouer des alliances\net traite ainsi avec Renly Baratheon dans\nl'espoir de trouver un terrain d'entente.\nA Port-Réal, là où les complots rythment la vie\nde la cour, Tyrion Lannister s'engage dans un\nplan complexe pour mettre à jour un de ses ennemis.")
                    else:
                        f3=f3+1
                        R.config(text="")

                def R4 ():
                    global f4
                    if f4%2==0:
                        f4=f4+1
                        R.config(text="A Port-Réal, Tyrion Lannister connaît bien\nles codes de la Cour royale et use de toute son\nintelligence pour étendre son influence. Modéré\net stratège, il veut limiter les accès de cruauté\ndu roi Joffrey, parfois imprévisible.")
                    else:
                        f4=f4+1
                        R.config(text="")
                def R5 ():
                    global f5
                    if f5%2==0:
                        f5=f5+1
                        R.config(text="Dans la perspective de nouer des alliances\nentre les différentes maisons du royaume, Catelyn\nStark doit prendre une décision urgente et même\ns'enfuir aux côtés d'un allié inattendu. Dans le\nchaos politique qui règne, Petyr Baelish tente de\ntirer profit de la situation et des opportunités\nqui se présentent.")
                    else:
                        f5=f5+1
                        R.config(text="")

                def R6 ():
                    global f6
                    if f6%2==0:
                        f6=f6+1
                        R.config(text="Theon Greyjoy accomplit une prouesse qui\nlui vaut le respect des siens. Pendant ce temps,\nsentant que la situation se dégrade à Port-Réal,\nles Lannister décident d'éloigner Myrcella de\nla ville. Elle la quitte juste à temps.")
                    else:
                        f6=f6+1
                        R.config(text="")

                def R7 ():
                    global f7
                    if f7%2==0:
                        f7=f7+1
                        R.config(text="Installée chez Xaro, important dignitaire\nde Qarth, Daenerys reçoit l'autorisation de se\nrendre dans l'hôtel des Nonmourants. Pendant ce\ntemps, sur Westeros, Jaime Lannister rencontre un\nparent éloigné pendant que sa soeur, la reine\nCersei, prodigue quelques conseils à la jeune\nSansa Stark.")
                    else:
                        f7=f7+1
                        R.config(text="")

                def R8 ():
                    global f8
                    if f8%2==0:
                        f8=f8+1
                        R.config(text="Après son coup d'éclat, Theon doit maintenant\ntenir sa position. C'est alors qu'un visiteur\nse présente à lui. A Port-Réal, Tyrion Lannister\net Varys, l'ennuque du palais, finissent par\npasser un accord.")
                    else:
                        f8=f8+1
                        R.config(text="")

                def R9 ():
                    global f9
                    if f9%2==0:
                        f9=f9+1
                        R.config(text="Stannis Baratheon et ses troupes arrivent\npar la mer au large de Port-Réal. L'enjeu est\npour lui de s'emparer du Trône de Fer. Dans la\ncitadelle, les Lannister doivent se battre\npour leur vie.")
                    else:
                        f9=f9+1
                        R.config(text="")
                def R10 ():
                    global f10
                    if f10%2==0:
                        f10=f10+1
                        R.config(text="La bataille de Port-Réal est terminée,\net c'est la victoire des Lannister. Arya Stark\nretrouve le mystérieux Jaqen H'ghar et Daenerys\ncherche ses dragons dans la maison de l'Immortel.")

                    else:
                        f10=f10+1
                        R.config(text="")
                global prix
                maste2=Tk()
                maste2.title('Got S2')
        
                m1=PanedWindow(maste2,bg='black')
                m1.grid(row=0,column=0)

                m2=PanedWindow(maste2)
                m2.grid(row=1,column=0)
        
                rem1 = Button(m1, text='Episode 1',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R1,overrelief=GROOVE)
                rem1.grid(row=0,column=0)

                rem2 = Button(m1, text='Episode 2',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R2,overrelief=GROOVE)
                rem2.grid(row=1,column=0)

                rem3 = Button(m1, text='Episode 3',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R3,overrelief=GROOVE)
                rem3.grid(row=2,column=0)

                rem4 = Button(m1, text='Episode 4',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R4,overrelief=GROOVE)
                rem4.grid(row=3,column=0)
        
                rem5 = Button(m1, text='Episode 5',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R5,overrelief=GROOVE)
                rem5.grid(row=4,column=0)

                rem6 = Button(m1, text='Episode 6',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R6,overrelief=GROOVE)
                rem6.grid(row=5,column=0)

                rem7 = Button(m1, text='Episode 7',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R7,overrelief=GROOVE)
                rem7.grid(row=6,column=0)

                rem8 = Button(m1, text='Episode 8',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R8,overrelief=GROOVE)
                rem8.grid(row=7,column=0)

                rem9 = Button(m1, text='Episode 9',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R9,overrelief=GROOVE)
                rem9.grid(row=8,column=0)

                rem10 = Button(m1, text='Episode 10',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R10,overrelief=GROOVE)
                rem10.grid(row=9,column=0)

                em1 = Label(m1, text='Le nord se souvient', font ='Arial 11 bold italic',bg='white')
                em1.grid(row=0,column=1)

                em2 = Label(m1, text='Les contrées nocturnes',font ='Arial 11 bold italic',bg='white')
                em2.grid(row=1,column=1)

                em3 = Label(m1, text='Ce qui est mort ne saurait mourir',font ='Arial 11 bold italic',bg='white')
                em3.grid(row=2,column=1)

                em4 = Label(m1, text='Le jardin des os',font ='Arial 11 bold italic',bg='white')
                em4.grid(row=3,column=1)
        
                em5 = Label(m1, text="Le fantôme d'harrenhal",font ='Arial 11 bold italic',bg='white')
                em5.grid(row=4,column=1)

                em6 = Label(m1, text='Les anciens et les nouveaux dieux',font ='Arial 11 bold italic',bg='white')
                em6.grid(row=5,column=1)

                em7 = Label(m1, text='Un homme sans honneur',font ='Arial 11 bold italic',bg='white')
                em7.grid(row=6,column=1)

                em8 = Label(m1, text="Le prince de Winterfell",font ='Arial 11 bold italic',bg='white')
                em8.grid(row=7,column=1)

                em9 = Label(m1, text='La Néra',font ='Arial 11 bold italic',bg='white')
                em9.grid(row=8,column=1)

                em10 = Label(m1, text='Valar Morghulis',font ='Arial 11 bold italic',bg='white')
                em10.grid(row=9,column=1)

                mp1 = Button(m1, bitmap='hourglass',command=pa)
                mp1.grid(row=0,column=2)

                mp2 = Button(m1, bitmap='hourglass',command=pa)
                mp2.grid(row=1,column=2)

                mp3 = Button(m1, bitmap='hourglass',command=pa)
                mp3.grid(row=2,column=2)

                mp4 = Button(m1,bitmap='hourglass',command=pa)
                mp4.grid(row=3,column=2)
                
                mp5 = Button(m1, bitmap='hourglass',command=pa)
                mp5.grid(row=4,column=2)

                mp6 = Button(m1, bitmap='hourglass',command=pa)
                mp6.grid(row=5,column=2)

                mp7 = Button(m1, bitmap='hourglass',command=pa)
                mp7.grid(row=6,column=2)

                mp8 = Button(m1, bitmap='hourglass',command=pa)
                mp8.grid(row=7,column=2)

                mp9 = Button(m1, bitmap='hourglass',command=pa)
                mp9.grid(row=8,column=2)

                mp10 = Button(m1, bitmap='hourglass',command=pa)
                mp10.grid(row=9,column=2)

                R = Label(m2,text='')
                R.grid(row=1,column=0)
 
                mainloop()
                
            elif r=='Saison 3':
                global prix
                maste3=Tk()
                maste3.title('Got S3')
                def R1 ():
                    R.config(text="Jon Snow est amené devant Mance Rayder,\nle Roi d'au-delà du Mur, alors que les chevaliers\nde la Garde de Nuit entament leur retraite vers\nle Sud. A Port-Réal, Tyrion exige sa récompense,\ntandis que Petyr Baelish offre à Sansa Stark une\nporte de sortie.")
                def R2 ():
                    R.config(text="A Port-Réal, alors que Sansa est\ninterrogée par lady Olenna, qui cherche\nà en savoir plus sur le roi Joffrey, Shae\ndemande un service à Tyrion. Au-delà du\nMur, Jon Snow, toujours protégé par Ygritte,\nrencontre Orell, un warg capable de voir à\ntravers les yeux des animaux.")
                def R3 ():
                    R.config(text="En l'absence de Littlefinger,\nTyrion obtient de nouvelles\nresponsabilités à Port-Réal tandis\nqu'à Astapor, Daenerys réussit à\nconvaincre ses hôtes de lui vendre\ndes Immaculés, des soldats sans peur.")
                def R4 ():
                    R.config(text="Les survivants de la Garde de\nNuit arrivent chez Craster, un seigneur\nodieux qui profite de ses nombreuses\népouses : en échange d'un peu de\nrepos, Craster oblige les hommes à\ns'occuper des cochons.")
                def R5 ():
                    R.config(text="Daenerys déploie son armée et ses dragons\npour libérer les esclaves d'Astapor. Quant à\nSandor Clegane, il doit répondre de ses actes\npassés devant la Confrérie des sans-bannières.\nCependant, au nord du Mur, Jon Snow est contraint\nde faire ses preuves.")
                def R6 ():
                    R.config(text="Jon Snow, Ygritte et les Sauvageons s'attaquent\nà une escalade périlleuse. Pour sa part, Tywin élabore\ndes mariages stratégiques pour les Lannister.\nRobb est à la recherche d'un compromis pour\nretrouver la confiance de la maison Frey...")
                def R7 ():
                    R.config(text="Pour Jon Snow, l'heure est venue de régler ses\ncomptes avec Orell, l'un des membres des Wildings.\nDe son côté, Daenerys poursuit sa route vers la\ncité de Yunkaï, plus déterminée que jamais à\nlibérer des esclaves.")
                def R8 ():
                    R.config(text="Daenerys fait la connaissance d'un mercenaire.\nElle obtient l'appui d'une armée dans sa quête de\npouvoir. En parallèle, à Port-Réal, Sansa et Tyrion\nse marient sous le regard amusé de Joffrey.")
                def R9 ():
                    R.config(text="Robb se présente devant Walder Frey tandis\nqu'Edmure fait la connaissance de sa future épouse.\nDe son côté, Jon est confronté à la pire épreuve\nde sa jeune existence et Bran se découvre un nouveau don.")        
                def R10 ():
                    R.config(text="C'est le chaos au sein du clan Lannister...\nJoffrey défie Tywin. A Peyredragon, le salut\nviendra peut-être d'alliés inattendus. Bran est\nhanté par une vision venue d'outre tombe. Daenerys\nse retrouve face à un dilemme : est-elle une\nguerrière ou une libératrice ?")


        
                m1=PanedWindow(maste3,bg='black')
                m1.grid(row=0,column=0)

                m2=PanedWindow(maste3)
                m2.grid(row=1,column=0)
        
                rem1 = Button(m1, text='Episode 1',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R1,overrelief=GROOVE)
                rem1.grid(row=0,column=0)

                rem2 = Button(m1, text='Episode 2',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R2,overrelief=GROOVE)
                rem2.grid(row=1,column=0)

                rem3 = Button(m1, text='Episode 3',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R3,overrelief=GROOVE)
                rem3.grid(row=2,column=0)

                rem4 = Button(m1, text='Episode 4',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R4,overrelief=GROOVE)
                rem4.grid(row=3,column=0)
        
                rem5 = Button(m1, text='Episode 5',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R5,overrelief=GROOVE)
                rem5.grid(row=4,column=0)

                rem6 = Button(m1, text='Episode 6',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R6,overrelief=GROOVE)
                rem6.grid(row=5,column=0)

                rem7 = Button(m1, text='Episode 7',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R7,overrelief=GROOVE)
                rem7.grid(row=6,column=0)

                rem8 = Button(m1, text='Episode 8',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R8,overrelief=GROOVE)
                rem8.grid(row=7,column=0)

                rem9 = Button(m1, text='Episode 9',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R9,overrelief=GROOVE)
                rem9.grid(row=8,column=0)

                rem10 = Button(m1, text='Episode 10',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R10,overrelief=GROOVE)
                rem10.grid(row=9,column=0)
 
                em1 = Label(m1, text='Valar Dohaeris', font ='Arial 11 bold italic',bg='white')
                em1.grid(row=0,column=1)

                em2 = Label(m1, text='Noires ailes, noires nouvelles',font ='Arial 11 bold italic',bg='white')
                em2.grid(row=1,column=1)

                em3 = Label(m1, text='Les immaculés',font ='Arial 11 bold italic',bg='white')
                em3.grid(row=2,column=1)

                em4 = Label(m1, text='Voici que son tour de garde est fini',font ='Arial 11 bold italic',bg='white')
                em4.grid(row=3,column=1)
        
                em5 = Label(m1, text="Baisée par le feu",font ='Arial 11 bold italic',bg='white')
                em5.grid(row=4,column=1)

                em6 = Label(m1, text="L'ascension",font ='Arial 11 bold italic',bg='white')
                em6.grid(row=5,column=1)

                em7 = Label(m1, text="L’ours et la belle",font ='Arial 11 bold italic',bg='white')
                em7.grid(row=6,column=1)

                em8 = Label(m1, text="Les puînés",font ='Arial 11 bold italic',bg='white')
                em8.grid(row=7,column=1)

                em9 = Label(m1, text='Les pluies de castamere',font ='Arial 11 bold italic',bg='white')
                em9.grid(row=8,column=1)

                em10 = Label(m1, text='Mhysa',font ='Arial 11 bold italic',bg='white')
                em10.grid(row=9,column=1)

                mp1 = Button(m1, bitmap='hourglass',command=pa)
                mp1.grid(row=0,column=2)

                mp2 = Button(m1, bitmap='hourglass',command=pa)
                mp2.grid(row=1,column=2)

                mp3 = Button(m1, bitmap='hourglass',command=pa)
                mp3.grid(row=2,column=2)

                mp4 = Button(m1,bitmap='hourglass',command=pa)
                mp4.grid(row=3,column=2)
                
                mp5 = Button(m1, bitmap='hourglass',command=pa)
                mp5.grid(row=4,column=2)

                mp6 = Button(m1, bitmap='hourglass',command=pa)
                mp6.grid(row=5,column=2)

                mp7 = Button(m1, bitmap='hourglass',command=pa)
                mp7.grid(row=6,column=2)

                mp8 = Button(m1, bitmap='hourglass',command=pa)
                mp8.grid(row=7,column=2)

                mp9 = Button(m1, bitmap='hourglass',command=pa)
                mp9.grid(row=8,column=2)

                mp10 = Button(m1, bitmap='hourglass',command=pa)
                mp10.grid(row=9,column=2)

                R = Label(m2,text='')
                R.grid(row=1,column=0)
 
                mainloop()

        l2= Label(p11, text= "Sélectionnez", font="Arial 9")
        l2.grid(row=0, column=0)

        b1= Button(p11, text= "Valider",command=Got)
        b1.grid(row=0, column= 2)

        mainloop()

    elif r==2:
        global prix
        def pa():
                global prix
                prix=prix+3
        imgg = PhotoImage(file="2.png")
        label=Label(p9,image=imgg)
        label.grid(row=0,column=0)
    
        l1.config(text= "Chaque épisode de cette anthologie montre\n la dépendance des hommes vis-à-vis de tout ce qui a un écran....")
        L= ['Saison 1', 'Saison 2','Saison 3', 'Saison 4']
        c1= ttk.Combobox(p11, values= L)
        c1.grid(row = 0, column = 1)

        def BM ():
            global prix
            def pa():
                global prix
                prix=prix+3
            r=c1.get()
            if r=='Saison 1':
                global prix
                def R1 ():
                    R.config(text="Le Premier Ministre Michael Callow fait\nface à un terrible dilemme après le kidnapping\nde la bien-aimée Princesse Susannah.")
                def R2 ():
                    R.config(text="Rejetée par le jury lors d'une émission\nde chant, une femme doit réaliser des tâches\ndégradantes ou retourner à sa condition d'esclave.")
                def R3 ():
                    R.config(text="Dans un futur proche, tout le monde\npourra être équipé d'un implant enregistrant\ntout ce qui sera fait, vu ou entendu...")
                ma1=Tk()
                ma1.title('BM S1')
        
                m1=PanedWindow(ma1)
                m1.grid(row=0,column=0)

                m2=PanedWindow(ma1)
                m2.grid(row=1,column=0)
        
                rem1 = Button(m1, text='Episode 1',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R1,overrelief=GROOVE)
                rem1.grid(row=0,column=0)

                rem2 = Button(m1, text='Episode 2',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R2,overrelief=GROOVE)
                rem2.grid(row=1,column=0)

                rem3 = Button(m1, text='Episode 3',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R3,overrelief=GROOVE)
                rem3.grid(row=2,column=0)

                em1 = Label(m1, text="L’hymne national", font ='Arial 11 bold italic',bg='white')
                em1.grid(row=0,column=1)

                em2 = Label(m1, text='15 millions de mérites',font ='Arial 11 bold italic',bg='white')
                em2.grid(row=1,column=1)

                em3 = Label(m1, text='Retour sur images',font ='Arial 11 bold italic',bg='white')
                em3.grid(row=2,column=1)

                mp1 = Button(m1, bitmap='hourglass',command=pa)
                mp1.grid(row=0,column=2)

                mp2 = Button(m1, bitmap='hourglass',command=pa)
                mp2.grid(row=1,column=2)

                mp3 = Button(m1, bitmap='hourglass',command=pa)
                mp3.grid(row=2,column=2)

                R = Label(m2,text='')
                R.grid(row=1,column=0)

                mainloop()
        
            elif r=='Saison 2':
                global prix
                def R1 ():
                    R.config(text="Après avoir entendu parler\nd'un nouveau service permettant de\ngarder contact avec les morts, une\njeune femme endeuillée renoue avec\nson petit ami.")
                def R2 ():
                    R.config(text="Victoria se réveille un matin\nen n'ayant plus aucun souvenir de sa\nvie, et tous ceux qu'elle rencontre\nrefusent de communiquer avec elle.")
                def R3 ():
                    R.config(text="Un comédien raté prêtant sa\nvoix à un célèbre ourson de\ntélévision se retrouve mêlé à des\naffaires politiques quand ses\nproducteurs décident de le présenter\naux élections.")
                def R4 ():   
                    R.config(text="Deux hommes isolés dans un\ndésert glacé à Noël se racontent\ndes histoires où la technologie\npart en vrille et joue un rôle\ncalamiteux.")          
                def pa():
                    global prix
                    prix=prix+3

                ma2=Tk()
                ma2.title('BM S2')
        
                m1=PanedWindow(ma2)
                m1.grid(row=0,column=0)

                m2=PanedWindow(ma2)
                m2.grid(row=1,column=0)
        
                rem1 = Button(m1, text='Episode 1',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R1,overrelief=GROOVE)
                rem1.grid(row=0,column=0)

                rem2 = Button(m1, text='Episode 2',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R2,overrelief=GROOVE)
                rem2.grid(row=1,column=0)

                rem3 = Button(m1, text='Episode 3',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R3,overrelief=GROOVE)
                rem3.grid(row=2,column=0)

                rem4 = Button(m1, text='Episode 4',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R4,overrelief=GROOVE)
                rem4.grid(row=3,column=0)
        
                em1 = Label(m1, text='Bientôt de retour', font ='Arial 11 bold italic',bg='white')
                em1.grid(row=0,column=1)

                em2 = Label(m1, text='La chasse',font ='Arial 11 bold italic',bg='white')
                em2.grid(row=1,column=1)

                em3 = Label(m1, text='Le show de Waldo',font ='Arial 11 bold italic',bg='white')
                em3.grid(row=2,column=1)

                em4 = Label(m1, text='Blanc comme neige',font ='Arial 11 bold italic',bg='white')
                em4.grid(row=3,column=1)

                mp1 = Button(m1, bitmap='hourglass',command=pa)
                mp1.grid(row=0,column=2)

                mp2 = Button(m1, bitmap='hourglass',command=pa)
                mp2.grid(row=1,column=2)

                mp3 = Button(m1, bitmap='hourglass',command=pa)
                mp3.grid(row=2,column=2)

                mp4 = Button(m1,bitmap='hourglass',command=pa)
                mp4.grid(row=3,column=2)

                R = Label(m2,text='')
                R.grid(row=1,column=0)
                
                mainloop()
                
            elif r=='Saison 3':
                global prix
                def R1 ():
                    R.config(text="Pour une femme obsédée par\nsa notoriété sur les médias sociaux,\nse faire inviter à un mariage huppé\nreprésente une aubaine inespérée.\nMais c'était compter sans le voyage.")
                def R2 ():
                    R.config(text="Un voyageur américain fauché\ns'engage à tester un nouveau système\nde jeu révolutionnaire, avant de\ndécouvrir que les sensations sont\n un peu trop réelles.")
                def R3 ():
                    R.config(text="Quand un virus infecte son\nordinateur, un adolescent fait face\nà un choix de taille : exécuter les\nordres qu'il reçoit, ou risquer de\nvoir exposer ses secrets intimes.")
                def R4 ():
                    R.config(text="En 1987, dans une ville de\nbord de mer, une jeune femme\ntimide et une fêtarde extravertie\nnouent un lien puissant qui semble\ndéfier les lois de l'espace et du temps.")
                def R5 ():
                    R.config(text="Après sa première bataille\ncontre un ennemi insaisissable, un\nsoldat commence à éprouver des\nsensations inhabituelles et à\nrencontrer d'étranges problèmes\n techniques.")
                def R6 ():
                    R.config(text="La mort d'une journaliste\nprovocatrice haïe sur les réseaux\nsociaux conduit une enquêtrice\naguerrie et sa stagiaire férue de\ntechnologie à une découverte glaçante.")        
                def pa():
                    global prix
                    prix=prix+3

                ma3=Tk()
                ma3.title('BM S3')
        
                m1=PanedWindow(ma3)
                m1.grid(row=0,column=0)

                m2=PanedWindow(ma3)
                m2.grid(row=1,column=0)
        
                rem1 = Button(m1, text='Episode 1',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R1,overrelief=GROOVE)
                rem1.grid(row=0,column=0)

                rem2 = Button(m1, text='Episode 2',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R2,overrelief=GROOVE)
                rem2.grid(row=1,column=0)

                rem3 = Button(m1, text='Episode 3',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R3,overrelief=GROOVE)
                rem3.grid(row=2,column=0)

                rem4 = Button(m1, text='Episode 4',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R4,overrelief=GROOVE)
                rem4.grid(row=3,column=0)
        
                rem5 = Button(m1, text='Episode 5',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R5,overrelief=GROOVE)
                rem5.grid(row=4,column=0)

                rem6 = Button(m1, text='Episode 6',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R6,overrelief=GROOVE)
                rem6.grid(row=5,column=0)

                em1 = Label(m1, text='Chute libre', font ='Arial 11 bold italic',bg='white')
                em1.grid(row=0,column=1)

                em2 = Label(m1, text='Phase d’essai',font ='Arial 11 bold italic',bg='white')
                em2.grid(row=1,column=1)

                em3 = Label(m1, text='Tais-toi et danse',font ='Arial 11 bold italic',bg='white')
                em3.grid(row=2,column=1)

                em4 = Label(m1, text='San Junipero',font ='Arial 11 bold italic',bg='white')
                em4.grid(row=3,column=1)
        
                em5 = Label(m1, text="Tuer sans état d’âme",font ='Arial 11 bold italic',bg='white')
                em5.grid(row=4,column=1)

                em6 = Label(m1, text='Haine virtuelle',font ='Arial 11 bold italic',bg='white')
                em6.grid(row=5,column=1)

                mp1 = Button(m1, bitmap='hourglass',command=pa)
                mp1.grid(row=0,column=2)

                mp2 = Button(m1, bitmap='hourglass',command=pa)
                mp2.grid(row=1,column=2)

                mp3 = Button(m1, bitmap='hourglass',command=pa)
                mp3.grid(row=2,column=2)

                mp4 = Button(m1,bitmap='hourglass',command=pa)
                mp4.grid(row=3,column=2)
                
                mp5 = Button(m1, bitmap='hourglass',command=pa)
                mp5.grid(row=4,column=2)

                mp6 = Button(m1, bitmap='hourglass',command=pa)
                mp6.grid(row=5,column=2)

                R = Label(m2,text='')
                R.grid(row=1,column=0)
 
                mainloop()

            elif r=='Saison 4':
                global prix
                def R1 ():
                    R.config(text="Le capitaine Robert Daly\ndirige l'équipage de son vaisseau\nspatial d'une poigne ferme et\njuste... Mais une nouvelle recrue\narrive, et les faux-semblants volent\nen éclat.")
                def R2 ():
                    R.config(text="Inquiète pour la sécurité\nde sa fillette, Marie, mère\ncélibataire, équipe celle-ci\nd'un implant de surveillance de\npointe qui permet de la localiser.\nEt pas seulement.")
                def R3 ():
                    R.config(text="Mia, une architecte,\npourra-t-elle taire son terrible\nsecret quand Shazia, enquêtrice\nd'assurance, sonne à sa porte,\nglanantles récents souvenirs d'un\naccident voisin ?")
                def R4 ():
                    R.config(text="Selon ce système de\nrencontres, toute relation a une\ndate de fabrication et d'expiration.\nMais Frank et Amy remettent vite en\nquestion cette logique stérile")
                def R5 ():
                    R.config(text="En explorant un entrepôt\nabandonné, trois pillards en\nquête de ressources déclenchent\nun monstre impitoyable qui s’élance\nà leur poursuite dans un désert\ninhospitalier.")
                def R6 ():
                    R.config(text="Sur un tronçon d'autoroute\nvétuste, une touriste tombe sur un\nmusée vantant des artefacts criminels\nrares. Mais le clou de l'exposition\nlui réserve une surprise de choc.")
                def pa():
                    global prix
                    prix=prix+3

                ma4=Tk()
                ma4.title('BM S4')
        
                m1=PanedWindow(ma4)
                m1.grid(row=0,column=0)

                m2=PanedWindow(ma4)
                m2.grid(row=1,column=0)
     
                rem1 = Button(m1, text='Episode 1',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R1,overrelief=GROOVE)
                rem1.grid(row=0,column=0)

                rem2 = Button(m1, text='Episode 2',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R2,overrelief=GROOVE)
                rem2.grid(row=1,column=0)

                rem3 = Button(m1, text='Episode 3',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R3,overrelief=GROOVE)
                rem3.grid(row=2,column=0)

                rem4 = Button(m1, text='Episode 4',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R4,overrelief=GROOVE)
                rem4.grid(row=3,column=0)
    
                rem5 = Button(m1, text='Episode 5',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R5,overrelief=GROOVE)
                rem5.grid(row=4,column=0)

                rem6 = Button(m1, text='Episode 6',bd=8,activebackground='blue',activeforeground="red",bg='white',command=R6,overrelief=GROOVE)
                rem6.grid(row=5,column=0)

                em1 = Label(m1, text='Uss callister', font ='Arial 11 bold italic',bg='white')
                em1.grid(row=0,column=1)

                em2 = Label(m1, text='Archange',font ='Arial 11 bold italic',bg='white')
                em2.grid(row=1,column=1)

                em3 = Label(m1, text='Crocodile',font ='Arial 11 bold italic',bg='white')
                em3.grid(row=2,column=1)

                em4 = Label(m1, text='Pendez le dj',font ='Arial 11 bold italic',bg='white')
                em4.grid(row=3,column=1)
        
                em5 = Label(m1, text="Tête de métal",font ='Arial 11 bold italic',bg='white')
                em5.grid(row=4,column=1)

                em6 = Label(m1, text="Black museum",font ='Arial 11 bold italic',bg='white')
                em6.grid(row=5,column=1)

                mp1 = Button(m1, bitmap='hourglass',command=pa)
                mp1.grid(row=0,column=2)

                mp2 = Button(m1, bitmap='hourglass',command=pa)
                mp2.grid(row=1,column=2)

                mp3 = Button(m1, bitmap='hourglass',command=pa)
                mp3.grid(row=2,column=2)

                mp4 = Button(m1,bitmap='hourglass',command=pa)
                mp4.grid(row=3,column=2)
                
                mp5 = Button(m1, bitmap='hourglass',command=pa)
                mp5.grid(row=4,column=2)

                mp6 = Button(m1, bitmap='hourglass',command=pa)
                mp6.grid(row=5,column=2)

                R = Label(m2,text='')
                R.grid(row=1,column=0)

                mainloop()

        l2= Label(p11, text= "Sélectionnez", font="Arial 9")
        l2.grid(row=0, column=0)

        b1= Button(p11, text= "Valider",command=BM)
        b1.grid(row=0, column= 2)

        mainloop()
        
    elif r==3:
        global prix
        def pa():
            global prix
            prix=prix+3

        imgg = PhotoImage(file="3.png")
        label=Label(p9,image=imgg)
        label.grid(row=0,column=0)
    
        l1.config(text= " Dans un monde ravagé depuis plus d’un siècle par des titans mangeurs d’homme,\nles rares survivants de l’humanité n’ont d’autre choix que de se barricader dans une \ncité-forteresse. Le jeune Eren, témoin de la mort de sa mère dévorée par un titan, \nn’a qu’un rêve : entrer dans le corps d’élite chargé de découvrir l’origine des \ntitans et de les annihiler jusqu’au dernier.")

        L= ['Saison 1']
        c1= ttk.Combobox(p11, values= L)
        c1.grid(row = 0, column = 1)

        def snk ():
            global prix
            def pa():
                    global prix
                    prix=prix+3

            r=c1.get()
            if r=='Saison 1':
                global prix
                def R1 ():
                    R.config(text="Réfugiés dans une ville fortifiée,\nles survivants de l'humanité tentent\nd'échapper aux titans qui les dévorent.\nJusqu'au jour où un titan colossal apparaît.")
                def R2 ():
                    R.config(text="Les titans ont percé la première\nenceinte de la ville. Les survivants\ns'enfuient. Hannes présente ses excuses\nà Eren pour la mort de sa mère.")
                def R3 ():
                    R.config(text="Eren intègre l'armée. Il se retrouve\nsous le commandement de Keith Sadies,\nun formateur sévère. Eren découvre\nl'équipement spécifique des troupes.")
                def R4 ():
                    R.config(text="Eren poursuit son entraînement avec\nles autres recrues, sous la supervision de\nKeith. Il apprend que certains engagés\nsouhaitent rejoindre la police militaire.")
                def R5 ():
                    R.config(text="Eren attaque le titan colossal, qui\nmontre une certaine intelligence en s'en\nprenant aux canons du mur. Au moment où\nEren s'apprête à le frapper à son point\n faible, le monstre disparaît…")
                def R6 ():
                    R.config(text="Armin se réveille, entouré par\nConnie, Ymir et l'équipe de Krista. Il\nfond en larmes lorsqu'on lui demande ce\nqu'il est advenu de son équipe. Armin s'en\nveut surtout pour ne pas avoir réussi\nà sauver Eren…")
                def R7 ():
                    R.config(text="Les survivants, incapables de\ngravir le mur, perdent le moral quand\ndes titans détruisent les dépôts les\nplus proches, où ils espéraient trouver\n du carburant.")
                def R8 ():
                    R.config(text="Alors que le dépôt est entouré\npar les Titans, Armin a l'idée\nd'utiliser le Rogue Titan pour les\ndétruire. Pendant ce temps, Jean et\nles autres atteignent le dépôt, au prix\n de lourdes pertes…")
                def R9 ():
                    R.config(text="Alors que l'unité de Levi parvient\nà reprendre une ville aux Titans, elle\nest appelée à l'aide pour éliminer les\ncréatures qui ont envahi la cité…")
                def R10 ():
                    R.config(text="Eren récupère de sa transformation,\nqui lui a permis de sauver Armine et Mikasa.\nIl pense détenir la clé de la préservation de\nl'humanité et le moyen de détruire les Titans…")
                def R11 ():
                    R.config(text="Armin aide les hommes de Pixis à\nélaborer un plan, ce qui leur rend espoir.\nPixis se charge ensuite de calmer tout le monde\net de les pousser à combattre.")
                def R12 ():
                    R.config(text="Mikasa cherche en vain à raisonner\nEren sous sa forme titanesque. Ce dernier\ncontinue ses attaques et finit par se blesser.\nSes accompagnateurs lancent une fusée pour\navertir de l'échec du plan...")

                mas1=Tk()
                mas1.title('ADT S1')
        
                m1=PanedWindow(mas1,bg='darkred')
                m1.grid(row=0,column=0)

                m2=PanedWindow(mas1)
                m2.grid(row=1,column=0)
        
                rem1 = Button(m1, text='Episode 1',bd=8,activebackground='blue',activeforeground="red",command=R1,overrelief=GROOVE)
                rem1.grid(row=0,column=0)

                rem2 = Button(m1, text='Episode 2',bd=8,activebackground='blue',activeforeground="red",command=R2,overrelief=GROOVE)
                rem2.grid(row=1,column=0)

                rem3 = Button(m1, text='Episode 3',bd=8,activebackground='blue',activeforeground="red",command=R3,overrelief=GROOVE)
                rem3.grid(row=2,column=0)

                rem4 = Button(m1, text='Episode 4',bd=8,activebackground='blue',activeforeground="red",command=R4,overrelief=GROOVE)
                rem4.grid(row=3,column=0)
        
                rem5 = Button(m1, text='Episode 5',bd=8,activebackground='blue',activeforeground="red",command=R5,overrelief=GROOVE)
                rem5.grid(row=4,column=0)

                rem6 = Button(m1, text='Episode 6',bd=8,activebackground='blue',activeforeground="red",command=R6,overrelief=GROOVE)
                rem6.grid(row=5,column=0)

                rem7 = Button(m1, text='Episode 7',bd=8,activebackground='blue',activeforeground="red",command=R7,overrelief=GROOVE)
                rem7.grid(row=6,column=0)

                rem8 = Button(m1, text='Episode 8',bd=8,activebackground='blue',activeforeground="red",command=R8,overrelief=GROOVE)
                rem8.grid(row=7,column=0)

                rem9 = Button(m1, text='Episode 9',bd=8,activebackground='blue',activeforeground="red",command=R9,overrelief=GROOVE)
                rem9.grid(row=8,column=0)

                rem10 = Button(m1, text='Episode 10',bd=8,activebackground='blue',activeforeground="red",command=R10,overrelief=GROOVE)
                rem10.grid(row=9,column=0)

                rem11 = Button(m1, text='Episode 11',bd=8,activebackground='blue',activeforeground="red",command=R11,overrelief=GROOVE)
                rem11.grid(row=10,column=0)

                rem12 = Button(m1, text='Episode 12',bd=8,activebackground='blue',activeforeground="red",command=R12,overrelief=GROOVE)
                rem12.grid(row=11,column=0)

                em1 = Label(m1, text='La chute de Shiganshina', font ='Arial 11 bold italic',bg='white')
                em1.grid(row=0,column=1)

                em2 = Label(m1, text='Ce jour-là',font ='Arial 11 bold italic',bg='white')
                em2.grid(row=1,column=1)

                em3 = Label(m1, text='Une faible étincelle dans le désespoir',font ='Arial 11 bold italic',bg='white')
                em3.grid(row=2,column=1)

                em4 = Label(m1, text="Le réveil de l'humanité",font ='Arial 11 bold italic',bg='white')
                em4.grid(row=3,column=1)
        
                em5 = Label(m1, text="Première bataille",font ='Arial 11 bold italic',bg='white')
                em5.grid(row=4,column=1)

                em6 = Label(m1, text="Une petite lame",font ='Arial 11 bold italic',bg='white')
                em6.grid(row=5,column=1)

                em7 = Label(m1, text="La lutte pour le district de Trost",font ='Arial 11 bold italic',bg='white')
                em7.grid(row=6,column=1)

                em8 = Label(m1, text="J'entends les battements de ton coeur",font ='Arial 11 bold italic',bg='white')
                em8.grid(row=7,column=1)

                em9 = Label(m1, text="Qu'est-il advenu du bras gauche ?",font ='Arial 11 bold italic',bg='white')
                em9.grid(row=8,column=1)

                em10 = Label(m1, text='Répondre',font ='Arial 11 bold italic',bg='white')
                em10.grid(row=9,column=1)

                em11 = Label(m1, text='Idole',font ='Arial 11 bold italic',bg='white')
                em11.grid(row=10,column=1)

                em12 = Label(m1, text='Blessure',font ='Arial 11 bold italic',bg='white')
                em12.grid(row=11,column=1)

                mp1 = Button(m1, bitmap='hourglass',command=pa)
                mp1.grid(row=0,column=2)

                mp2 = Button(m1, bitmap='hourglass',command=pa)
                mp2.grid(row=1,column=2)

                mp3 = Button(m1, bitmap='hourglass',command=pa)
                mp3.grid(row=2,column=2)

                mp4 = Button(m1,bitmap='hourglass',command=pa)
                mp4.grid(row=3,column=2)
                
                mp5 = Button(m1, bitmap='hourglass',command=pa)
                mp5.grid(row=4,column=2)

                mp6 = Button(m1, bitmap='hourglass',command=pa)
                mp6.grid(row=5,column=2)

                mp7 = Button(m1, bitmap='hourglass',command=pa)
                mp7.grid(row=6,column=2)

                mp8 = Button(m1, bitmap='hourglass',command=pa)
                mp8.grid(row=7,column=2)

                mp9 = Button(m1, bitmap='hourglass',command=pa)
                mp9.grid(row=8,column=2)

                mp10 = Button(m1, bitmap='hourglass',command=pa)
                mp10.grid(row=9,column=2)

                mp11 = Button(m1, bitmap='hourglass',command=pa)
                mp11.grid(row=10,column=2)

                mp11 = Button(m1, bitmap='hourglass',command=pa)
                mp11.grid(row=11,column=2)

                R = Label(m2,text='')
                R.grid(row=1,column=0)
 
                mainloop()



        l2= Label(p11, text= "Sélectionnez", font="Arial 9")
        l2.grid(row=0, column=0)

        b1= Button(p11, text= "Valider",command=snk)
        b1.grid(row=0, column= 2)

        mainloop()

    elif r==4:
        global prix
        imgg = PhotoImage(file="4.png")
        label=Label(p9,image=imgg)
        label.grid(row=0,column=0)
    
        l1.config(text= "Rick Sanchez est un vieux scientifique\nalcoolique au caractère imprévisible et exubérant \nqui passe son temps à entraîner son petit-fils Morty\ndans des aventures folles et dangereuses...")
        
        L= ['Saison 1', 'Saison 2','Saison 3']
        c1= ttk.Combobox(p11, values= L)
        c1.grid(row = 0, column = 1)


        def Rem ():
            global prix
            def pa():
                global prix
                prix=prix+3

            r=c1.get()
            if r=='Saison 1':
                global prix
                def R1 ():
                    R.config(text="Rick part avec Morty chercher des graines\nde 'méga-arbres' dans une autre dimension alors\nque Jerry et Beth se disputent au sujet de\nl'influence de Rick sur leur fils.")
                def R2 ():
                    R.config(text="Rick invente une machine à rendre Snuffles\nplus intelligent. Rick et Morty s'immiscent dans\nles rêves du professeur de math de Morty.")
                def R3 ():
                    R.config(text="Morty termine dans un étrange parc à thèmes\nde maladies graves à l'intérieur du corps d'un\nsans-abri. Jerry reçoit la visite de ses parents.")
                def R4 ():
                    R.config(text="Des extraterrestres envoient Rick, Morty et\nJerry dans un univers parallèle afin de\ndécouvrir un secret.")
                def R5 ():
                    R.config(text="Las des histoires de Rick, Morty se lance\ndans une aventure qu'il croit plus sûre. Jerry\nfait appel à d'étranges créatures pour\n l'aider au golf.")
                def R6 ():
                    R.config(text="Un philtre d'amour concocté pour Morty\nfinit par infecter toute la planète. Rick doit\nalors régler le problème par un autre problème.")
                def R7 ():
                    R.config(text="Quand Morty devient père de famille,\nRick et Summer se rendent sur la planète de\nson robot, où les enfants se transforment en\nadultes en l'espace de quelques jours.")
                def R8 ():
                    R.config(text="Rick modifie le modem afin de pouvoir\n regarder les chaînes des autres dimensions.\nChacun porte des lunettes spéciales pour voir\nà quoi il correspond dans l'autre monde.")
                def R9 ():
                    R.config(text="Rick a des doutes sur le nouveau travail\nque Summer a trouvé dans une boutique tenue par\nle diable. Jerry et Morty vont sur Pluton pour\n mettre fin à une controverse.")
                def R10 ():
                    R.config(text="Un groupe d'anciens associés enlève Rick\nalors qu'il prend son petit-déjeuner afin de le\njuger pour tout ce qu'il leur a fait subir.")
                def R11 ():
                    R.config(text="Profitant de l'absence de Jerry et Beth,\nRick et Summer organisent une fête gigantesque\n dont ils perdent le contrôle.")
                master1=Tk()
                master1.title('ReM S1')

                m2=PanedWindow(master1,bg='teal')
                m2.grid(row=0,column=0)

                m3=PanedWindow(master1)
                m3.grid(row=1,column=0)

                rem1 = Button(m2, text='Résumé Episode 1 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R1,overrelief=GROOVE)
                rem1.grid(row=0,column=0)

                rem2 = Button(m2, text='Résumé Episode 2 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R2,overrelief=GROOVE)
                rem2.grid(row=1,column=0)

                rem3 = Button(m2, text='Résumé Episode 3 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R3,overrelief=GROOVE)
                rem3.grid(row=2,column=0)

                rem4 = Button(m2, text='Résumé Episode 4 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R4,overrelief=GROOVE)
                rem4.grid(row=3,column=0)
        
                rem5 = Button(m2, text='Résumé Episode 5 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R5,overrelief=GROOVE)
                rem5.grid(row=4,column=0)

                rem6 = Button(m2, text='Résumé Episode 6 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R6,overrelief=GROOVE)
                rem6.grid(row=5,column=0)

                rem7 = Button(m2, text='Résumé Episode 7 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R7,overrelief=GROOVE)
                rem7.grid(row=6,column=0)

                rem8 = Button(m2, text='Résumé Episode 8 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R8,overrelief=GROOVE)
                rem8.grid(row=7,column=0)

                rem9 = Button(m2, text='Résumé Episode 9 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R9,overrelief=GROOVE)
                rem9.grid(row=8,column=0)

                rem10 = Button(m2, text='Résumé Episode 10',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R10,overrelief=GROOVE)
                rem10.grid(row=9,column=0)

                rem11 = Button(m2, text='Résumé Episode 11',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R11,overrelief=GROOVE)
                rem11.grid(row=10,column=0)
        
                em1 = Label(m2, text='Pilote', font ='Arial 11 bold italic',bg='azure')
                em1.grid(row=0,column=1)

                em2 = Label(m2, text='Croquette',font ='Arial 11 bold italic',bg='azure')
                em2.grid(row=1,column=1)

                em3 = Label(m2, text='Anatomy park',font ='Arial 11 bold italic',bg='azure')
                em3.grid(row=2,column=1)

                em4 = Label(m2, text='M.Night Shaym-Aliens',font ='Arial 11 bold italic',bg='azure')
                em4.grid(row=3,column=1)
        
                em5 = Label(m2, text='La boîte à larbins ',font ='Arial 11 bold italic',bg='azure')
                em5.grid(row=4,column=1)

                em6 = Label(m2, text='E-Rick-xir d’amour',font ='Arial 11 bold italic',bg='azure')
                em6.grid(row=5,column=1)

                em7 = Label(m2, text='Gazorpazorp Junior',font ='Arial 11 bold italic',bg='azure')
                em7.grid(row=6,column=1)

                em8 = Label(m2, text='Télé…visons ',font ='Arial 11 bold italic',bg='azure')
                em8.grid(row=7,column=1)

                em9 = Label(m2, text='La petite bou-Rick des horreurs',font ='Arial 11 bold italic',bg='azure')
                em9.grid(row=8,column=1)

                em10 = Label(m2, text='Rencontres du troisième Rick',font ='Arial 11 bold italic',bg='azure')
                em10.grid(row=9,column=1)

                em11 = Label(m2, text='Ricksy Business',font ='Arial 11 bold italic',bg='azure')
                em11.grid(row=10,column=1)

                mp1 = Button(m2, bitmap='hourglass',command=pa)
                mp1.grid(row=0,column=2)

                mp2 = Button(m2, bitmap='hourglass',command=pa)
                mp2.grid(row=1,column=2)

                mp3 = Button(m2, bitmap='hourglass',command=pa)
                mp3.grid(row=2,column=2)

                mp4 = Button(m2,bitmap='hourglass',command=pa)
                mp4.grid(row=3,column=2)
                
                mp5 = Button(m2, bitmap='hourglass',command=pa)
                mp5.grid(row=4,column=2)

                mp6 = Button(m2, bitmap='hourglass',command=pa)
                mp6.grid(row=5,column=2)

                mp7 = Button(m2, bitmap='hourglass',command=pa)
                mp7.grid(row=6,column=2)

                mp8 = Button(m2, bitmap='hourglass',command=pa)
                mp8.grid(row=7,column=2)

                mp9 = Button(m2, bitmap='hourglass',command=pa)
                mp9.grid(row=8,column=2)

                mp10 = Button(m2, bitmap='hourglass',command=pa)
                mp10.grid(row=9,column=2)

                mp11 = Button(m2, bitmap='hourglass',command=pa)
                mp11.grid(row=10,column=2)

                R = Label(m3,text='')
                R.grid(row=1,column=0)

                mainloop()
        
            elif r=='Saison 2':
                global prix
                def R1 ():
                    R.config(text="Rick arrête de figer le temps, ce qui provoque\n l'apparition d'un univers parallèle...")
                def R2 ():
                    R.config(text="Lorsque Rick vend une arme à un assassin extraterrestre\npour jouer aux jeux vidéo, Morty se lance à la poursuite\n du meurtrier afin de l'arrêter.")
                def R3 ():
                    R.config(text="Rick renoue avec une ancienne compagne du nom d'Unity\nsouhaitant contrôler la population d'une planète\n extraterrestre, mais Summer s'y oppose.")
                def R4 ():
                    R.config(text="Un parasite produit de faux souvenirs dans la tête des\nmembres de la famille, qui ne savent plus si l'un\n de leurs amis existe vraiment.")
                def R5 ():
                    R.config(text="Rick et Morty demandent à Ice-T de les aider à\ncomposer une chanson pour un télé-crochet intergalactique.")
                def R6 ():
                    R.config(text="Lorsque la voiture de Rick tombe en panne,\nMorty découvre que Rick a créé un univers miniature\n dans la batterie.")
                def R7 ():
                    R.config(text="Summer demande à Rick de se transformer en\nadolescent pour la protéger des vampires de l'école.\nBeth et Jerry suivent une thérapie de couple\n hors de la Terre.")
                def R8 ():
                    R.config(text="Jerry termine à l'hôpital après avoir mangé\nune glace dont Rick se servait pour développer une\n dangereuse bactérie.")
                def R9 ():
                    R.config(text="Rick et Morty atterrissent sur une planète\noù tous les habitants ont le droit, pendant une\nnuit, de commettre des crimes sans être punis.")
                def R10 ():
                    R.config(text="Jerry est envoyé sur la planète où se tient\nle mariage de Condorman et Tammy, obligeant toute la\nfamille à assister à une cérémonie qui ne se passe\n pas comme prévu.")
                master2=Tk()
                master2.title('ReM S2')
        
                m2=PanedWindow(master2,bg='teal')
                m2.grid(row=0,column=0)

                m3=PanedWindow(master2)
                m3.grid(row=1,column=0)
        
                rem1 = Button(m2, text='Résumé Episode 1 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R1,overrelief=GROOVE)
                rem1.grid(row=0,column=0)

                rem2 = Button(m2, text='Résumé Episode 2 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R2,overrelief=GROOVE)
                rem2.grid(row=1,column=0)

                rem3 = Button(m2, text='Résumé Episode 3 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R3,overrelief=GROOVE)
                rem3.grid(row=2,column=0)

                rem4 = Button(m2, text='Résumé Episode 4 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R4,overrelief=GROOVE)
                rem4.grid(row=3,column=0)
        
                rem5 = Button(m2, text='Résumé Episode 5 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R5,overrelief=GROOVE)
                rem5.grid(row=4,column=0)

                rem6 = Button(m2, text='Résumé Episode 6 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R6,overrelief=GROOVE)
                rem6.grid(row=5,column=0)

                rem7 = Button(m2, text='Résumé Episode 7 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R7,overrelief=GROOVE)
                rem7.grid(row=6,column=0)

                rem8 = Button(m2, text='Résumé Episode 8 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R8,overrelief=GROOVE)
                rem8.grid(row=7,column=0)

                rem9 = Button(m2, text='Résumé Episode 9 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R9,overrelief=GROOVE)
                rem9.grid(row=8,column=0)

                rem10 = Button(m2, text='Résumé Episode 10',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R10,overrelief=GROOVE)
                rem10.grid(row=9,column=0)

                em1 = Label(m2, text='Effet Rick-ochet', font ='Arial 11 bold italic',bg='azure')
                em1.grid(row=0,column=1)

                em2 = Label(m2, text='Prout, l’extra-terrestre',font ='Arial 11 bold italic',bg='azure')
                em2.grid(row=1,column=1)

                em3 = Label(m2, text='Assimilation auto-érotique',font ='Arial 11 bold italic',bg='azure')
                em3.grid(row=2,column=1)

                em4 = Label(m2, text='Total Rickall',font ='Arial 11 bold italic',bg='azure')
                em4.grid(row=3,column=1)
        
                em5 = Label(m2, text='On va vous faire schwifter',font ='Arial 11 bold italic',bg='azure')
                em5.grid(row=4,column=1)

                em6 = Label(m2, text='Les Ricks sont tombés sur la tête',font ='Arial 11 bold italic',bg='azure')
                em6.grid(row=5,column=1)

                em7 = Label(m2, text='Mini-Rick, méga hic',font ='Arial 11 bold italic',bg='azure')
                em7.grid(row=6,column=1)

                em8 = Label(m2, text='Cable interdimensionnel 2',font ='Arial 11 bold italic',bg='azure')
                em8.grid(row=7,column=1)

                em9 = Label(m2, text='Qui est ce qui purge, maintenant ?',font ='Arial 11 bold italic',bg='azure')
                em9.grid(row=8,column=1)

                em10 = Label(m2, text='Mariage à la squanchaise',font ='Arial 11 bold italic',bg='azure')
                em10.grid(row=9,column=1)

                mp1 = Button(m2, bitmap='hourglass',command=pa)
                mp1.grid(row=0,column=2)

                mp2 = Button(m2, bitmap='hourglass',command=pa)
                mp2.grid(row=1,column=2)

                mp3 = Button(m2, bitmap='hourglass',command=pa)
                mp3.grid(row=2,column=2)

                mp4 = Button(m2,bitmap='hourglass',command=pa)
                mp4.grid(row=3,column=2)
                
                mp5 = Button(m2, bitmap='hourglass',command=pa)
                mp5.grid(row=4,column=2)

                mp6 = Button(m2, bitmap='hourglass',command=pa)
                mp6.grid(row=5,column=2)

                mp7 = Button(m2, bitmap='hourglass',command=pa)
                mp7.grid(row=6,column=2)

                mp8 = Button(m2, bitmap='hourglass',command=pa)
                mp8.grid(row=7,column=2)

                mp9 = Button(m2, bitmap='hourglass',command=pa)
                mp9.grid(row=8,column=2)

                mp10 = Button(m2, bitmap='hourglass',command=pa)
                mp10.grid(row=9,column=2)

                R = Label(m3,text='')
                R.grid(row=1,column=0)
 
                mainloop()
                
            elif r=='Saison 3':
                global prix
                def R1 ():
                    R.config(text="Summer et Morty voyagent à travers les dimensions\npour tenter de retrouver Rick, tandis que celui-ci se\n prend de passion pour une sauce pour nuggets.")
                def R2 ():
                    R.config(text="Rick, Morty et Summer décident de fuir le chaos du\nquotidien en voyageant dans un monde post-apocalyptique pour\n tenter de résoudre leurs problèmes personnels.")
                def R3 ():
                    R.config(text="Rick, Morty et Summer décident de fuir le chaos du\nquotidien en voyageant dans un monde post-apocalyptique pour\n tenter de résoudre leurs problèmes personnels.")
                def R4 ():
                    R.config(text="Censé aider un groupe de super-héros vengeurs, un\nRick alcoolisé leur prépare au contraire un scénario qui\n finit par un petit coup de scie bien senti…")
                def R5 ():
                    R.config(text="Alors que Rick et Jerry séjournent dans un hôtel où\nmourir est impossible, une créature a décidé d'en finir avec\n Rick. Le projet de Summer tourne à la catastrophe.")
                def R6 ():
                    R.config(text="Après une aventure épuisante, Rick et Morty décident\nqu'il leur faut des vacances. Mais voilà que la machine\ns'emballe quand ils essaient un nouveau système détox.")
                def R7 ():
                    R.config(text="Rick et Morty font la connaissance de leurs homonymes\nde la Citadelle des Ricks avant de vivre de passionnantes\n aventures sur l'Atlantide.")
                def R8 ():
                    R.config(text="Alors que Rick a gardé en stock les souvenirs que Morty\nlui a demandé d'effacer de sa mémoire, la situation dégénère\n quand Rick décide de remuer le passé.")
                def R9 ():
                    R.config(text="Rick aide Beth à surmonter ses traumatismes d'enfance\nen l'accompagnant à Froopy Land. Morty et Summer se montrent\n méfiants envers la nouvelle petite amie de Jerry.")
                def R10 ():
                    R.config(text="Rick et Morty acceptent malgré eux de venir en aide au\nPrésident des États-Unis. Beth fait face au doute : est-elle\n vraiment elle-même ou son propre clone ?")
                master3=Tk()
                master3.title('ReM S3')
        
                m2=PanedWindow(master3,bg='teal')
                m2.grid(row=0,column=0)

                m3=PanedWindow(master3)
                m3.grid(row=1,column=0)
        
                rem1 = Button(m2, text='Résumé Episode 1 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R1,overrelief=GROOVE)
                rem1.grid(row=0,column=0)

                rem2 = Button(m2, text='Résumé Episode 2 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R2,overrelief=GROOVE)
                rem2.grid(row=1,column=0)

                rem3 = Button(m2, text='Résumé Episode 3 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R3,overrelief=GROOVE)
                rem3.grid(row=2,column=0)

                rem4 = Button(m2, text='Résumé Episode 4 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R4,overrelief=GROOVE)
                rem4.grid(row=3,column=0)
        
                rem5 = Button(m2, text='Résumé Episode 5 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R5,overrelief=GROOVE)
                rem5.grid(row=4,column=0)

                rem6 = Button(m2, text='Résumé Episode 6 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R6,overrelief=GROOVE)
                rem6.grid(row=5,column=0)

                rem7 = Button(m2, text='Résumé Episode 7 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R7,overrelief=GROOVE)
                rem7.grid(row=6,column=0)

                rem8 = Button(m2, text='Résumé Episode 8 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R8,overrelief=GROOVE)
                rem8.grid(row=7,column=0)

                rem9 = Button(m2, text='Résumé Episode 9 ',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R9,overrelief=GROOVE)
                rem9.grid(row=8,column=0)

                rem10 = Button(m2, text='Résumé Episode 10',bd=8,activebackground='blue',activeforeground="red",bg='teal',command=R10,overrelief=GROOVE)
                rem10.grid(row=9,column=0)

                em1 = Label(m2, text='A la recherche de Rick', font ='Arial 11 bold italic',bg='azure')
                em1.grid(row=0,column=1)

                em2 = Label(m2, text='A la recherche de la pierre verte',font ='Arial 11 bold italic',bg='azure')
                em2.grid(row=1,column=1)

                em3 = Label(m2, text='Rick-ornichon',font ='Arial 11 bold italic',bg='azure')
                em3.grid(row=2,column=1)

                em4 = Label(m2, text='Troisième édition',font ='Arial 11 bold italic',bg='azure')
                em4.grid(row=3,column=1)
        
                em5 = Label(m2, text='Conspiration',font ='Arial 11 bold italic',bg='azure')
                em5.grid(row=4,column=1)

                em6 = Label(m2, text='Repos et Ricklaxation',font ='Arial 11 bold italic',bg='azure')
                em6.grid(row=5,column=1)

                em7 = Label(m2, text='Confusion en Ricklantide',font ='Arial 11 bold italic',bg='azure')
                em7.grid(row=6,column=1)

                em8 = Label(m2, text='Les souvenirs effacés de Morty',font ='Arial 11 bold italic',bg='azure')
                em8.grid(row=7,column=1)

                em9 = Label(m2, text='Froopyland',font ='Arial 11 bold italic',bg='azure')
                em9.grid(row=8,column=1)

                em10 = Label(m2, text='L’ami de Washington',font ='Arial 11 bold italic',bg='azure')
                em10.grid(row=9,column=1)

                mp1 = Button(m2, bitmap='hourglass',command=pa)
                mp1.grid(row=0,column=2)

                mp2 = Button(m2, bitmap='hourglass',command=pa)
                mp2.grid(row=1,column=2)

                mp3 = Button(m2, bitmap='hourglass',command=pa)
                mp3.grid(row=2,column=2)

                mp4 = Button(m2,bitmap='hourglass',command=pa)
                mp4.grid(row=3,column=2)
                
                mp5 = Button(m2, bitmap='hourglass',command=pa)
                mp5.grid(row=4,column=2)

                mp6 = Button(m2, bitmap='hourglass',command=pa)
                mp6.grid(row=5,column=2)

                mp7 = Button(m2, bitmap='hourglass',command=pa)
                mp7.grid(row=6,column=2)

                mp8 = Button(m2, bitmap='hourglass',command=pa)
                mp8.grid(row=7,column=2)

                mp9 = Button(m2, bitmap='hourglass',command=pa)
                mp9.grid(row=8,column=2)

                mp10 = Button(m2, bitmap='hourglass',command=pa)
                mp10.grid(row=9,column=2)

                R = Label(m3,text='')
                R.grid(row=1,column=0)
 
                mainloop()

        l2= Label(p11, text= "Sélectionnez", font="Arial 9")
        l2.grid(row=0, column=0)

        b1= Button(p11, text= "Valider",command=Rem)
        b1.grid(row=0, column= 2)

        mainloop()

    elif r==5:
        global prix
        imgg = PhotoImage(file="5.png")
        label=Label(p9,image=imgg)
        label.grid(row=0,column=0)
    
        l1.config(text= "Huit voleurs font une prise d'otages dans la Maison royale de la Monnaie \nd'Espagne, tandis qu'un génie du crime manipule la police pour mettre \nson plan à exécution.")

        L= ['Saison 1', 'Saison 2']
        c1= ttk.Combobox(p11, values= L)
        c1.grid(row = 0, column = 1)

        def lcdp ():
            global prix
            def pa():
                global prix
                prix=prix+3

            r=c1.get()
            if r=='Saison 1':
                global prix
                def R1 ():
                    R.config(text="Le Professeur recrute une jeune\nbraqueuse et sept autres criminels en vue\nd'un cambriolage grandiose ciblant la\nMaison royale de la Monnaie d'Espagne.")
                def R2 ():
                    R.config(text="Raquel, qui gère les négociations\npour la libération des otages, établit\nun contact avec le Professeur. L'un des\notages est un élément clé du plan des\n cambrioleurs.")
                def R3 ():
                    R.config(text="La police identifie l'un des\ncambrioleurs. Raquel se méfie de\nl'homme qu'elle a rencontré dans\n un bar.")
                def R4 ():
                    R.config(text="Raquel traverse une crise\npersonnelle avec son ex. Les otages\nprennent peur en entendant des coups\nde feu. Les cambrioleurs n'arrivent\npas à se mettre d'accord.")
                def R5 ():
                    R.config(text="Les cambrioleurs laissent\ndes médecins entrer dans l'édifice\net un policier s'infiltre parmi\neux. Le Professeur saura-t-il\ngarder une longueur d'avance\n sur Raquel ?")
                def R6 ():
                    R.config(text="L'état de Mónica s'aggrave.\nLe Professeur se délecte après sa\ndernière ruse. Rio est troublé par\nune nouvelle dont il prend\nconnaissance à la télévision.")
                def R7 ():
                    R.config(text="Le Professeur risque d'être\ndécouvert à cause d'une avancée\ndans l'enquête et d'une erreur\ncommise par l'un des cambrioleurs.")
                def R8 ():
                    R.config(text="Tokyo surprend Alison en\ntrain de bavarder avec Rio et la\nmet au pied du mur. La police pense\navoir été infiltrée par un espion.")
                def R9 ():
                    R.config(text="Le Professeur se hâte pour\nempêcher un témoin de l'identifier.\nBerlin cherche à se venger quand son\nnom est dévoilé et bafoué dans la presse.")
                def R10 ():
                    R.config(text="Raquel pénètre dans la\nMaison de la Monnaie pour\ns'assurer que tous les otages\nsont encore sains et saufs.\nNairobi donne un conseil à Alison.")
                def R11 ():
                    R.config(text=" Ángel et Raquel mettent\nleur loyauté respective en doute.\nMónica prend l'initiative avec\nDenver. Rio doit prendre une\ndécision difficile.")
                mast1=Tk()
                mast1.title('lcdp S1')
        
                m1=PanedWindow(mast1,bg='red')
                m1.grid(row=0,column=0)

                m2=PanedWindow(mast1)
                m2.grid(row=1,column=0)
        
                rem1 = Button(m1, text='Résumé Episode 1',bd=8,activebackground='blue',activeforeground="red",font ='Arial 11 bold italic',bg='azure',command=R1,overrelief=GROOVE)
                rem1.grid(row=0,column=0)

                rem2 = Button(m1, text='Résumé Episode 2',bd=8,activebackground='blue',activeforeground="red",font ='Arial 11 bold italic',bg='azure',command=R2,overrelief=GROOVE)
                rem2.grid(row=1,column=0)

                rem3 = Button(m1, text='Résumé Episode 3',bd=8,activebackground='blue',activeforeground="red",font ='Arial 11 bold italic',bg='azure',command=R3,overrelief=GROOVE)
                rem3.grid(row=2,column=0)

                rem4 = Button(m1, text='Résumé Episode 4',bd=8,activebackground='blue',activeforeground="red",font ='Arial 11 bold italic',bg='azure',command=R4,overrelief=GROOVE)
                rem4.grid(row=3,column=0)
        
                rem5 = Button(m1, text='Résumé Episode 5',bd=8,activebackground='blue',activeforeground="red",font ='Arial 11 bold italic',bg='azure',command=R5,overrelief=GROOVE)
                rem5.grid(row=4,column=0)

                rem6 = Button(m1, text='Résumé Episode 6',bd=8,activebackground='blue',activeforeground="red",font ='Arial 11 bold italic',bg='azure',command=R6,overrelief=GROOVE)
                rem6.grid(row=5,column=0)

                rem7 = Button(m1, text='Résumé Episode 7',bd=8,activebackground='blue',activeforeground="red",font ='Arial 11 bold italic',bg='azure',command=R7,overrelief=GROOVE)
                rem7.grid(row=6,column=0)

                rem8 = Button(m1, text='Résumé Episode 8',bd=8,activebackground='blue',activeforeground="red",font ='Arial 11 bold italic',bg='azure',command=R8,overrelief=GROOVE)
                rem8.grid(row=7,column=0)

                rem9 = Button(m1, text='Résumé Episode 9',bd=8,activebackground='blue',activeforeground="red",font ='Arial 11 bold italic',bg='azure',command=R9,overrelief=GROOVE)
                rem9.grid(row=8,column=0)

                rem10 = Button(m1, text='Résumé Episode 10',bd=8,activebackground='blue',activeforeground="red",font ='Arial 11 bold italic',bg='azure',command=R10,overrelief=GROOVE)
                rem10.grid(row=9,column=0)

                rem11 = Button(m1, text='Résumé Episode 11',bd=8,activebackground='blue',activeforeground="red",font ='Arial 11 bold italic',bg='azure',command=R11,overrelief=GROOVE)
                rem11.grid(row=10,column=0)

                em1 = Label(m1, text='Partie 1 ', font ='Arial 11 bold italic',bg='azure')
                em1.grid(row=0,column=1)

                em2 = Label(m1, text='Partie 2 ',font ='Arial 11 bold italic',bg='azure')
                em2.grid(row=1,column=1)

                em3 = Label(m1, text='Partie 3 ',font ='Arial 11 bold italic',bg='azure')
                em3.grid(row=2,column=1)

                em4 = Label(m1, text='Partie 4 ',font ='Arial 11 bold italic',bg='azure')
                em4.grid(row=3,column=1)
        
                em5 = Label(m1, text='Partie 5 ',font ='Arial 11 bold italic',bg='azure')
                em5.grid(row=4,column=1)

                em6 = Label(m1, text='Partie 6 ',font ='Arial 11 bold italic',bg='azure')
                em6.grid(row=5,column=1)

                em7 = Label(m1, text='Partie 7 ',font ='Arial 11 bold italic',bg='azure')
                em7.grid(row=6,column=1)

                em8 = Label(m1, text='Partie 8 ',font ='Arial 11 bold italic',bg='azure')
                em8.grid(row=7,column=1)

                em9 = Label(m1, text='Partie 9 ',font ='Arial 11 bold italic',bg='azure')
                em9.grid(row=8,column=1)

                em10 = Label(m1, text='Partie 10',font ='Arial 11 bold italic',bg='azure')
                em10.grid(row=9,column=1)

                em11 = Label(m1, text='Partie 11',font ='Arial 11 bold italic',bg='azure')
                em11.grid(row=10,column=1)

                mp1 = Button(m1, bitmap='hourglass',command=pa)
                mp1.grid(row=0,column=2)

                mp2 = Button(m1, bitmap='hourglass',command=pa)
                mp2.grid(row=1,column=2)

                mp3 = Button(m1, bitmap='hourglass',command=pa)
                mp3.grid(row=2,column=2)

                mp4 = Button(m1,bitmap='hourglass',command=pa)
                mp4.grid(row=3,column=2)
                
                mp5 = Button(m1, bitmap='hourglass',command=pa)
                mp5.grid(row=4,column=2)

                mp6 = Button(m1, bitmap='hourglass',command=pa)
                mp6.grid(row=5,column=2)

                mp7 = Button(m1, bitmap='hourglass',command=pa)
                mp7.grid(row=6,column=2)

                mp8 = Button(m1, bitmap='hourglass',command=pa)
                mp8.grid(row=7,column=2)

                mp9 = Button(m1, bitmap='hourglass',command=pa)
                mp9.grid(row=8,column=2)

                mp10 = Button(m1, bitmap='hourglass',command=pa)
                mp10.grid(row=9,column=2)

                mp11 = Button(m1, bitmap='hourglass',command=pa)
                mp11.grid(row=10,column=2)

                R = Label(m2,text='')
                R.grid(row=1,column=0)

                mainloop()
        
            elif r=='Saison 2':
                global prix
                def R1 ():
                    R.config(text="Alors que la police\nscientifique cherche des\ntraces d'ADN dans la maison\nde Tolède, le Professeur perd\nle contrôle. Les cambrioleurs\nsont au bord de la crise de nerfs.")
                def R2 ():
                    R.config(text="La police interroge\nle premier malfaiteur capturé.\nFurieux contre Berlin et ses\nagissements récents, Rio prend\nposition contre lui.")
                def R3 ():
                    R.config(text="Espérant apprendre\nl'identité du Professeur,\nRaquel en appelle aux émotions\nde son prisonnier. Une punition\ndéclenche une révolte chez\n les voleurs.")
                def R4 ():
                    R.config(text="Comme ils réalisent\nque leur plan capote, les\nvoleurs veulent utiliser la\npresse pour gagner la\nconfiance du public. Raquel\nprépare un piège pour capturer\n le Professeur.")
                def R5 ():
                    R.config(text="Arturo tente un autre\nplan d'évasion. À l'occasion\nd'une discussion avec Salva,\nun petit détail attire\nl'attention de Raquel. Les\nidées se bousculent alors\n dans sa tête.")
                def R6 ():
                    R.config(text="Après avoir confessé\nun secret longtemps bien gardé,\nMoscou perd la confiance de son\nfils. Quand le plan B pour\nlibérer Tokyo échoue, elle\n doit improviser.")
                def R7 ():
                    R.config(text="Alors que l'un des\nleurs est grièvement blessé,\nles cambrioleurs entament une\ncourse contre la montre pour\nle sauver. Seule avec Mónica,\nAriadna lui fait une confession.")
                def R8 ():
                    R.config(text="Comme elle a été retirée\nde l'affaire à cause de sa\nrelation avec le Professeur,\nRaquel décide de trouver\nelle-même le cerveau du braquage.")
                def R9 ():
                    R.config(text="Quand la police s'introduit\ndans la Maison de la Monnaie,\nBerlin entraîne les cambrioleurs\ndans une ultime épreuve.\nSauront-ils s'échapper avec\nle butin et la vie sauve ?")
                mast2=Tk()
                mast2.title('lcdp S2')
        
                m1=PanedWindow(mast2,bg='red')
                m1.grid(row=0,column=0)

                m2=PanedWindow(mast2)
                m2.grid(row=1,column=0)
        
                rem1 = Button(m1, text='Résumé Episode 1',bd=8,activebackground='blue',activeforeground="red",bg='azure',font ='Arial 11 bold italic',command=R1,overrelief=GROOVE)
                rem1.grid(row=0,column=0)

                rem2 = Button(m1, text='Résumé Episode 2',bd=8,activebackground='blue',activeforeground="red",bg='azure',font ='Arial 11 bold italic',command=R2,overrelief=GROOVE)
                rem2.grid(row=1,column=0)

                rem3 = Button(m1, text='Résumé Episode 3',bd=8,activebackground='blue',activeforeground="red",bg='azure',font ='Arial 11 bold italic',command=R3,overrelief=GROOVE)
                rem3.grid(row=2,column=0)

                rem4 = Button(m1, text='Résumé Episode 4',bd=8,activebackground='blue',activeforeground="red",bg='azure',font ='Arial 11 bold italic',command=R4,overrelief=GROOVE)
                rem4.grid(row=3,column=0)
        
                rem5 = Button(m1, text='Résumé Episode 5',bd=8,activebackground='blue',activeforeground="red",bg='azure',font ='Arial 11 bold italic',command=R5,overrelief=GROOVE)
                rem5.grid(row=4,column=0)

                rem6 = Button(m1, text='Résumé Episode 6',bd=8,activebackground='blue',activeforeground="red",bg='azure',font ='Arial 11 bold italic',command=R6,overrelief=GROOVE)
                rem6.grid(row=5,column=0)

                rem7 = Button(m1, text='RésuméEpisode 7',bd=8,activebackground='blue',activeforeground="red",bg='azure',font ='Arial 11 bold italic',command=R7,overrelief=GROOVE)
                rem7.grid(row=6,column=0)

                rem8 = Button(m1, text='Résumé Episode 8',bd=8,activebackground='blue',activeforeground="red",bg='azure',font ='Arial 11 bold italic',command=R8,overrelief=GROOVE)
                rem8.grid(row=7,column=0)

                rem9 = Button(m1, text='Résumé Episode 9',bd=8,activebackground='blue',activeforeground="red",bg='azure',font ='Arial 11 bold italic',command=R9,overrelief=GROOVE)
                rem9.grid(row=8,column=0)

                em1 = Label(m1, text='Partie 1 ', font ='Arial 11 bold italic',bg='azure')
                em1.grid(row=0,column=1)

                em2 = Label(m1, text='Partie 2 ',font ='Arial 11 bold italic',bg='azure')
                em2.grid(row=1,column=1)

                em3 = Label(m1, text='Partie 3 ',font ='Arial 11 bold italic',bg='azure')
                em3.grid(row=2,column=1)

                em4 = Label(m1, text='Partie 4 ',font ='Arial 11 bold italic',bg='azure')
                em4.grid(row=3,column=1)
        
                em5 = Label(m1, text='Partie 5 ',font ='Arial 11 bold italic',bg='azure')
                em5.grid(row=4,column=1)

                em6 = Label(m1, text='Partie 6 ',font ='Arial 11 bold italic',bg='azure')
                em6.grid(row=5,column=1)

                em7 = Label(m1, text='Partie 7 ',font ='Arial 11 bold italic',bg='azure')
                em7.grid(row=6,column=1)

                em8 = Label(m1, text='Partie 8 ',font ='Arial 11 bold italic',bg='azure')
                em8.grid(row=7,column=1)

                em9 = Label(m1, text='Partie 9 ',font ='Arial 11 bold italic',bg='azure')
                em9.grid(row=8,column=1)


                mp1 = Button(m1, bitmap='hourglass',command=pa)
                mp1.grid(row=0,column=2)

                mp2 = Button(m1, bitmap='hourglass',command=pa)
                mp2.grid(row=1,column=2)

                mp3 = Button(m1, bitmap='hourglass',command=pa)
                mp3.grid(row=2,column=2)

                mp4 = Button(m1,bitmap='hourglass',command=pa)
                mp4.grid(row=3,column=2)
                
                mp5 = Button(m1, bitmap='hourglass',command=pa)
                mp5.grid(row=4,column=2)

                mp6 = Button(m1, bitmap='hourglass',command=pa)
                mp6.grid(row=5,column=2)

                mp7 = Button(m1, bitmap='hourglass',command=pa)
                mp7.grid(row=6,column=2)

                mp8 = Button(m1, bitmap='hourglass',command=pa)
                mp8.grid(row=7,column=2)

                mp9 = Button(m1, bitmap='hourglass',command=pa)
                mp9.grid(row=8,column=2)

                R = Label(m2,text='')
                R.grid(row=1,column=0)

                mainloop()

                
            

        l2= Label(p11, text= "Sélectionnez", font="Arial 9")
        l2.grid(row=0, column=0)

        b1= Button(p11, text= "Valider",command=lcdp)
        b1.grid(row=0, column= 2)

        mainloop()

    
def s1():
    s(1)
def s2():
    s(2)
def s3():
    s(3)
def s4():
    s(4)
def s5():
    s(5)



master= Tk()
master.title('Lemon Tv')


p1=PanedWindow(master)
p1.grid(row=0,column=0)

p2=PanedWindow(master,bg='white')
p2.grid(row=1,column=0)

p3=PanedWindow(master)
p3.grid(row=1,column=1)

p4=PanedWindow(master)
p4.grid(row=0,column=1)

p9=PanedWindow(master)
p9.grid(row=2,column=0)

p10=PanedWindow(master)
p10.grid(row=3,column=0)

p11=PanedWindow(master)
p11.grid(row=4)

prix=0
img =tk.PhotoImage(file="op.png")
label=Label(p1,image=img,)
label.grid(row=0,column=3)

img1 =tk.PhotoImage(file="1.png")
b=Button(p2,image=img1,overrelief=FLAT,bd=7,bg='white',command=s1)
b.grid(row=0,column=0)

img2 =tk.PhotoImage(file="2.png")
b1=Button(p2,image=img2,overrelief=FLAT,bd=7,bg='black',command=s2)
b1.grid(row=0,column=1)

img3 =tk.PhotoImage(file="3.png")
b2=Button(p2,image=img3,overrelief=FLAT,bd=7,bg='darkred',command=s3)
b2.grid(row=0,column=2)

img4 =tk.PhotoImage(file="4.png")
b3=Button(p2,image=img4,overrelief=FLAT,bd=7,bg='navy',command=s4)
b3.grid(row=0,column=3)

img5 =tk.PhotoImage(file="5.png")
b4=Button(p3,image=img5,overrelief=FLAT,bd=7,bg='red',command=s5)
b4.grid(row=0,column=0)

b5=Button(p1,bitmap='question',command=aide,activeforeground="red",overrelief=FLAT,bd=7,bg='blue')
b5.grid(row=0,column=4)

l1= Label(p10, text='',font="Arial 11 italic")
l1.grid(row=0,column=0)

ade=Label(p4,text='')
ade.grid(row=0,column=4)

price=Button(p1,text='Afficher le panier',font="Arial 11 bold",bd=11,overrelief=GROOVE,command=pri)
price.grid(row=0,column=2)

pricelabel=Label(p1,text='',font="Arial 11 bold")
pricelabel.grid(row=0,column=0)

pricelabe=Label(p1,text='€',font="Arial 11 bold")
pricelabe.grid(row=0,column=1)

mainloop()












    































##    load = Image.open("1.png")
##    render = ImageTk.PhotoImage(load)
##    img = Label(master, image=render)
##    img.image = render
##    img.place(x=0, y=0)




