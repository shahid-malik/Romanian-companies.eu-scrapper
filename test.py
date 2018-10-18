import pymysql as MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root","romanian_companies" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("show tables")

# Fetch a single row using fetchone() method.
data = cursor.fetchall()
print (data)

# disconnect from server
db.close()
