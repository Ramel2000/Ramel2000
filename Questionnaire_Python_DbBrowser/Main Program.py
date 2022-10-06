from PIL import Image, ImageTk
from tkinter import *
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import sqlite3

global img1
global nom
global prenom
global Age
global S
global A
global W
global Q
global O
global k
global d
global E4
global E5
global E6
global E1
global E2
global E3
global s1
global s2
global s3
global s4
global s5
global s6
global s7
global s8
global a1
global a2
global a3
global a4
global a5
global a6
global a7
global a8
global L1
global L2
global L3
global Ll1
global Ll2
global Ll3

k=0
d=0
LARGE_FONT = ("Verdana", 12)
window=tk.Tk()
window.title("MainPage")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.configure(background="white")
window.resizable(width=False, height=False)

window.geometry("650x650+"+str(int(window.winfo_screenwidth()/2)-300)+"+"+str(int(window.winfo_screenheight()/2)-300))

 

window.minsize(650,650)

window.maxsize(650,650)


img1=PhotoImage(file="logo.png")

img2=PhotoImage(file="im2.png")









def retour():
    global nom
    global prenom
    global Age
    global S
    global A
    global W
    global Q
    global O
    global k
    global d
    global img1
    global E4
    global E5
    global E6
    global E1
    global E2
    global E3
    global L1
    global L2
    global L3
    global Ll1
    global Ll2
    global Ll3
    nom=''
    prenom=''
    email=''
    
    if d%2!=0:
        d=d+1
        for widget in window.winfo_children():
                widget.destroy()        
        label=Label(window, image=img1, bg="white").grid(row= 0, columnspan = 2, pady = 20)
            
        Ti=Label(window, text ="Sustainable Development Solutions",fg='green', font="times 20 bold",bg='white')
        Ti.place(x=0, y=0, relwidth=1)

        L1=Label(window, text="Name :", font="times 12 bold",bg='white')
        L1.grid(row=1,column=0, pady = 1, padx = 20)

        L2=Label(window, text="Last name :", font="times 12 bold",bg='white')
        L2.grid(row=2,column=0, pady = 1)
        L3=Label(window, text="Age :",font="times 12 bold",bg='white')
        L3.grid(row=3,column=0, pady = 1)
        L4=Button(window, command=stat,text="statistiques")
        L4.grid(row=4, pady = 25)

        E1=Entry(window)
        E1.grid(row=1,column=1, pady = 1, padx = 80)
        E2=Entry(window)
        E2.grid(row=2, column=1, pady = 1)
        E3=Entry(window)
        E3.grid(row=3, column=1, pady = 1)

        B1=Button(window,text='continuer',command=continuer)
        B1.grid(row=4, column=1)
        window.mainloop()
        
    elif d%2==0:
        d=d+1
        for widget in window.winfo_children():
                widget.destroy()        
        label=Label(window, image=img1, bg="white").grid(row= 0, columnspan = 2, pady = 20)
            
        Ti=Label(window, text ="Sustainable Development Solutions",fg='green', font="times 20 bold",bg='white')
        Ti.place(x=0, y=0, relwidth=1)

        Ll1=Label(window, text="Name :", font="times 12 bold",bg='white')
        Ll1.grid(row=1,column=0, pady = 1, padx = 20)

        Ll2=Label(window, text="Last name :", font="times 12 bold",bg='white')
        Ll2.grid(row=2,column=0, pady = 1)
        Ll3=Label(window, text="Age :",font="times 12 bold",bg='white')
        Ll3.grid(row=3,column=0, pady = 1)
        L4=Button(window, text='statistiques',command=stat)
        L4.grid(row=4, pady = 25)

        E4=Entry(window)
        E4.grid(row=1,column=1, pady = 1, padx = 80)
        E5=Entry(window)
        E5.grid(row=2, column=1, pady = 1)
        E6=Entry(window)
        E6.grid(row=3, column=1, pady = 1)

        B1=Button(window,text='continuer',command=continuer)
        B1.grid(row=4, column=1)
        window.mainloop()



def continuer():

    t=0
    global k
    global d
    global img1
    global nom
    global prenom
    global age
    global S
    global A
    global W
    global Q
    global O
    global E4
    global E5
    global E6
    global E1
    global E2
    global E3
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global s7
    global s8
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    global a8
    global L1
    global L2
    global L3
    global Ll1
    global Ll2
    global Ll3
    if k%2==0:
            
            if E1.get()==''or E2.get()==''or E3.get()=='':
                    t=0
                    if E1.get()=='':
                            L1.config(bg='red')
                    elif E1.get()!='':
                            L1.config(bg='white')
                    if E2.get()=='':
                            L2.config(bg='red')
                    elif E2.get()!='':
                            L2.config(bg='white')
                    if E3.get()=='':
                            L3.config(bg='red')
                    elif E3.get()!='':
                            L3.config(bg='white')
            elif E1.get()!=''or E2.get()!=''or E3.get()!='':
                    k=k+1
                    t=1
            
            
            nom=E1.get()
            prenom=E2.get()
            age=E3.get()
            print(nom,prenom,age)
        
            
    elif k%2!=0:
            t=1
            if E4.get()==''or E5.get()==''or E6.get()=='':
                    t=0
                    if E4.get()=='':
                            Ll1.config(bg='red')
                    elif E4.get()!='':
                            Ll1.config(bg='white')
                    if E5.get()=='':
                            Ll2.config(bg='red')
                    elif E5.get()!='':
                            Ll2.config(bg='white')
                    if E6.get()=='':
                            Ll3.config(bg='red')
                    elif E6.get()!='':
                            Ll3.config(bg='white')
            elif E4.get()!=''or E5.get()!=''or E6.get()!='':
                    t=1
                    k=k+1
            
            
            nom=E4.get()
            prenom=E5.get()
            age=E6.get()
            print(nom,prenom,age)

    if t==1:
            for widget in window.winfo_children():
                    widget.destroy()
            
                    
            p1=PanedWindow(window,bg='white')
            p1.grid(row=0,column=0)

            p2=PanedWindow(window,bg='white')
            p2.grid(row=1,column=0)

            p3=PanedWindow(window,bg='white')
            p3.grid(row=2,column=0)

            p4=PanedWindow(window,bg='white')
            p4.grid(row=3,column=0)
            
            p5=PanedWindow(window,bg='white')
            p5.grid(row=4,column=0)

            p6=PanedWindow(window,bg='white')
            p6.grid(row=5,column=0)

            p7=PanedWindow(window,bg='white')
            p7.grid(row=6,column=0)

            p8=PanedWindow(window,bg='white')
            p8.grid(row=7,column=0)

            p9=PanedWindow(window,bg='white')
            p9.grid(row=8,column=0)

            p10=PanedWindow(window,bg='white')
            p10.grid(row=9,column=0)

            p11=PanedWindow(window,bg='white')
            p11.grid(row=10,column=0)

            p12=PanedWindow(window,bg='white')
            p12.grid(row=11,column=0)

            p13=PanedWindow(window,bg='white')
            p13.grid(row=12,column=0)

            p14=PanedWindow(window,bg='white')
            p14.grid(row=13,column=0)

            p15=PanedWindow(window,bg='white')
            p15.grid(row=14,column=0)

            p16=PanedWindow(window,bg='white')
            p16.grid(row=15,column=0)

            p17=PanedWindow(window,bg='white')
            p17.grid(row=16,column=0)

            p18=PanedWindow(window,bg='white')
            p18.grid(row=17,column=0)

            p19=PanedWindow(window,bg='white')
            p19.grid(row=18,column=0)

            p20=PanedWindow(window,bg='white')
            p20.grid(row=19,column=0)

            p21=PanedWindow(window,bg='white')
            p21.grid(row=21,column=0)

            p22=PanedWindow(window,bg='white')
            p22.grid(row=22,column=0)

            p23=PanedWindow(window,bg='white')
            p23.grid(row=23,column=0)

            p24=PanedWindow(window,bg='white')
            p24.grid(row=24,column=0)

            p25=PanedWindow(window,bg='white')
            p25.grid(row=25,column=0)

            p26=PanedWindow(window,bg='white')
            p26.grid(row=26,column=0)

            p27=PanedWindow(window,bg='white')
            p27.grid(row=27,column=0)
        #-----------------------------------------------------------------------------------------
            label1=Label(p1,text='Prenez-vous les transports en commun ?',bg='white',font='size 13',pady=9,fg='green')
            s1 = StringVar()
            rad1 = Radiobutton(p2,text='Oui',activeforeground="gold",overrelief=SUNKEN,variable=s1,value='TCO',bg ='white',font='size 12')
            rad2 = Radiobutton(p2,text='Non',activeforeground="gold",overrelief=SUNKEN,variable=s1,value='TCN',bg ='white',font='size 12')
        #-----------------------------------------------------------------------------------------
            label2=Label(p3,text='Prenez-vous souvent le train ?',bg='white',font='size 13',pady=9,fg='green')
            s2 = StringVar()
            rad3 = Radiobutton(p4,text='Oui',activeforeground="gold",overrelief=SUNKEN,variable=s2,value='TO',bg ='white',font='size 12')
            rad4 = Radiobutton(p4,text='Non',activeforeground="gold",overrelief=SUNKEN,variable=s2,value='TN',bg ='white',font='size 12')
        #-----------------------------------------------------------------------------------------
            label3=Label(p5,text="Vous arrive-t-il de prendre l'avion ?",bg='white',font='size 13',pady=9,fg='green')
            s3 = StringVar()
            rad5 = Radiobutton(p6,text='Oui',activeforeground="gold",overrelief=SUNKEN,variable=s3,value='AO',bg ='white',font='size 12')
            rad6 = Radiobutton(p6,text='Non',activeforeground="gold",overrelief=SUNKEN,variable=s3,value='AN',bg ='white',font='size 12')
        #-----------------------------------------------------------------------------------------
            label4=Label(p7,text='Avez-vous une voiture ?',bg='white',font='size 13',pady=9,fg='green')
            s4 = StringVar()
            rad7 = Radiobutton(p8,text='Voiture (essence)',activeforeground="gold",overrelief=SUNKEN,variable=s4,value='ess',bg ='white',font='size 12')
            rad8 = Radiobutton(p8,text='Voiture (gasoil)',activeforeground="gold",overrelief=SUNKEN,variable=s4,value='Gas',bg ='white',font='size 12')
            radd8 = Radiobutton(p8,text='Non',activeforeground="gold",overrelief=SUNKEN,variable=s4,value='VN',bg ='white',font='size 12')
        #-----------------------------------------------------------------------------------------
            label6=Label(p11,text='Etes-vous végétarien, vegan ou aucun des deux ?',bg='white',font='size 13',pady=9,fg='green')
            s5 = StringVar()
            rad12 = Radiobutton(p12,text='Végétarien',activeforeground="gold",overrelief=SUNKEN,variable=s5,value='Végé',bg ='white',font='size 12')
            rad13 = Radiobutton(p12,text='Végan',activeforeground="gold",overrelief=SUNKEN,variable=s5,value='Véga',bg ='white',font='size 12')
            rad14 = Radiobutton(p12,text='Aucun des deux',activeforeground="gold",overrelief=SUNKEN,value='NVégéNVéga',variable=s5,bg ='white',font='size 12')
        #-----------------------------------------------------------------------------------------
            label8=Label(p15,text='Allez-vous souvent faire du shopping ?',bg='white',font='size 13',pady=9,fg='green')
            s6 = StringVar()
            rad17 = Radiobutton(p16,text='Oui',activeforeground="gold",overrelief=SUNKEN,variable=s6,value='SO',bg ='white',font='size 12')
            rad18 = Radiobutton(p16,text='Non',activeforeground="gold",overrelief=SUNKEN,variable=s6,value='SN',bg ='white',font='size 12')
        #-----------------------------------------------------------------------------------------
            label10=Label(p17,text='A quelle fréquence vous lavez-vous ?',bg='white',font='size 13',pady=9,fg='green')
            s7 = StringVar()
            rad23 = Radiobutton(p18,text='1 à 2 fois/semaine',activeforeground="gold",overrelief=SUNKEN,variable=s7,value='78',bg ='white',font='size 12')
            rad24 = Radiobutton(p18,text='1 fois /2jours',activeforeground="gold",overrelief=SUNKEN,variable=s7,value='183',bg ='white',font='size 12')
            rad25 = Radiobutton(p18,text='1/jour',activeforeground="gold",overrelief=SUNKEN,variable=s7,value='365',bg ='white',font='size 12')
        #-----------------------------------------------------------------------------------------
            label11=Label(p20,text="Buvez-vous de l'eau en bouteille ?",bg='white',font='size 13',pady=9,fg='green')
            s8 = StringVar()
            rad26 = Radiobutton(p21,text='Oui',activeforeground="gold",overrelief=SUNKEN,variable=s8,value='EO',bg ='white',font='size 12')
            rad27 = Radiobutton(p21,text='Non',activeforeground="gold",overrelief=SUNKEN,variable=s8,value='EN',bg ='white',font='size 12')
        #-----------------------------------------------------------------------------------------
            label1.grid(row=0)

            rad1.grid(column=0, row=1)
            rad2.grid(column=1, row=1)


            label2.grid(row=0)

            rad3.grid(column=0, row=1)
            rad4.grid(column=1, row=1)


            label3.grid(row=0)

            rad5.grid(column=0, row=1)
            rad6.grid(column=1, row=1)


            label4.grid(row=0)

            rad7.grid(column=0, row=3)
            rad8.grid(column=1, row=3)
            radd8.grid(column=2, row=3)

            label6.grid(row=0)

            rad12.grid(column=0, row=5)
            rad13.grid(column=1, row=5)
            rad14.grid(column=2, row=5)



            label8.grid(row=0)

            rad17.grid(column=0, row=5)
            rad18.grid(column=1, row=5)

            label10.grid(row=0)

            rad23.grid(column=0, row=5)
            rad24.grid(column=1, row=5)
            rad25.grid(column=2, row=5)

            label11.grid(row=0)

            rad26.grid(column=0, row=5)
            rad27.grid(column=1, row=5)

            
            def lola1():
                    print(s1.get(),a1)
                    print(s2.get(),a2)
                    print(s3.get(),a3)
                    print(s4.get(),a4)
                    print(s5.get(),a5)
                    print(s6.get(),a6)
                    print(s7.get(),a7)
                    print(s8.get(),a8)
            def lola():
                    global d
                    global s1
                    global s2
                    global s3
                    global s4
                    global s5
                    global s6
                    global s7
                    global s8
                    global a1
                    global a2
                    global a3
                    global a4
                    global a5
                    global a6
                    global a7
                    global a8
                    #-----------------------------------------------------------------------------------------
                    if s1.get() == 'TCO':
                            a1= 'normal'       
                    elif s1.get()=='TCN':
                            a1='disabled'
                    else:
                            a1=0       
                    #-----------------------------------------------------------------------------------------
                    if s2.get()== 'TO':
                            a2= 'normal'
                    elif s2.get()=='TN':
                            a2='disabled'
                    else:
                            a2=0
                    #-----------------------------------------------------------------------------------------
                    if s3.get()== 'AO':
                            a3= 'normal'
                    elif s3.get()=='AN':
                            a3='disabled'
                    else:
                            a3=0
                    #-----------------------------------------------------------------------------------------
                    if s4.get()== 'ess':
                            a4= 'normal'
                            aa4='disabled'
                    elif s4.get()=='Gas':
                            a4='disabled'
                            aa4='normal'
                    elif s4.get()=='VN':
                            a4='disabled'
                            aa4='disabled'
                    else :
                            a4=0
                            aa4=0
                    #-----------------------------------------------------------------------------------------
                    if s5.get()== 'Végé':
                            a5= 'disabled'
                            aa5='normal'
                    elif s5.get()=='Véga':
                            aa5='disabled'
                            a5='disabled'
                    elif s5.get()=='NVégéNVéga':
                            a5= 'normal'
                            aa5='normal'
                    else:
                            a5=0
                    #-----------------------------------------------------------------------------------------
                    if s6.get()=='SO':
                            a6='763 '
                    elif s6.get()=='SN':
                            a6='381 '
                    else:         
                            a6=0
                    #-----------------------------------------------------------------------------------------
                    if s7.get()=='78':
                            a7=78
                    elif s7.get()=='183':
                            a7=182.5
                    elif s7.get()=='365':
                            a7=365
                    else:
                            a7=0
                    #-----------------------------------------------------------------------------------------
                    if s8.get()=='EO':
                            a8='normal'
                    elif s8.get()=='EN':
                            a8='disabled'
                    else:
                            a8=0

                    if a1==0 or a2==0 or a3==0 or a4==0 or aa4==0 or a5==0 or a6==0 or a7==0 or a8==0 :
                            if a1==0:
                                    label1.config(fg='red')
                            elif a1!=0:
                                    label1.config(fg='green')
                            if a2==0:
                                    label2.config(fg='red')
                            elif a2!=0:
                                    label2.config(fg='green')
                            if a3==0:
                                    label3.config(fg='red')
                            elif a3!=0:
                                    label3.config(fg='green')
                            if a4==0:
                                    label4.config(fg='red')
                            elif a4!=0:
                                    label4.config(fg='green')
                            if a5==0:
                                    label6.config(fg='red')
                            elif a5!=0:
                                    label6.config(fg='green')
                            if a6==0:
                                    label8.config(fg='red')
                            elif a6!=0:
                                    label8.config(fg='green')
                            if a7==0:
                                    label10.config(fg='red')
                            elif a7!=0:
                                    label10.config(fg='green')
                            if a8==0:
                                    label11.config(fg='red')
                            elif a8!=0:
                                    label11.config(fg='green')
                    else:
                            for widget in window.winfo_children():
                                    widget.destroy()
                                    
                    
                            p1=PanedWindow(window,bg='white')
                            p1.grid(row=0,column=0)

                            p2=PanedWindow(window,bg='white')
                            p2.grid(row=1,column=0)

                            p3=PanedWindow(window,bg='white')
                            p3.grid(row=2,column=0)

                            p4=PanedWindow(window,bg='white')
                            p4.grid(row=3,column=0)

                            p5=PanedWindow(window,bg='white')
                            p5.grid(row=4,column=0)

                            p6=PanedWindow(window,bg='white')
                            p6.grid(row=5,column=0)

                            p7=PanedWindow(window,bg='white')
                            p7.grid(row=6,column=0)

                            p8=PanedWindow(window,bg='white')
                            p8.grid(row=7,column=0)

                            p9=PanedWindow(window,bg='white')
                            p9.grid(row=8,column=0)

                            p10=PanedWindow(window,bg='white')
                            p10.grid(row=9,column=0)

                            p11=PanedWindow(window,bg='white')
                            p11.grid(row=10,column=0)

                            p12=PanedWindow(window,bg='white')
                            p12.grid(row=11,column=0)

                            p13=PanedWindow(window,bg='white')
                            p13.grid(row=12,column=0)

                            p14=PanedWindow(window,bg='white')
                            p14.grid(row=13,column=0)

                            p15=PanedWindow(window,bg='white')
                            p15.grid(row=14,column=0)

                            p16=PanedWindow(window,bg='white')
                            p16.grid(row=15,column=0)

                            p17=PanedWindow(window,bg='white')
                            p17.grid(row=16,column=0)

                            p18=PanedWindow(window,bg='white')
                            p18.grid(row=17,column=0)
                            
                            p19=PanedWindow(window,bg='white')
                            p19.grid(row=18,column=0)

                            #-----------------------------------------------------------------------------------------
                            #-----------------------------------------------------------------------------------------
                            l1=Label(p1,text='Approximation quotidienne du nombre de km que vous faites en transports en commun',font='Arial 13',pady=11,bg='white',fg='green')
                            l1.grid(row=0,column=0)

                            q1=Label(p2,text='Bus',font='Arial 12',bg='white')
                            q1.grid(row=0,column=0)

                            e1=Entry(p2,state=a1)
                            e1.grid(row=0,column=1)

                            qq1=Label(p2,text='RER/metro',font='Arial 12',bg='white')
                            qq1.grid(row=0,column=2)

                            ee1=Entry(p2,state=a1)
                            ee1.grid(row=0,column=3)

                            
                            #-----------------------------------------------------------------------------------------
                            #-----------------------------------------------------------------------------------------
                            l2=Label(p3,text='Rentrez une approximation du nombre de km que vous faites en train',font='Arial 13',pady=11,bg='white',fg='green')
                            l2.grid(row=0,column=0)

                            q2=Label(p4,text='Train',font='Arial 12',bg='white')
                            q2.grid(row=0,column=0)

                            e2=Entry(p4,state=a2)
                            e2.grid(row=0,column=1)
                            #-----------------------------------------------------------------------------------------
                            #-----------------------------------------------------------------------------------------
                            l3=Label(p5,text='Rentrez une approximation du nombre de km que vous faites en avion',font='Arial 13',pady=11,bg='white',fg='green')
                            l3.grid(row=0,column=0)

                            q3=Label(p6,text='Avion',font='Arial 12',bg='white')
                            q3.grid(row=0,column=0)

                            e3=Entry(p6,state=a3)
                            e3.grid(row=0,column=1)
                            #-----------------------------------------------------------------------------------------
                            #-----------------------------------------------------------------------------------------
                            l4=Label(p7,text='Rentrez une approximation du nombre de km que vous faites en voiture',font='Arial 13',pady=11,bg='white',fg='green')
                            l4.grid(row=0,column=0)

                            q4=Label(p8,text='Essence',font='Arial 12',bg='white')
                            q4.grid(row=0,column=0)

                            e4=Entry(p8,state=a4)
                            e4.grid(row=0,column=1)

                            qq4=Label(p8,text='Gasoil',font='Arial 12',bg='white')
                            qq4.grid(row=0,column=2)

                            ee4=Entry(p8,state=aa4)
                            ee4.grid(row=0,column=3)
                            #-----------------------------------------------------------------------------------------
                            #-----------------------------------------------------------------------------------------
                            l5=Label(p9,text='Rentrez la quantité de viande en gramme que vous mangez quotidiennement',font='Arial 13',pady=11,bg='white',fg='green')
                            l5.grid(row=0,column=0)

                            q5=Label(p10,text="quantité en 'g'",font='Arial 12',bg='white')
                            q5.grid(row=0,column=0)

                            e5=Entry(p10,state=a5)
                            e5.grid(row=0,column=1)
                            #-----------------------------------------------------------------------------------------
                            #-----------------------------------------------------------------------------------------
                            label7=Label(p11,text='Consommez-vous les produits suivants ?',bg='white',font='Arial 13',pady=11,fg='green')
                            label7.grid(row=0)

                            o4 = IntVar()
                            o5 = IntVar()
                            
                            rad15 = Checkbutton(p12,state =aa5, text='Lait de vache',activeforeground="gold",overrelief=SUNKEN,variable=o4,bg ='white',font='size 12')
                            rad16 = Checkbutton(p12,state =aa5,text='Oeufs',activeforeground="gold",overrelief=SUNKEN,variable=o5,bg ='white',font='size 12')
                            rad15.grid(column=0, row=5)
                            rad16.grid(column=1, row=5)
                            #-----------------------------------------------------------------------------------------
                            #-----------------------------------------------------------------------------------------

                            l8=Label(p15,text="Combien de litres d'eau minérale (en bouteille) buvez-vous quotidiennement ?",font='Arial 13',pady=11,bg='white',fg='green')
                            l8.grid(row=0,column=0)

                            q8=Label(p16,text="quantité en 'L'",font='Arial 12',bg='white')
                            q8.grid(row=0,column=0)

                            e8=Entry(p16,state=a8)
                            e8.grid(row=0,column=1)
                            #-----------------------------------------------------------------------------------------
                            #-----------------------------------------------------------------------------------------

                            label9=Label(p17,text='Avez-vous les technologies suivantes ?',bg='white',font='Arial 13',pady=11,fg='green')
                            o6 = IntVar()
                            o7 = IntVar()
                            o8 = IntVar()
                            o9 = IntVar()

                            rad19 = Checkbutton(p18,text='Téléphone',activeforeground="gold",overrelief=SUNKEN,variable=o6,bg='white',font='size 12')
                            rad20 = Checkbutton(p18,text='Télévision',activeforeground="gold",overrelief=SUNKEN,variable=o7,bg='white',font='size 12')
                            rad21 = Checkbutton(p18,text='Ordinateur',activeforeground="gold",overrelief=SUNKEN,variable=o8,bg='white',font='size 12')
                            rad22 = Checkbutton(p18,text='Tablette',activeforeground="gold",overrelief=SUNKEN,variable=o9,bg='white',font='size 12')

                            label9.grid(row=0)

                            rad19.grid(column=0, row=5)
                            rad20.grid(column=1, row=5)
                            rad21.grid(column=2, row=5)
                            rad22.grid(column=3, row=5)
                            #-----------------------------------------------------------------------------------------
                            

                            def onéla():
                                PV01=e1.get()
                                PV001=ee1.get()
                                PV02=e2.get()
                                PV03=e3.get()
                                PV04=e4.get()
                                PV004=ee4.get()
                                PV05=e5.get()
                                PV07=int(s7.get())
                                PV08=e8.get()
                                PV06=o4.get()
                                PV006=o5.get()
                                PV09=o6.get()
                                PV009=o7.get()
                                PV0009=o8.get()
                                PV00009=o9.get()
                                PV10 = int(a6)
                                if PV01 == '' or PV001 =='' or PV02 =='' or PV03 =='' or PV04 =='' or PV004 =='' or PV05 =='' or PV07 =='' or PV08 =='':
                                    if PV01 == '':
                                        PV01 = 0
                                    if PV001 == '':
                                        PV001 = 0
                                    if PV02 == '':
                                        PV02 = 0
                                    if PV03 == '':
                                        PV03 = 0
                                    if PV04 == '':
                                        PV04 = 0
                                    if PV004 == '':
                                        PV004 = 0
                                    if PV05 == '':
                                        PV05 = 0
                                    if PV07 == '':
                                        PV07 = 0
                                    if PV08 == '':
                                        PV08 = 0
                                PV01 = round ((float(PV01)*55*365*(10**-6)),5)
                                PV001 = round((float(PV001) * 4 * 365 * (10**-6)),5)
                                PV02 = round((float( PV02) * (86*(10**-6)) * 365),5)
                                PV03 = round((float(PV03) * (285*(10**-6)) * 365),5)
                                PV04 = round((float(PV04) * (186*(10**-6)) * 365),5)
                                PV004 = round((float(PV004) * (165*(10**-6)) * 365),5)
                                PV05 = round((float(PV05) * (4.67*(10**-3) * 365)/50),5)
                                PV07 = round((float(PV07) * 210 *(10**-6)),5)
                                PV08 = round((float(PV08 )* 121 *(10**-6) *365),5)
                                PV06 = round((float(PV06)*3*(0.94*(10**-3))*52),5)
                                PV006 = round((float(PV006)*3*(1.72*(10**-3))*52),5)
                                PV09 = round((float(PV09) *20*(10**-3)),5)
                                PV009 = round((float(PV009) *400*(10**-6)),5)
                                PV0009 = round((float(PV0009) *45*(10**-3)),5)
                                PV00009 = round((float(PV00009) *25*(10**-3)),5)
                                PV10 = round((float(PV10) * (10**-3)),5)
                                Total = round((PV01 + PV001 + PV02 + PV03 + PV04 + PV004 + PV05 + PV06 + PV006 + PV07 + PV08 + PV09 + PV009 + PV0009 + PV00009 + PV10),3)

                                arb = int((Total/(25*(10**-3))))

                                arbeco = arb*3


                                print(PV09,PV009,PV0009)


                                global nom
                                global prenom
                                global age
                                global S
                                global A
                                global W
                                global Q
                                global O
                                global img1
                                        

                                connexion = sqlite3.connect("GP21.db")
                                curseur = connexion.cursor()
                                curseur.execute("INSERT INTO Test_progra_3 (nom,prenom,age,Bus,Rer_metro,Train,Avion,Gasoil,Essence,viande,Lait,oeufs,douche,eau,Téléphone,Télévision,Ordinateur,Tablette,Shopping,Total)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(nom,prenom,age,PV01, PV001, PV02, PV03, PV04, PV004, PV05, PV06, PV006, PV07, PV08, PV09, PV009, PV0009, PV00009,PV10,Total))
               
		
                                connexion.commit()
                                connexion.close()
                                print("enregistrement reussi")

                                
                                for widget in window.winfo_children():
                                    widget.destroy()

                                p1=PanedWindow(window,bg='white')
                                p1.grid(row=0,column=0)
    
                                p2=PanedWindow(window,bg='white')
                                p2.grid(row=1,column=0)
    
                                p3=PanedWindow(window,bg='white')
                                p3.grid(row=2,column=0)
    
                                p4=PanedWindow(window,bg='white')
                                p4.grid(row=3,column=0)
    
                                p5=PanedWindow(window,bg='white')
                                p5.grid(row=4,column=0)
    
                                p6=PanedWindow(window,bg='white')
                                p6.grid(row=5,column=0)
    
                                p7=PanedWindow(window,bg='white')
                                p7.grid(row=6,column=0)
    
                                p8=PanedWindow(window,bg='white')
                                p8.grid(row=7,column=0)


                                L1=Label(p1, text="Votre bilan carbone annuel est de : ",bg='white',fg='green',font=LARGE_FON)
                                L1.grid(row=0,column=0, pady = 10)
                                
                                L2=Label(p1, text= Total,bg='white',fg='green',font=LARGE_FON)
                                L2.grid(row=0,column=1, pady = 10)
                                
                                L3=Label(p1, text="Tonnes",bg='white',fg='green',font=LARGE_FON)
                                L3.grid(row=0,column=2, pady = 10)
                                
                                L4=Label(p2, text="Cela équivaut à devoir planter :",bg='white',fg='green',font=LARGE_FONT)
                                L4.grid(row=1,column=0, pady = 10)

                                L5=Label(p2, text=arb ,bg='white',font=LARGE_FONT,fg='green')
                                L5.grid(row=1,column=1, pady = 10)

                                L6=Label(p2, text="arbres" ,bg='white',fg='green',font=LARGE_FONT)
                                L6.grid(row=1,column=2, pady = 10)

                                L7=Label(p3, text="(pour absorber votre bilan carbone annuel)" ,bg='white',fg='green',font=LARGE_FONT)
                                L7.grid(row=2, pady = 10)

                                L8=Label(p4, text= "Pour un prix de :" ,bg='white',font=LARGE_FONT,fg='green')
                                L8.grid(row=3,column=0, pady = 10)

                                L9=Label(p4, text= arbeco ,bg='white',font=LARGE_FONT,fg='green')
                                L9.grid(row=3,column=1, pady = 10)

                                L10=Label(p4, text= "€" ,bg='white',fg='green',font=LARGE_FONT)
                                L10.grid(row=3,column=2, pady = 10)

                                L11=Label(window, image=img2 ,bg='white',fg='green',font=LARGE_FONT)
                                L11.grid(row=4,column=0, pady = 10)

                                
                                    
                                                                                



                                    
                                
                            #-----------------------------------------------------------------------------------------
                            
                            btttn =Button(p19,command=retour,text="retour",bd=7,overrelief=GROOVE,bg='cyan')
                            btttn.grid(column=2,row=0)
                            bttttn =Button(p19,command=onéla,text="Confirmer",bd=7,overrelief=GROOVE,bg='green')
                            bttttn.grid(column=3,row=0)



    

            btn = Button(p27,command=lola,text="Confirmer",bd=7,overrelief=GROOVE,bg='green') 
            btn.grid(column=2, row=0)
            bttn = Button(p27,command=window.destroy,text='Annuler',bd=7,overrelief=GROOVE,bg='red',font='size 10 italic') 
            bttn.grid(column=0, row=0)
            
            B1=Button(p27,text='retour',command=retour,bd=7,font='size 10 italic',overrelief=GROOVE,bg='cyan')
            B1.grid(row=0, column=1)          
        




LARGE_FONT = ("Verdana", 12)        

    
label=Label(window, image=img1, bg="white")
label.grid(row= 0, columnspan = 2, pady = 20)    

        
Ti=Label(window, text ="Sustainable Development Solutions",fg='green', font="times 20 bold",bg='white')
Ti.place(x=0, y=0, relwidth=1,relheigh=0.25)

L1=Label(window, text="Name :", font="times 12 bold",bg='white')
L1.grid(row=1,column=0, pady = 1, padx = 20)

L2=Label(window, text="Last name :", font="times 12 bold",bg='white')
L2.grid(row=2,column=0, pady = 1)
L3=Label(window, text="Age :",font="times 12 bold",bg='white')
L3.grid(row=3,column=0, pady = 1)


E1=Entry(window)
E1.grid(row=1,column=1, pady = 1, padx = 80)
E2=Entry(window)
E2.grid(row=2, column=1, pady = 1)
E3=Entry(window)
E3.grid(row=3, column=1, pady = 1)

B1=Button(window,text='continuer',command=continuer)
B1.grid(row=4, column=1)

def stat():
    global nom
    global prenom
    global Age
    global S
    global A
    global W
    global Q
    global O
    global k
    global d
    global img1
    global E4
    global E5
    global E6
    global E1
    global E2
    global E3
    global L1
    global L2
    global L3
    global Ll1
    global Ll2
    global Ll3
    

    def stat1():

        connexion = sqlite3.connect("GP21.db")
        curseur = connexion.cursor()
        result = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Train != ? ",("0"))
        connexion.commit
        Result=curseur.fetchone()
        T=int(Result[0])
        print(Result[0])
        print(T)
        
        resultat = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Train = ? ",("0"))
        connexion.commit
        Resultat=curseur.fetchone()
        Nt=int(Resultat[0])
        print(Resultat[0])
        print(Nt)
        connexion.close
            
        labels = 'Train', 'Non Train'
        sizes = [T , Nt]
        colors = ['yellowgreen', 'gold']
        explode = (0.1, 0.3)

        plt.pie(sizes, labels=labels,explode=explode, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=90)

        plt.title("Pourcentage de personnes prenant le train")

        plt.axis('equal')
        plt.savefig('PieChart01.png')

        plt.show()

    def stat2():

        connexion = sqlite3.connect("GP21.db")
        curseur = connexion.cursor()
        result = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Avion != ? ",("0"))
        connexion.commit
        Result=curseur.fetchone()
        A=int(Result[0])
        print(Result[0])
        print(A)
        
        resultat = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Avion = ? ",("0"))
        connexion.commit
        Resultat=curseur.fetchone()
        Na=int(Resultat[0])
        print(Resultat[0])
        print(Na)
        connexion.close
            
        labels = 'Avion', 'Non Avion'
        sizes = [A , Na]
        colors = ['yellow', 'red']
        explode = (0.1, 0.3)

        plt.pie(sizes, labels=labels,explode=explode, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=90)

        plt.title("Pourcentage de personnes prenant l'avion")

        plt.axis('equal')
        plt.savefig('PieChart02.png')
        plt.show()

    def stat3():
        
        connexion = sqlite3.connect("GP21.db")
        curseur = connexion.cursor()
        result = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Lait != ? ",("0"))
        connexion.commit
        Result=curseur.fetchone()
        L=int(Result[0])
        print(Result[0])

        
        resultat = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Lait = ? ",("0"))
        connexion.commit
        Resultat=curseur.fetchone()
        Nl=int(Resultat[0])
        print(Resultat[0])

        connexion.close
            
        labels = 'Lait', 'Non Lait'
        sizes = [L , Nl]
        colors = ['orange', 'pink']
        explode = (0.1, 0.3)

        plt.pie(sizes, labels=labels,explode=explode, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=90)

        plt.title("Pourcentage de personnes buvant du lait ou non")

        plt.axis('equal')
        plt.savefig('PieChart03.png')
        plt.show()

    def stat4():
        
        connexion = sqlite3.connect("GP21.db")
        curseur = connexion.cursor()
        result = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Rer_metro != ? ",("0"))
        connexion.commit
        Result=curseur.fetchone()
        Rm=int(Result[0])
        print(Result[0])
        print(Rm)
        
        resultat = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Rer_metro = ? ",("0"))
        connexion.commit
        Resultat=curseur.fetchone()
        Nrm=int(Resultat[0])
        print(Resultat[0])
        print(Nrm)
        connexion.close
            
        labels = 'Rer_métro', 'Non Rer_métro'
        sizes = [Rm , Nrm]
        colors = ['blue', 'purple']
        explode = (0.1, 0.3)

        plt.pie(sizes, labels=labels,explode=explode, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=90)

        plt.title("Pourcentage de personnes prenant le RER ou le métro")

        plt.axis('equal')
        plt.savefig('PieChart04.png')
        plt.show()

    def stat5():
        
        connexion = sqlite3.connect("GP21.db")
        curseur = connexion.cursor()
        result = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE eau != ? ",("0"))
        connexion.commit
        Result=curseur.fetchone()
        Rm=int(Result[0])
        print(Result[0])
        print(Rm)
        
        resultat = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE eau = ? ",("0"))
        connexion.commit
        Resultat=curseur.fetchone()
        Nrm=int(Resultat[0])
        print(Resultat[0])
        print(Nrm)
        connexion.close
            
        labels = 'eau en bouteille', 'eau du robinet'
        sizes = [Rm , Nrm]
        colors = ['blue', 'orange']
        explode = (0.1, 0.3)

        plt.pie(sizes, labels=labels,explode=explode, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=90)

        plt.title("Pourcentage de personnes buvant de l'eau du robinet")

        plt.axis('equal')
        plt.savefig('PieChart05.png')
        plt.show()

    def stat6():
        
        connexion = sqlite3.connect("GP21.db")
        curseur = connexion.cursor()
        result = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Télévision != ? ",("0"))
        connexion.commit
        Result=curseur.fetchone()
        Rm=int(Result[0])
        print(Result[0])
        print(Rm)
        
        resultat = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Télévision = ? ",("0"))
        connexion.commit
        Resultat=curseur.fetchone()
        Nrm=int(Resultat[0])
        print(Resultat[0])
        print(Nrm)
        connexion.close
            
        labels = 'Télévision', 'Non Télévision'
        sizes = [Rm , Nrm]
        colors = ['blue', 'purple']
        explode = (0.1, 0.3)

        plt.pie(sizes, labels=labels,explode=explode, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=90)

        plt.title("Pourcentage de personnes ayant une télévision")

        plt.axis('equal')
        plt.savefig('PieChart06.png')
        plt.show()
        
    def stat7():
        
        connexion = sqlite3.connect("GP21.db")
        curseur = connexion.cursor()
        result = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Téléphone != ? ",("0"))
        connexion.commit
        Result=curseur.fetchone()
        Rm=int(Result[0])
        print(Result[0])
        print(Rm)
        
        resultat = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Téléphone = ? ",("0"))
        connexion.commit
        Resultat=curseur.fetchone()
        Nrm=int(Resultat[0])
        print(Resultat[0])
        print(Nrm)
        connexion.close
            
        labels = 'Téléphone', 'Non Téléphone'
        sizes = [Rm , Nrm]
        colors = ['red', 'purple']
        explode = (0.1, 0.3)

        plt.pie(sizes, labels=labels,explode=explode, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=90)

        plt.title("Pourcentage de personnes ayant une téléphone")

        plt.axis('equal')
        plt.savefig('PieChart07.png')
        plt.show()

    def stat8():
        
        connexion = sqlite3.connect("GP21.db")
        curseur = connexion.cursor()
        result = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Tablette != ? ",("0"))
        connexion.commit
        Result=curseur.fetchone()
        Rm=int(Result[0])
        print(Result[0])
        print(Rm)
        
        resultat = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Tablette = ? ",("0"))
        connexion.commit
        Resultat=curseur.fetchone()
        Nrm=int(Resultat[0])
        print(Resultat[0])
        print(Nrm)
        connexion.close
            
        labels = 'Tablette', 'Non Tablette'
        sizes = [Rm , Nrm]
        colors = ['red', 'orange']
        explode = (0.1, 0.3)

        plt.pie(sizes, labels=labels,explode=explode, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=90)

        plt.title("Pourcentage de personnes ayant une tablette")

        plt.axis('equal')
        plt.savefig('PieChart08.png')
        plt.show()

    def stat9():
        
        connexion = sqlite3.connect("GP21.db")
        curseur = connexion.cursor()
        result = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Ordinateur != ? ",("0"))
        connexion.commit
        Result=curseur.fetchone()
        Rm=int(Result[0])
        print(Result[0])
        print(Rm)
        
        resultat = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Ordinateur = ? ",("0"))
        connexion.commit
        Resultat=curseur.fetchone()
        Nrm=int(Resultat[0])
        print(Resultat[0])
        print(Nrm)
        connexion.close
            
        labels = 'Ordinateur', 'Non Ordinateur'
        sizes = [Rm , Nrm]
        colors = ['red', 'purple']
        explode = (0.1, 0.3)

        plt.pie(sizes, labels=labels,explode=explode, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=90)

        plt.title("Pourcentage de personnes ayant un ordinateur")

        plt.axis('equal')
        plt.savefig('PieChart09.png')
        plt.show()

    def stat10():
        
        connexion = sqlite3.connect("GP21.db")
        curseur = connexion.cursor()
        result = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE oeufs != ? ",("0"))
        connexion.commit
        Result=curseur.fetchone()
        Rm=int(Result[0])
        print(Result[0])
        print(Rm)
        
        resultat = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE oeufs = ? ",("0"))
        connexion.commit
        Resultat=curseur.fetchone()
        Nrm=int(Resultat[0])
        print(Resultat[0])
        print(Nrm)
        connexion.close
            
        labels = 'oeufs', 'Non oeufs'
        sizes = [Rm , Nrm]
        colors = ['red', 'purple']
        explode = (0.1, 0.3)

        plt.pie(sizes, labels=labels,explode=explode, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=90)

        plt.title("Pourcentage de personnes consomant des oeufs")

        plt.axis('equal')
        plt.savefig('PieChart10.png')
        plt.show()

    def stat11():
        
        connexion = sqlite3.connect("GP21.db")
        curseur = connexion.cursor()
        result = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE viande != ? ",("0"))
        connexion.commit
        Result=curseur.fetchone()
        Rm=int(Result[0])
        print(Result[0])
        print(Rm)
        
        resultat = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE viande = ? ",("0"))
        connexion.commit
        Resultat=curseur.fetchone()
        Nrm=int(Resultat[0])
        print(Resultat[0])
        print(Nrm)
        connexion.close
            
        labels = 'viande', 'Non viande'
        sizes = [Rm , Nrm]
        colors = ['red', 'orange']
        explode = (0.1, 0.3)

        plt.pie(sizes, labels=labels,explode=explode, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=90)

        plt.title("Pourcentage de personnes consomant de la viande")

        plt.axis('equal')
        plt.savefig('PieChart11.png')
        plt.show()

    def stat12():
        
        connexion = sqlite3.connect("GP21.db")
        curseur = connexion.cursor()
        result = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Essence != ? ",("0"))
        connexion.commit
        Result=curseur.fetchone()
        Rm=int(Result[0])
        print(Result[0])
        print(Rm)
        
        resultat = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Essence = ? ",("0"))
        connexion.commit
        Resultat=curseur.fetchone()
        Nrm=int(Resultat[0])
        print(Resultat[0])
        print(Nrm)
        connexion.close
            
        labels = 'Essence', 'Non Essence'
        sizes = [Rm , Nrm]
        colors = ['red', 'blue']
        explode = (0.1, 0.3)

        plt.pie(sizes, labels=labels,explode=explode, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=90)

        plt.title("Pourcentage de personnes consomant de l'essence")

        plt.axis('equal')
        plt.savefig('PieChart12.png')
        plt.show()

    def stat13():
        
        connexion = sqlite3.connect("GP21.db")
        curseur = connexion.cursor()
        result = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Gasoil != ? ",("0"))
        connexion.commit
        Result=curseur.fetchone()
        Rm=int(Result[0])
        print(Result[0])
        print(Rm)
        
        resultat = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Gasoil = ? ",("0"))
        connexion.commit
        Resultat=curseur.fetchone()
        Nrm=int(Resultat[0])
        print(Resultat[0])
        print(Nrm)
        connexion.close
            
        labels = 'Gasoil', 'Non Gasoil'
        sizes = [Rm , Nrm]
        colors = ['blue', 'orange']
        explode = (0.1, 0.3)

        plt.pie(sizes, labels=labels,explode=explode, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=90)

        plt.title("Pourcentage de personnes consomant du gasoil")

        plt.axis('equal')
        plt.savefig('PieChart13.png')
        plt.show()

    def stat14():
        
        connexion = sqlite3.connect("GP21.db")
        curseur = connexion.cursor()
        result = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Bus != ? ",("0"))
        connexion.commit
        Result=curseur.fetchone()
        Rm=int(Result[0])
        print(Result[0])
        print(Rm)
        
        resultat = curseur.execute("SELECT COUNT ( * ) FROM Test_progra_3 WHERE Bus = ? ",("0"))
        connexion.commit
        Resultat=curseur.fetchone()
        Nrm=int(Resultat[0])
        print(Resultat[0])
        print(Nrm)
        connexion.close
            
        labels = 'Bus', 'Non Bus'
        sizes = [Rm , Nrm]
        colors = ['green', 'red']
        explode = (0.1, 0.3)

        plt.pie(sizes, labels=labels,explode=explode, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=90)

        plt.title("Pourcentage de personnes prenant le bus")

        plt.axis('equal')
        plt.savefig('PieChart14.png')
        plt.show()





    d=d+1   
        
    for widget in window.winfo_children():
        widget.destroy()

    B1 =Button(window,command=stat1,text="statistiques concernant le train",bd=5,overrelief=GROOVE,padx=800,font=LARGE_FONT)
    B1.grid(row=0,pady=4)

    B2 =Button(window,command=stat2,text="statistiques concernant l'avion",bd=5,overrelief=GROOVE,padx=800,font=LARGE_FONT)
    B2.grid(row=1,pady=4)

    B3 =Button(window,command=stat3,text="statistiques concernant le lait",bd=5,overrelief=GROOVE,padx=800,font=LARGE_FONT)
    B3.grid(row=2,pady=4)

    B4 =Button(window,command=stat4,text="statistiques concernant le rer et le métro",bd=5,overrelief=GROOVE,padx=800,font=LARGE_FONT)
    B4.grid(row=3,pady=4)

    B5 =Button(window,command=stat5,text="statistiques concernant l'eau",bd=5,overrelief=GROOVE,padx=800,font=LARGE_FONT)
    B5.grid(row=4,pady=4)

    B6 =Button(window,command=stat6,text="statistiques concernant la télévision",bd=5,overrelief=GROOVE,padx=800,font=LARGE_FONT)
    B6.grid(row=5,pady=4)

    B7 =Button(window,command=stat7,text="statistiques concernant le téléphone",bd=5,overrelief=GROOVE,padx=800,font=LARGE_FONT)
    B7.grid(row=6,pady=4)

    B8 =Button(window,command=stat8,text="statistiques concernant les tablettes",bd=5,overrelief=GROOVE,padx=800,font=LARGE_FONT)
    B8.grid(row=7,pady=5)

    B9 =Button(window,command=stat9,text="statistiques concernant les ordinateurs",bd=5,overrelief=GROOVE,padx=800,font=LARGE_FONT)
    B9.grid(row=8,pady=5)

    B10 =Button(window,command=stat10,text="statistiques concernant les oeufs",bd=5,overrelief=GROOVE,padx=800,font=LARGE_FONT)
    B10.grid(row=9,pady=5)

    B11 =Button(window,command=stat11,text="statistiques concernant la viande",bd=5,overrelief=GROOVE,padx=800,font=LARGE_FONT)
    B11.grid(row=10,pady=5)

    B12 =Button(window,command=stat12,text="statistiques concernant l'essence",bd=5,overrelief=GROOVE,padx=800,font=LARGE_FONT)
    B12.grid(row=11,pady=5)

    B13 =Button(window,command=stat13,text="statistiques concernant le gasoil",bd=5,overrelief=GROOVE,padx=800,font=LARGE_FONT)
    B13.grid(row=12,pady=5)

    B14 =Button(window,command=stat14,text="statistiques concernant le bus",bd=5,overrelief=GROOVE,padx=800,font=LARGE_FONT)
    B14.grid(row=13,pady=5)

    B15 =Button(window,command=retour,text="retour",bd=5,overrelief=GROOVE,bg='cyan')
    B15.grid(row=14,pady=5)
                                    

    

    

    

    

    
    
                               
tttn =Button(window,command=stat,text="statistiques",bd=5,overrelief=GROOVE)
tttn.grid(row=4, pady = 25)

LARGE_FONT = ("Verdana", 12)

LARGE_FON = ("Verdana bold", 15)


window.mainloop()

