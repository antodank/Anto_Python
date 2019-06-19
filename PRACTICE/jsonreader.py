import json
 
input = '''
{
    "FirstName":"Bhairav",
    "MiddleName":"S",
    "LastName":"Ram",
    "DateOfBirth":"09-01-1984",
    "Contact":{
        "Phone":9988776655,
        "Email":"bhairav@gmail.com"
    },
    "Address":[
        {
            "Type":"Office",
            "ZipNumber":560056,
            "Street":"Nagarbhavi Road",
            "City":"Bangalore",
            "Country":"India"
        },
        {
            "Type":"Home",
            "ZipNumber":560004,
            "Street":"Gandhi Bazaar Road",
            "City":"Bangalore",
            "Country":"India"
        }
    ]
}
        '''
#print(type(input))
jsonObjectInfo = json.loads(input)
#print(type(jsonObjectInfo))
#print(jsonObjectInfo)
print("First Name is {0}".format(jsonObjectInfo['FirstName']))
print("Middle Name is {0}".format(jsonObjectInfo['MiddleName']))
print("Last Name is {0}".format(jsonObjectInfo['LastName']))
print("Date of Birth is {0}".format(jsonObjectInfo['DateOfBirth']))
print("Phone Number is {0}".format(jsonObjectInfo['Contact'][0]))
print("Email ID is is {0}".format(jsonObjectInfo['Contact'][1]))
print("-----------------**************---------------")
for eachJsonObject in jsonObjectInfo['Address']:
    print("Address Type is {0}".format(eachJsonObject['Type']))
    print("Zip Number is {0}".format(eachJsonObject['ZipNumber']))
    print("Street Name is {0}".format(eachJsonObject['Street']))
    print("City Name is {0}".format(eachJsonObject['City']))
    print("Country Name is {0}".format(eachJsonObject['Country']))
    print("-----------------**************---------------")
 