#!/usr/bin/python3
import pymysql
conn = pymysql.connect(host='localhost', unix_socket='/tmp/mysql.sock', user='root', passwd='Sriram@321', db='mysql')
cur = conn.cursor()
cur.execute("SELECT Host,User FROM user")
for r in cur:
    print(r)
cur.close()
conn.close()
