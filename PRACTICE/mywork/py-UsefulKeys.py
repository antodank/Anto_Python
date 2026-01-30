
list1 = list(range(0, 11) )
print(list1)

for i in list1:
    print(i)

# above list will print from 0 to 10

# Third parameter is step size!
# step size just means how big of a jump/leap/step you 
list2 = list(range(0, 101,10) )
for j in list2:
    print(j)

#enumerate - there is no need to creating and updating counter
for k,letter in enumerate('abcde'):
    print(f"At index {i} the letter is {letter}")

list3  = list(enumerate('abcde'))
for l in list3:
    print(l) 


mylist1 = [5,6,7,8,9]
mylist2 = ['a','b','c','d','e']

list4 = list(zip(mylist1,mylist2))
for m in list4:
    print(m)

res = 'x' in ['x','y','z']
print(res)

res = 'a' in ['x','y','z']
print(res)

print(min(mylist1))
print(max(mylist1))

inp = input("Enter Something:")
print(inp)