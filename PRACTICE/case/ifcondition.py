x = int(input("Please enter an integer: "))
if x < 0:
    x = -1
    print("Sign is Minus")
else if x == 0:
    print("Sign is Zero")
else if x > 0:
    print("Sign is Plus")
else:
    print("Should never see that")