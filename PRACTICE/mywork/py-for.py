list1 = [1,2,3,4,5,6,7,8,9,10]

for i in list1:
    print(i)

for num in list1:
    if num % 2 == 0:
        print(f"{num} Even")
    else:
        print(f"{num} Odd")

list_sum = 0 
for num in list1:
    list_sum += num

print(list_sum)

#string
for letter in 'This is a string.':
    print(letter)

#dictonary
d = {'k1':1,'k2':2,'k3':3}

for item,val in d:
    print(item)
    print(val)


# for only key d.keys() and for only values d.values()