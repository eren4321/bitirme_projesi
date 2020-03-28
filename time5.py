from datetime import datetime
import mysql.connector

#txt file düzenleme
file = open("Output.txt", "r", encoding="utf-8")
dolar_time = []
dolar_price = []
for i in file:
    fields = i.split(",")
    dolar_price.append(fields[0])
    dolar_time.append(int(fields[1]))
print(len(dolar_time))


#database/tablo olusturma

#mydb = mysql.connector.connect(
 # host="localhost",
 # user="yourusername",
 # passwd="yourpassword",
 # database="mydatabase"
#)

#mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE IF NOT EXISTS fivesec (id INT AUTO_INCREMENT PRIMARY KEY, price float(255), time datetime(255))")

#(eger tablo varsa) mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#date çevirme
guncel_date = []
for a in dolar_time:
    timestamp = int(a)
    dt_object = datetime.fromtimestamp(timestamp / 1000)
    guncel_date.append(dt_object)

print(len(guncel_date))
b = 1
c = 0

while c <= len(dolar_time):
    while b <= len(dolar_time):
        if int(dolar_time[c]) - int(dolar_time[b]) >= 5:
            print(dolar_time[b], "-", dolar_time[c])
            c += 1
            #mycursor.execute("""INSERT INTO ogrenci VALUES (?, ?)""", dolar_time[b])
        else:
            b += 1




