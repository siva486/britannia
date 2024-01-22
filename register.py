#!C:/python/python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")


Form=cgi.FieldStorage()
SName=Form.getvalue("Name")
SFlavour=Form.getvalue("Flavour")
SAddress=Form.getvalue("Address")
SContact=Form.getvalue("Contact")
SLocation=Form.getvalue("Location")
print("<br><center><h2>Thank you for Britannia online order<a href='/Britannia'><br><br>Back To Home</a>")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="britannia"
    )

mycursor=mydb.cursor()
sql="INSERT INTO customer(Name,Flavour,Address,Contact,Location)VALUES(%s,%s,%s,%s,%s)"
val=(SName,SFlavour,SAddress,SContact,SLocation)
mycursor.execute(sql,val)
mydb.commit()

ptint("</body>")
ptint("</html>")
