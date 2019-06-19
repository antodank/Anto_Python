dic1 = dict([('guido', 4127), ('jack', 4098)])
dic2 = {'jack': 5098, 'guido': 5127}

print(dic1['jack'])
print(dic2['jack'])

dic1['mike'] = 5000
for key in dic1.keys():
    print(dic1[key])

#if(dic1.has_key('mike')):
#   print("Hello Mike")

