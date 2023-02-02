import sqlite3 
conn = sqlite3.connect('mybase.db')
cur = conn.cursor()

req="select prénom from client "
req1="select id from client where id = 2014"
cur.execute(req)
res=cur.fetchall()
cur.execute(req1)
res1=cur.fetchall()
res2=list(cur)
if res1 == [] :
        print("il n'y a pas des valeurs ")
else : 
    for row in res1 :
        print(row[0])
    

cur.close()


conn.commit()
conn.close()
