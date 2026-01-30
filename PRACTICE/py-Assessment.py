#print out words that start with 's' or 'S':

st = 'Hi Sam, Print only the words that start with s in this sentence'

for str in st.split():
    if(str[0] == 's' or str[0] == 'S'):
        print(str)

list1 = list(range(2, 11,2) )
print(list1)

list2 = list(range(3, 51,3) )
print(list2)

list3 = [x for x in range(1,51) if x%5 == 0]
print(list3)

#fizbuzz 1 to 100
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)