import math

val1 = math.sqrt(36)

val2 = math.exp(math.log(5))

print(val1)
print(val2)


#user define func
def printmysong():
	print("my heart will go on")
	print("right now na na na na")
	
def calArea(shape,radius):
	if shape == 'square':
		area = radius * radius
	elif shape == 'circle':
		area = (math.pi * radius * radius) / 2
	else:
		area = "Invalid argument"
	print(area)

#function defination begins with def keyword and ends with :
#statements starts with TAB or four spaces is consider as function body 	
#empty line is used to indicated function end
	
# nested func
def repeatsong():
	printmysong()

printmysong()
#repeatsong()
calArea('circle',5)


