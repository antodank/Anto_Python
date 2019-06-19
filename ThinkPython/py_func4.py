def CamelCase(str):
    finalword = ""
    for word in str.split():
        finalword = finalword + word[0].upper() + word[1:] 
    return finalword   

def CountPrime(limit):
    n= 1
    cnt = 0
    while(n <= limit):
        i = 1
        while(i < n):
            if(i != 1 and n%i == 0):
                i = n
            else:
                if(i == n -1):
                    print(f"prime = {n}")
                    cnt = cnt + 1
            i = i + 1
        n = n +1
    print(f"Total = {cnt}")


#print(CamelCase("ankit is python developer."))
#print(CountPrime(100))