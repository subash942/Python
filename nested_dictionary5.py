 
student = {
"name": "Alice",
"subjects": {
"Math": 95,
"Science": 88,
"English": 92
},
"age": 20
}

print(student["subjects"]["Science"])
student["subjects"]["Maths"] = 98
print(student)
print("-"*40)
employees = {
"emp1":{
"name":"tej",
"Department":"Software Development"
},
"emp2":{
"name":"sai",
"Department":"Cyber Security"
},
"emp3":{
"name":"varun",
"Department":"Software Engineer"
},
"emp4":{
"name":"jai",
"Department":"Software Development"
}
}
for i in employees.values():
 print(f"{i['name']} : {i['Department']}")
