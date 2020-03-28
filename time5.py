from datetime import datetime
import mysql.connector


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
#  user="yourusername",
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

for c in range(0, (len(guncel_date) -1)):
    for b in range(1, (len(guncel_date) - 1)):
        if int(dolar_time[c]) - int(dolar_time[b]) >= 5:
            print(dolar_time[b], "-", dolar_time[c])
            c += 1
            break
            #mycursor.execute("""INSERT INTO ogrenci VALUES (?, ?, ?)""", dolar_time[b])
        else:
            b += 1

            break

