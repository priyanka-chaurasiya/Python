# Dictionary Basics 

student= {
    "name": "Priyanka Chaurasiya",
    "city": "Indore",
    "age": 20,
    "rollNumber": 122,
}

print(type(student))
print(student["name"])
print(student)
print(student["city"])
# student["city"]= "Hyderabad"
# print(student)
student["favSubject"]= "Maths"
print(student)
student.pop("favSubject")
print(student)
print(student.items())