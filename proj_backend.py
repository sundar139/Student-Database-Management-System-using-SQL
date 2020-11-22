import mysql.connector
#import proj_frontend

def StudentData():
        con = mysql.connector.connect(host="localhost",user="root",password="Pass1Word2",database="Project")
        cur=con.cursor()
       
        cur.execute("CREATE TABLE IF NOT EXISTS toc(id integer primary key AUTO_INCREMENT,StdID text,Firstname text,Surname text,DoB text,Age text,Gender text,Address text,Mobile text)")
        con.commit()
        con.close()              
def AddStdRec(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile):
        con=con = mysql.connector.connect(host="localhost",user="root",password="Pass1Word2")
        cur=con.cursor()
        cur.execute("use Project")
        cur.execute("INSERT INTO toc VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)",(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
        con.commit()
        con.close() 
def ViewData():
        con=con = mysql.connector.connect(host="localhost",user="root",password="Pass1Word2")
        cur=con.cursor()
        cur.execute("use Project")
        cur.execute("select * from toc")
        row=cur.fetchall()
        con.close()       
        return row
def DeleteRec(id):
        con=con = mysql.connector.connect(host="localhost",user="root",password="Pass1Word2")
        cur=con.cursor()
        cur.execute("use Project")
        cur.execute("DELETE FROM toc WHERE id=%s",(id,))
        con.commit()
        con.close()         
def SearchData(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile):
        con=con = mysql.connector.connect(host="localhost",user="root",password="Pass1Word2")
        cur=con.cursor()
        cur.execute("use Project")
        cur.execute("SELECT * FROM toc WHERE StdID=%s or Firstname=%s or Surname=%s or DoB=%s or Age=%s or Gender=%s or Address=%s or Mobile=%s",(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
        rows=cur.fetchall()
        con.close()        
        return rows
def DataUpdate(id,StdID="",Firstname="",Surname="",DoB="",Age="",Gender="",Address="",Mobile=""):
        con = mysql.connector.connect(host="localhost",user="root",password="Pass1Word2")
        cur=con.cursor()
        cur.execute("use Project")
        cur.execute("UPDATE toc SET StdID=%s,Firstname=%s,Surname=%s,DoB=%s,Age=%s,Gender=%s,Address=%s,Mobile=%s WHERE id=%s",(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
        con.commit()
        con.close()
def ViewNames():
        con=con = mysql.connector.connect(host="localhost",user="root",password="Pass1Word2")
        cur=con.cursor()
        cur.execute("use Project")
        cur.execute("SELECT * FROM toc WHERE Firstname LIKE 'a%';")
        row=cur.fetchall()
        con.close()       
        return row
def ViewMobile():
        con=con = mysql.connector.connect(host="localhost",user="root",password="Pass1Word2")
        cur=con.cursor()
        cur.execute("use Project")
        cur.execute("SELECT * FROM toc WHERE Mobile LIKE '+1%';")
        row=cur.fetchall()
        con.close()       
        return row
def ViewAddress():
        con=con = mysql.connector.connect(host="localhost",user="root",password="Pass1Word2")
        cur=con.cursor()
        cur.execute("use Project")
        cur.execute("SELECT * FROM toc WHERE Address LIKE 'd%';")
        row=cur.fetchall()
        con.close()       
        return row
def ViewDoB():
        con=con = mysql.connector.connect(host="localhost",user="root",password="Pass1Word2")
        cur=con.cursor()
        cur.execute("use Project")
        cur.execute("SELECT * FROM toc WHERE DoB LIKE '%2000';")
        row=cur.fetchall()
        con.close()       
        return row
def ViewGender():
        con=con = mysql.connector.connect(host="localhost",user="root",password="Pass1Word2")
        cur=con.cursor()
        cur.execute("use Project")
        cur.execute("SELECT * FROM toc WHERE Gender LIKE 'f%';")
        row=cur.fetchall()
        con.close()       
        return row
def ViewID():
        con=con = mysql.connector.connect(host="localhost",user="root",password="Pass1Word2")
        cur=con.cursor()
        cur.execute("use Project")
        cur.execute("SELECT * FROM toc WHERE StdID LIKE '2k18%';")
        row=cur.fetchall()
        con.close()       
        return row


