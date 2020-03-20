from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123123",
    database="mydata",


)
print(mydb)

sql_select_Query = "select * from data"
mycursor = mydb.cursor()
mycursor.execute(sql_select_Query)
records = mycursor.fetchall()
print("Total number of rows in Laptop is: ", mycursor.rowcount)

@app.route('/')
def index():
    return render_template('chart.html')


@app.route('/data')
def data():
    dolar = []
    for row in records:
        if row[1] == "o10":
            dolar.append(row[5])
    return jsonify({'result' : dolar})

if __name__ == '__main__':
    app.run(debug=True)
