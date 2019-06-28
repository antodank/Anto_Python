
def arithmatic():
    #liValues = ["a","b","c"]
    liValues = [2,3,4]
    for x in liValues:
        try:
            print(x**2)
        except TypeError:
            print('Arithmatic Error')

def zeroError():
    x = 5
    y = 10
    try:
        x  = x/y
    except: #ZeroDivisionError
        x = 0
        print('Error')
    print(x)

if __name__ == "__main__":
    #arithmatic()
    zeroError()