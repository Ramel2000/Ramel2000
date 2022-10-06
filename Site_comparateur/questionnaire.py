#-------Prog--Questionnaire-------

from tkinter import *
import tkinter as tk

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
            print( K[i])
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

    
img =tk.PhotoImage(file="tktt.png")   
btn = Button(master,command=bonjour,image=img,bd=7,overrelief=GROOVE) 
btn.grid(column=4, row=10)
bttn = Button(master,command=master.destroy,text='Annuler',bd=7,overrelief=GROOVE,bg='red',font='size 12 italic') 
bttn.grid(column=4, row=0)
bj=Label(p13, text="(Répondez pour voir votre / vos préférence(s) s'afficher ici)",bg ='black',font='size 13 bold italic',fg='white') 
bj.grid(column=0, row=0)
bja=Label(p13, text="",bg ='black') 
bja.grid(column=1, row=0)

master.mainloop()


