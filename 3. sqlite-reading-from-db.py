import sqlite3
import time
import datetime

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()
sql = "SELECT * FROM stuffToPlot WHERE keyword =? AND source =?"

wordUsed = 'Python Sentiment'
sourceVariable = 'twitter'

def readData():
    for row in c.execute(sql, [(wordUsed), (sourceVariable)]):
        print str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    

readData()
