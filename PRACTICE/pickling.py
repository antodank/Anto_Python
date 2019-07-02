import pickle 

def storeData(): 
    Omkar = {'key' : 'A1', 'name' : 'Ankit Todankar',  
    'age' : 25, 'pay' : 40000} 
    Jagdish = {'key' : 'A2', 'name' : 'Viraj Todankar', 
    'age' : 22, 'pay' : 50000} 
  
    # database 
    db = {} 
    db['A1'] = Omkar 
    db['A2'] = Jagdish 
      
    # Its important to use binary mode 
    dbfile = open('examplePickle', 'ab') 
      
    # source, destination 
    pickle.dump(db, dbfile)                      
    dbfile.close() 

def loadData(): 
    # for reading also binary mode is important 
    dbfile = open('examplePickle', 'rb')      
    db = pickle.load(dbfile) 
    for keys in db: 
        print(keys, '=>', db[keys]) 
    dbfile.close()

if __name__ == '__main__': 
    storeData() 
    loadData() 