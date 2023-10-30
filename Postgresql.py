import psycopg2
from dotenv import load_dotenv
import os
import matplotlib

load_dotenv()


conn = psycopg2.connect(
    database="postgres",
    host="localhost",
    user=os.getenv('PGSQL_USER'),
    password=os.getenv('PASSWORD'),
    port="5432"
)

cur = conn.cursor()
cur.execute("SELECT * FROM customer")

data = cur.fetchall()

cur.close()
conn.close()

for dt in data:
	print(dt[0], dt[1])
