# Create a new dictionary
d = {}

# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}

print(my_dict['key2'])

#flexible to store any data
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}

# Create a new key through assignment
d['A01'] = 'Ankit'

# Dictionary nested inside a dictionary nested inside a dictionary
d = {'key1':{'nestkey':{'subnestkey':'nest val'}}}
print(d['key1']['nestkey']['subnestkey'])
