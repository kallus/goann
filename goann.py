import MySQLdb as sql
import os

connection = sql.connect(host = "localhost", user = "root", db = "goann")
cursor = connection.cursor(sql.cursors.DictCursor)

while True:

  #create
  cursor.execute("SELECT count(*) AS count FROM player")
  pcount = cursor.fetchone()["count"]
  if pcount < 1000:
    os.system('create')
    continue

  #play

  #kill
