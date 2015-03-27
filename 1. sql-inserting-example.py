import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def tableCreate():
    c.execute("CREATE TABLE stuffToPlot(ID INT, unix REAL, datestamp TEXT, keyword TEXT, value REAL)")


def dataEntry():
    c.execute("INSERT INTO stuffToPlot VALUES(1, 1365952181,'2013-04-14 10:09:41','Python Sentiment',5)")
    c.execute("INSERT INTO stuffToPlot VALUES(2, 1365952257,'2013-04-14 10:10:57','Python Sentiment',6)")
    c.execute("INSERT INTO stuffToPlot VALUES(3, 1365952264,'2013-04-14 10:11:04','Python Sentiment',4)")
    conn.commit()
