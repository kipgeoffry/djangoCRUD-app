#create the application db nemanager 
import  mysql.connector
mydb = mysql.connector.connect(
  host="192.168.5.43",
  port ="3360",
  user="root",
  password="pw123456",
  

)
kgcursor = mydb.cursor()
kgcursor.execute('CREATE DATABASE nemanager')

print('Database created successfully')