
#variable should not start with special char or num 
#variables are case sensitive
pi = 3.14
age = 25
str = ' this is to test string '

val = 'ankit'+'todankar'
val1 = 'ankit' + 10 # + cannont be used with str and int
val2 = '50'* 3

#val3 = val1 * val2   
#above statement is invalid becoz str can be operate only with int

#val4 = '55' / 5
#val5 = '55' - 10
# / and - are unsupported operands with string

print(str)
print(age)
print(pi)

print(age/2)
print(pi*2)
print(5+4*6/3-1)
print(val) 
print(val1)
print(val2)
#print(val3)
#print(val4)
#print(val5)