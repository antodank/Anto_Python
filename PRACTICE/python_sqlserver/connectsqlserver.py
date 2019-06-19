import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ANKIT-PC\SQLEXPRESS;'
                      'Database=EmployeeDB;'
                      'Trusted_Connection=yes;')
#pip install pyodbc
cursor = conn.cursor()
cursor.execute('select * from [EmployeeDB].[dbo].[Employees]')

for row in cursor:
    print(row)

cursor.execute('''
                INSERT INTO [dbo].[Employees]
            ([FirstName],[LastName],[Gender],[Salary])
            VALUES
            ('Bob','Simon','Male',4520)
                ''') 
conn.commit();

cursor.execute('select * from [EmployeeDB].[dbo].[Employees]')
for row in cursor:
    print(row)

conn.close()