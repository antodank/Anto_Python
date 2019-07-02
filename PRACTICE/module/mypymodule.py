def printEven(x):
    return [num for num in range(x)[1:] if num%2==0]

def printOdd(x):
    return [num for num in range(1,x + 1,2)]

#a[start:stop]  # items start through stop-1
#a[start:]      # items start through the rest of the array
#a[:stop]       # items from the beginning through stop-1
#a[:]           # a copy of the whole array

def printLanguage():
    languages = ["C", "C++", "Perl", "Python"] 
    return [str for str in languages]
