# Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print(x)

students[0]["last_name"] = "Bryant"

sports_directory["soccer"][0] = 'Andres'

z[0]['y']=30
print(z)

# Iterate Through a List of Dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in range (0, len(students)):
        studentDictionary = students[i]
        for key in studentDictionary:
            print (key, studentDictionary[key])

iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for i in range(0, len(some_list)):
        print (some_list[i][key_name])

iterateDictionary2('first_name', students)

# Iterate Through a Dictionary with List Values
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# printInfo(dojo)

def printInfo(some_dict):
    for key in some_dict:
        print (len(some_dict[key]), key)
        for i in range(0, len(some_dict[key])):
            print(some_dict[key][i])

printInfo(dojo)
        
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

