#!/usr/bin/python3
import pymysql
conn = pymysql.connect(host='localhost', unix_socket='/tmp/mysql.sock', user='root', passwd='your_password', db='mysql')
cur = conn.cursor()
cur.execute("SELECT Host,User FROM user")
for r in cur:
    print(r)
cur.close()
conn.close()

#if you see ConnectionRefusedError: [Errno 111] Connection refused, follow the below steps
#[root@sriram mysql]# cd /tmp/
#[root@sriram tmp]# ln -s /var/lib/mysql/mysql.sock mysql.sock
