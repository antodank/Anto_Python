#pip install pandas
import pandas as pd

df = pd.read_csv(r'D:\PRACS\python\PRACTICE\files\employee.csv')
print(df)

newdf = pd.DataFrame(df, columns= ['Name','Salary'])
print (newdf)
