
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msb

def main():
    
    def dalej(event):
        
        
        def zaznacz(event):

            def zamknij(event):
                zaz.destroy()
                nowe.destroy()
                



            def tabelka(event):
                
               
                def zamko(event):
                    tabelka.destroy()
                    zaz.deiconify()
                    
              
                                
                tabelka=Toplevel(zaz)
                zaz.withdraw()    
                tabelka.attributes("-topmost", True)
                
                  
                organizm1=[[tabelki11[0][0].get()],[tabelki11[0][1].get()]]
                organizm2=[[tabelki22[0][0].get()],[tabelki22[0][1].get()]]
                

                
                for x in range(dlugosc-1):
                    for i in range(2**(x+1)):
                        organizm1.append((organizm1[i][:]))
                        organizm2.append((organizm2[i][:]))
                    
                    c=int(2**(x+2)/2)
                    
                    for i in range(c):
                        
                        organizm1[i]=organizm1[i]+[tabelki11[x+1][0].get()]
                        organizm1[i+c]=organizm1[i+c]+[tabelki11[x+1][1].get()]
                        organizm2[i]=organizm2[i]+[tabelki22[x+1][0].get()]
                        organizm2[i+c]=organizm2[i+c]+[tabelki22[x+1][1].get()]
                        
                      
                    
                unique_sweets = []
                for sweet in organizm1:
                    if sweet not in unique_sweets:
                        unique_sweets.append(sweet)
                organizm1=unique_sweets[:]

                unique_sweets = []
                for sweet in organizm2:
                    if sweet not in unique_sweets:
                        unique_sweets.append(sweet)
                organizm2=unique_sweets[:]  
                
                
                k=0
                
                org1=len(organizm1)
                org2=len(organizm2)
                for x in range(org1):
                    for i in range(len(organizm1[x])):
                        
                        organizm1[x][i]=nazwy.index(organizm1[x][i])
                        
                    k+=1    
                     
                

                k=0
                
                
                for x in range(org2):
                    for i in range(len(organizm2[x])):
                        organizm2[x][i]=nazwy.index(organizm2[x][i])
                    k+=1
                            
      

              
                organizm1.sort()
                organizm2.sort()
                
               

                tab=[]
                
                tabako=[]
                ktora=0

                for wys in range(org2):
                    for sze in range(org1):
                        A=[]
                        for x in range(dlugosc):
                           A+=[organizm1[sze][x]]+[organizm2[wys][x]]
                        
                        
                        
                        tabako.append(A)
                        tabako[ktora].sort()
                        ktora+=1
                
                y=[]
                for x in tabako:
                    for t in range(dlugosc*2):
                       y.append(nazwy[x[t]])
                    tab.append(y)
                    
                    y=[]
                
                

                

                for x in range(org1):
                    textf=''
                    for i in range(dlugosc):
                        textf+=nazwy[organizm1[x][i]]
                    Label(tabelka,text=textf,font=("a",15)).grid(row=0,column=x+1)



                for x in range(org2):
                    textb=''
                    for i in range(dlugosc):
                        textb+=nazwy[organizm2[x][i]]
                    Label(tabelka,text=textb,font=("a",15)).grid(row=x+1,column=0)
                    


                ile=[]
                co=[]
                ile2=[]
                co2=[]
                naz2=[]
                ktora=0
                for wys in range(org2):
                    for sze in range(org1):
                        Label(tabelka,text=tab[ktora],border=5,relief="groove",font=("a",15)).grid(row=wys+1,column=sze+1)
                        s=sze+2
                        w=wys+2
                        ktora+=1
                x=0
                
                while x!=(org1*org2):
                    
                    c=tab.count(tab[0])
                    naz=tab[0]
                    co.append(naz)
                    ile.append(c)
                    for v in range(c):
                        tab.remove(naz)
                    x+=c
                
                rodzaj=[]
                
                
                
                for x in tabako:
                    aq=''
                    for i in range(0,dlugosc*2,2):
                        aq+=str(x[i])
                    rodzaj.append(aq)
                    
                x=0
                
                while x!=org1*org2:
                    c=rodzaj.count(rodzaj[0])    
                    naz2=rodzaj[0]
                    co2.append(naz2)
                    ile2.append(c)
                    
                    for v in range(c):
                        rodzaj.remove(naz2)
                    x+=c
                
                
                
                
                Label(tabelka,text="Genotypy",font=("a",15)).grid(row=0,column=s) 
                Label(tabelka,text="Fenotypy",font=("a",15)).grid(row=0,column=s+1)   
                
                for x in range(len(co)):
                    aq=''
                    
                    for i in range(dlugosc*2):
                        aq+=str(co[x][i])
                    tex=aq+": "+str(ile[x]) 
                    Label(tabelka,text=tex,font=("a",15)).grid(row=x+1,column=s)   
                    
                 
                
                
                for x in range(len(co2)):
                    aq=''
                    for i in range(dlugosc):
                        aq+=(nazwy[int(co2[x][i])])
                        if i != dlugosc-1:
                            aq+=" - "
                        
                      
                    
                    tex=aq+": "+str(ile2[x]) 
                    Label(tabelka,text=tex,font=("a",15)).grid(row=x+1,column=s+1)     

                           
                        

                    
                tex=''    
                for x in tabelki11:
                    tex+=(x[0].get()+x[1].get())
                tex+=" X "
                for x in tabelki22:
                    tex+=(x[0].get()+x[1].get())

                Label(tabelka,text=tex,font=("a",20)).grid(row=w,column=1,columnspan=org1)
                tabelka.bind(des,zamko)
                tabelka.bind(ret,zamko)
                Button(tabelka,text="zamknij",command=lambda:zamko(ret)).grid()






            zaz=Toplevel(okno)
            zaz.lift()
            zaz.attributes("-topmost", True)
            tabelki1=[]
            tabelki11=[]
            tabelki2=[]
            tabelki22=[]
            nazwy=[]
            j=0


            


            for x in range(dlugosc):
                for i in range(nazwy2[x]):
                    nazwy.append(str(wejscia2[x][i].get()))
            


            

            Label(zaz,text="Organizm 1",pady=5,font=("1",12)).grid(row=0,column=0,columnspan=dlugosc*2)

            for x in range(dlugosc):
                
                for k in range(2):
                    combox11= ttk.Combobox(zaz,width=5)
                    combox11['values']=[i.get() for i in wejscia2[x]]
                    combox11['state'] = 'readonly'
                    combox11.grid(row=1,column=j)
                    combox11.set(wejscia2[x][k].get())
                    j+=1
                    tabelki1.append(combox11)
                tabelki11.append(tabelki1[:])
                tabelki1.clear()

            
           
            j=0
            Label(zaz,text="Organizm 2",pady=5,font=("1",12)).grid(row=2,column=0,columnspan=dlugosc*2)

            for x in range(dlugosc):
                
                for k in range(2):
                    combox11= ttk.Combobox(zaz,width=5)
                    combox11['values']=[i.get() for i in wejscia2[x]]
                    combox11['state'] = 'readonly'
                    combox11.grid(row=3,column=j)
                    combox11.set(wejscia2[x][k].get())
                    j+=1
                    tabelki2.append(combox11)
                tabelki22.append(tabelki2[:])
                tabelki2.clear()



            zaz.bind(ret,tabelka)
            zaz.bind(des,zamknij)
            Button(zaz,text="sprawdz",width=29,pady=5,command=lambda: tabelka(ret)).grid(row=4,column=0,columnspan=dlugosc*2)
            Button(zaz,text="zamknij",width=29,pady=5,command=lambda: zamknij(des)).grid(row=5,column=0,columnspan=dlugosc*2)
            nowe.withdraw() 
            
                
        def wroc(event):
            nowe.destroy()
            okno.deiconify()
            
        
        
        nazwy2=[]
        wejscia=[]
        wejscia2=[]
        
        j=1
        
        
        for x in range(len(nazwy)):
            nazwy2.append(int(nazwy[x].get()))
            if nazwy2[x]<1:
                msb.showwarning(title='Result',message="cos ciemno to widze")
                nazwy2.clear()
                j=2
                break
        
            
        

        
        
        if j==1:
         
            nowe=Toplevel(okno)
            nowe.lift()
            okno.withdraw()
            dlugosc=len(nazwy2)
            
            
            for x in nazwy2:
                Label(nowe,text="nazwij na gorze najwazniejsze",font=("a",20)).grid(row=j,column=0,columnspan=5)
                j+=1   
                for i in range(x):
                    var=Entry(nowe,width=4,font=("a",20),justify='center')
                    wejscia.append(var)
                    var.grid(row=j,column=0)
                    j+=1    
                wejscia2.append(wejscia[:])
                wejscia.clear()



            if dlugosc==2:
                if nazwy2[0]==2:
                    wejscia2[0][0].insert(0,"A")
                    wejscia2[0][1].insert(0,"a")
                if nazwy2[1]==2:
                    wejscia2[1][0].insert(0,"B")
                    wejscia2[1][1].insert(0,"b")
            
            nowe.bind(ret,zaznacz)
            nowe.bind(des,wroc)
            Button(nowe,command= lambda :zaznacz(ret),text="ok",font=("a",20)).grid(row=j+1,column=5)
            
            

    def callback(il):
        zmienna=il.get()
        if zmienna=='':
            tyle=1
        else:
            tyle=int(zmienna)
            if tyle>10:
                tyle=10
            elif tyle<2:
                tyle=1
        for x in elementy:
            x.destroy()
        elementy.clear()
        nazwy.clear()
        for x in range(tyle):
            tekscik="Ile alleli " + str(x+1)
            nazwy.append(IntVar(okno,2))
            a=Label(okno,text=tekscik,font=("a",20),justify='left',padx=10)
            a.grid(row=x+1,column=0)
            b=Entry(okno,textvariable=nazwy[x],width=5,font=("a",20),justify='center')
            b.grid(row=x+1,column=2)
            elementy.append(a)
            elementy.append(b)
            
        
        c=Button(okno,text="ok",command= lambda: dalej(ret),height=3,width=10)
        c.grid(row=x+2,column=1,columnspan=2)
        elementy.append(c)

    okno=Tk()
    okno.lift()
    
    ret='<Return>'
    des='<Destroy>'
    okno.eval('tk::PlaceWindow . center')
    okno.resizable(width=False, height=False)

    nazwy=[]
    elementy=[]
    

    il=StringVar(okno,2)
    tyle=2
    


    Label(okno,text="ile cech",font=("a",20),justify='left',padx=10).grid(row=0,column=0)
    il.trace("w", lambda name, index, mode, il=il: callback(il))
    Entry(okno,textvariable=il,width=5,font=("a",20),justify='center').grid(row=0,column=2)
    

    
    for x in range(tyle):
            tekscik="Ile alleli " + str(x+1)
            nazwy.append(IntVar(okno,2))
            a=Label(okno,text=tekscik,font=("a",20),justify='left',padx=10)
            a.grid(row=x+1,column=0)
            b=Entry(okno,textvariable=nazwy[x],width=5,font=("a",20),justify='center')
            b.grid(row=x+1,column=2)
            elementy.append(a)
            elementy.append(b)
    
    
    
    okno.bind(ret,dalej)
    c=Button(okno,text="ok",command= lambda: dalej(ret),height=3,width=10)
    c.grid(row=x+2,column=1,columnspan=2)
    elementy.append(c)

    
    okno.mainloop()

    
    
   

main()


