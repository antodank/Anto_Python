#list are mutable array
a1 = [99, "happy birthday", ["ankit", "raj", "simi"]]
print(a1[1])
print(a1[2][1])

a2 = range(5,10)
for x in a2:
    print(x)

a3 = [91,92,93,94,95]
a3.reverse()
a3.append(80)
a3.sort() 

for x in a3:
    print(x) 