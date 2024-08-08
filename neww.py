import pymysql
db_connection=pymysql.connect(
    host="localhost",
    user="root",
    password="123",
    database="qb"
)
my_db=db_connection.cursor()

print("Connected successfully")
