import sqlite3
#from tkMessageBox import  *
con=sqlite3.Connection('Database')
cur=con.cursor()
cur.execute('create table if not exists record(website Varchar(500), vulnerable Varchar(5), exploitable Varchar(5), testdate date)')


def addnewwebsite(website,vulnerable,exploitable,testdate):
    cur.execute('insert into record values(?,?,?,?)',(website,vulnerable,exploitable,testdate,))
    con.commit()
    
    #showinfo('New website', 'Record successfully added to database')

def viewdata():
    cur.execute('select * from record')
    a=cur.fetchall()
    return a
def updateexploitable(b,website):
    cur.execute('update record set exploitable =(?) where website=(?)',(b,website))
    con.commit()
    #showinfo('Alert', 'information updated into database')

def updatedate(d,website):
    cur.execute('update record set testdate =(?) where website=(?)',(d,website))
    con.commit()
    
    
