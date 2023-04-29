#! C:/Users/Ajay kumar.J/AppData/Local/Programs/Python/Python39/python.exe
import cgi

print("content-type:text/html\n\r")
form=cgi.FieldStorage()
uname=form.getvalue("name")
fname=form.getvalue("fname")
des=form.getvalue("des")
a="record"
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="Ajay@2002",database="mylearn")
mycursor=mydb.cursor()
sql="""insert into fun (uname,fname,des) values (%s, %s,%s );"""
val = (""+uname+"", ""+fname+"", ""+des+"")
mycursor.execute(sql, val)
mydb.commit()
print("%s submitted" %a)