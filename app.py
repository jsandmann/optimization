from flask import Flask, render_template, redirect, request
import json
import mysql

app = Flask(__name__)

import mysql.connector
mydb = mysql.connector.connect(
  host="optimized-living.mysql.database.azure.com",
  user="jsandmann@optimized-living",
  passwd="Ocarinaoftime0!"
)
mycursor = mydb.cursor()

@app.route('/') # home page
def welcome():
    return render_template('home.html')

@app.route('/workouts') # show the set data
def workouts():
    mycursor.execute("SELECT * FROM personaldata.setdata")
    myresult = mycursor.fetchall()
    return render_template('workouts.html', data = myresult)

@app.route('/newset') # go to the enter exercise form
def newset():
    mycursor.execute("SELECT * FROM personaldata.exercise")
    myresult = mycursor.fetchall()
    return render_template('newset.html', data = myresult)

@app.route('/logset', methods=['POST']) # enter the form data into the database
def logset():
    date = request.form['date']
    exercise = request.form['exercise']
    reps = request.form['reps']
    weight = request.form['weight']
    print(date)
    list(string.split(",")
    print(reps)
    print(weight)
    return 'Success!'