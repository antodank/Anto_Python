def writeFile():
    try:
        f = open('testfile','w')
        f.write('Test write this')
    except IOError:
        # This will only check for an IOError exception and then execute this print statement
        print("Error: Could not find file or read data")
    else:
        print("Content written successfully")
        f.close()

def writeFileNew():
    try:
        f = open('testfile','r')
        f.write('Test write this')
    except IOError:
        # This will only check for an IOError exception and then execute this print statement
        print("Error: Could not find file or read data")
    else:
        print("Content written successfully")
        f.close()

def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))
            break
        except:
            print("Looks like you did not enter an integer!")
            continue
        finally:
            print("Finally, I executed!")
    
    print(val)

if __name__ == "__main__":
    #writefile()
    #writeFileNew()
    askint()
