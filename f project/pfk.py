import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",password="Khan@123",database="log")
#cur=mycon.cursor()
#cur.execute("create database log")
#str="create table yasu(Name varchar(255),Age integer(2),Gender varchar(255),City varchar(255))"
str="insert into yasu(Name,Age,Gender,City) values(%s,%s,%s,%s)"
b=("yasmin",23,"female","ctc")

cur=mycon.cursor()
cur.execute(str,b)
mycon.commit()













from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def detail():
    return render_template("index2.html")
app.run()