#pip install pandas
import pandas as pd

df = pd.read_csv(r'D:\PRACS\python\Anto_Python\PRACTICE\files\employee.csv')

newdf = pd.DataFrame(df, columns= ['Name','Salary'])
print (newdf)

for line in newdf:
    print(line)
