'''import csv'''
import pandas as pd
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    import pymssql

''' def main():
    with open(r'D:\PRACS\python\Anto_Python\PRACTICE\files\Clients.csv', 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    for line in your_list:
        print(line[0]) '''

def main():
    server = r"ANKIT-PC\SQLEXPRESS"
    user = "sa"
    password = "admin@123"

    conn = pymssql.connect(server, user, password, "dbSample")
    cursor = conn.cursor()
    df = pd.read_csv(r'D:\PRACS\python\Anto_Python\PRACTICE\files\Clients.csv',header=None)
    df[4].fillna("0", inplace = True)
    cursor.execute("delete from tblClients")
    conn.commit()
    for index, row in df.iterrows():
        if row[0] != "ClientName":
            query = "insert into tblClients (ClientName,Country,Product,Purchase,Price) values ('%s','%s','%s',%s,%s)" % (row[0],row[1],row[2],row[3],row[4])
            print(query)
            cursor.execute(query)
            conn.commit()
            print("row added")
    conn.close()

if __name__ == "__main__":
    main()

    
