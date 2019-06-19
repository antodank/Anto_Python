#pip install pymssql
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    import pymssql



server = r"ANKIT-PC\SQLEXPRESS"
user = "sa"
password = "admin@123"

conn = pymssql.connect(server, user, password, "EmployeeDB")
cursor = conn.cursor()

cursor.execute('select * from [EmployeeDB].[dbo].[Employees]')
row = cursor.fetchone()
while row:
    print("ID=%d, Name=%s" % (row[0], row[1]))
    row = cursor.fetchone()

conn.close()