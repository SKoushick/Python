import pymysql

db_connection = pymysql.connect(
  host="localhost",
  user="root",
  password="123",
  database=""
)
my_database = db_connection.cursor()
print("connected successfully")




##Insert
####
sql_statement = "INSERT INTO staff (sno,name,age) values(%s,%s,%s)"
values = ("1","Naveen","25")
my_database.execute(sql_statement,values)
db_connection.commit()

sql_statement = "INSERT INTO staff (sno,name,age) values(%s,%s,%s)"
values = ("2","kumar","22")
my_database.execute(sql_statement,values)
db_connection.commit()

sql_statement = "INSERT INTO staff (sno,name,age) values(%s,%s,%s)"
values = ("3","Dinseh","23")
my_database.execute(sql_statement,values)
db_connection.commit()


##Update

##sql_statement = "UPDATE may SET place='trichy' where no=2"
##my_database.execute(sql_statement)
##db_connection.commit()




##Read



##sql_statement = "SELECT * FROM may"
##my_database.execute(sql_statement)
##output = my_database.fetchall()
##for x in output:
##  print(x)


##
##
######Delete
##sql_statement = "DELETE FROM may where place='trichy'"
##my_database.execute(sql_statement)
##db_connection.commit()
##print("Row(s) deleted successfully!!!!")






##
##import pymysql
##mysqldb=pymysql.connect(host="localhost",user="root",password="123",database="clg")   
##mycursor=mysqldb.cursor()
##mycursor.execute("create table database (roll INT, name VARCHAR(255), marks INT)")  
##mysqldb.close()

  
