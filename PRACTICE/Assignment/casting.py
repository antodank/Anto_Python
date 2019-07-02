# type cast function

#str converts its argument to a string:
print(str(5.99))

print(str(45))

#int can convert floating-point values to integers, but it doesn’t round off
print(int(6.99))
print(int('500'))

#error str cant be converted to int/float
#print(int('ankit')

print(float(10))
print(float('3.14'))

sName = 'ankittodankar'

tplName = tuple(sName)

print(tplName)

setName = set(sName)

print(setName)

strnum = '1001'
num1 = int(strnum)
print(num1)
hexnum = hex(num1)
print(hexnum)