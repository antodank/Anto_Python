
def ask(prompt, retries=3, complaint='Yes/no?'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'): 
            print ('thanks')
            return True
        if ok in ('n', 'no'):
            print ('bye') 
            return False
        
        retries -= 1
        if retries = 0: 
            raise IOError
            print (complaint)

ask ("Continue (y/n)?")