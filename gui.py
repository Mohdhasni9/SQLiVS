from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *
from SQLinjector import *
import time
import websitedata

def checkvuln(wsite,name):
    inject=[]
    global result
    for x in name:
        sqlinject=x
        inject.append(wsite.replace("FUZZ",sqlinject))
    showinfo('Wait'," Checking website for vulnerability please wait")
    result=injector(inject)
    process()

def deepXploit():
    global columns
    global version
    global curr_user
    global steal_usr
    global passwrd
    columns=detect_columns(wsite)
    version=detect_version(wsite)
    curr_user=detect_user(wsite)
    steal_usr,passwrd=steal_users(wsite)

def xploit():
    pro.destroy()
    xploy=Tk()
    showinfo('Exploit', "website is under deep Explotation wait ..!")
    xploy.geometry('1024x577')
    xploy.configure(bg='white', cursor='circle')
    pic=PhotoImage(file="softwall.gif")
    xploy.title("SQL Injection Vulnerability Scanner")
    Label(xploy,image=pic).grid(row=0,column=0,rowspan=20,columnspan=10)
    Label(xploy,text='SQL Injection Vulnerability Scanner', font='Harrington 18 bold' ).grid(row=0,column=0,columnspan=10)
    Label(xploy,text='Results:', font='Harrington 16 bold underline' ,bg='white').grid(row=2,column=0)
    Label(xploy,text='No. of columns:-', font='Harrington 14 bold underline' ,bg='white').grid(row=6,column=0)
    Label(xploy,text='Version:-', font='Harrington 14 bold underline' ,bg='white').grid(row=7,column=0)
    Label(xploy,text='Current Database User:-', font='Harrington 14 bold underline' ,bg='white').grid(row=8,column=0)
##    Label(xploy,text='Usernames & passwords:-', font='Harrington 14 bold underline' ,bg='white').grid(row=10,column=0)
    for x in columns:
        Label(xploy, text=x,font='Harrington 14 bold underline' ,bg='white').grid(row=6,column=(1+(int(columns.index(x)))))
##        xploy.mainloop()
    Label(xploy, text=version,font='Harrington 14 bold underline',bg='white').grid(row=7,column=1)
    Label(xploy, text=curr_user,font='Harrington 14 bold underline' ,bg='white').grid(row=8,column=1)
##    for x in steal_usr:
##        Label(xploy,text=x,font='Harrington 14 bold underline' ,bg='white').grid(row=10,column=(1+(int(steal_usr.index(x)))))
##        xploy.mainloop()
##    for x in passwrd:
##        Label(xploy,text=x,font='Harrington 14 bold underline' ,bg='white').grid(row=11,column=(1+(int(passwrd.index(x)))))
##        xploy.mainloop()
    xploy.mainloop()
    
    
def report():
    p1.destroy()
    global rep
    rep=Tk()
    rep.geometry('1024x577')
    rep.configure(bg='white', cursor='circle')
    pic=PhotoImage(file="softwall.gif")
    rep.title("SQL Injection Vulnerability Scanner")
    Label(rep,image=pic).grid(row=0,column=0,rowspan=10,columnspan=10)
    Label(rep,text='SQL Injection Vulnerability Scanner', font='Harrington 18 bold' ).grid(row=0,column=0,columnspan=10)
    Button(rep, text="back", bg='white', command=repback).grid(row=1, column=8)
    Label(rep,text='Report:', font='Harrington 16 bold underline' ,bg='white').grid(row=2,column=0)
    rep.mainloop()

def repback():
    rep.destroy()
    Home()
def process():
    global pro
    p1.destroy()
    pro=Tk()
    pro.geometry('1024x577')
    pro.configure(bg='white', cursor='circle')
    pic=PhotoImage(file="softwall.gif")
    Label(pro,image=pic).grid(row=0,column=0,rowspan=20,columnspan=10)
    pro.title("SQL Injection Vulnerability Scanner")
    Label(pro,text='SQL Injection Vulnerability Scanner', font='Harrington 18 bold' ).grid(row=1,column=0,columnspan=10)
    Label(pro,text='Processing:', font='Harrington 16 bold underline' ,bg='white').grid(row=2,column=0,sticky='W')
    Label(pro,text='Testing errors:-', font='Harrington 14 bold ' ,bg='white').grid(row=3,column=0,sticky='W')
    '''def testres(wsite,name):
        inject=[]
        for z in name:
                y=(wsite.replace("FUZZ",z))
                Label(pro,text='' , bg='white').grid(row=4,column=0,sticky='EWNS')
                Label(pro,text=y, bg='white').grid(row=4,column=0,sticky='EW')
                break'''
    global i
    i=int(0)
    for x in result:
            i=int(i+1)
            Label(pro,text=x,font='Harrington 12 bold',bg='white').grid(row=5+i,column=0,sticky='NS')
    if (len(result) != 0):
        showinfo('Results','Website is  vulnerable to sql injection')
        Button(pro,text='Exploit',bg='white',command=lambda:[deepXploit(),xploit(),]).grid(row=10,column=5,sticky='W')
    else :
        showinfo('Results','Website is not vulnerable to sql injection')
    pro.mainloop()


def checkres():
        if not result:
            showinfo('Results',"Not vulnerable")

            
def Home():
    global p1
    p1=Tk()
    global s
    p1.geometry('1024x577')
    p1.configure(bg='white', cursor='circle')
    pic=PhotoImage(file="softwall.gif")
    Label(p1,image=pic).grid(row=0,column=0,rowspan=10,columnspan=10)
    p1.title("SQL Injection Vulnerability Scanner")
    Label(p1,text='SQL Injection Vulnerability Scanner', font='Harrington 18 bold' ).grid(row=0,column=0,columnspan=10)
    Label(p1,text='Website:', font='Harrington 14 bold' ,bg='white').grid(row=2,column=0)
    s=Entry(p1,bg='LightCyan4', cursor='dot')
    s.grid(row=2,column=1,columnspan=5,sticky='EW')
    Label(p1,text='Injection file select:', font='Harrington 14 bold' ,bg='white').grid(row=8,column=0)
    def fileselect():
        injectionfile=askopenfilename(title = "Select injection  dictionary file",filetypes = (("text files","*.txt"),))
        f = open(injectionfile, "r")
        global name
        name = f.read().splitlines()
        print(name)

    def webget():
        global wsite
        wsite=str(s.get()+"FUZZ")
        print(wsite)
        
    Button(p1, text='select file', command=fileselect, bg='white', cursor='dot').grid(row=8, column=1)
    Button(p1, text="Check",bg='white',command=lambda:[webget(),checkvuln(wsite,name),]).grid(row=6,column=8, sticky='EWNS')
    p1.mainloop()
Home()


