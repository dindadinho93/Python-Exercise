import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
print()
db = mysql.connector.connect(
    user=os.getenv('MYSQL_USER'),
    password=os.getenv('PASSWORD'),
    host='localhost',
    database='db1',
    auth_plugin='mysql_native_password'
)

cur = db.cursor()
cur.execute('SELECT * FROM customer')

data = cur.fetchmany(size=10)

for dt in data:
	print(dt[0], dt[1])