def recursive(n):
	if(n ==0):
		print("blassssst")
	else:
		print(n)
		recursive(n-1)
		
		
def factorial(n):
	if n == 0:
		return 1
	else:
		print("n")
		print(n)
		recurse = factorial(n-1)
		print("recurse")
		print(recurse)
		result = n * recurse
		print("result")
		print(result)
		return result

no = int(input("Enter no : \n"))	
recursive(no)
print("factorial")
print(factorial(no))
	