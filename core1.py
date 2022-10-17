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
students[0]['last_name']='Bryant'
print(students)
sports_directory['soccer'][1]= 'Sadiku'
print(sports_directory)
z[0]['y']=30
print(z)
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in range(len(students)):
        print("first_name - "+students[i]['first_name']+", last_name - "+students[i]['last_name'])
iterateDictionary(students) 
def iterateDictionary2(key_name, list):
    for i in range(len(list)) :
        print(list[i][key_name])
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]),key)
        for i in range(len(some_dict[key])):
            print(some_dict[key][i])
        print("")

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

