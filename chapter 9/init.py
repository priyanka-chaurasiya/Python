class Student:
    schoolName= "ABC School"

    def __init__(self, name, course):
        # print("Whenever a new object is created I am called automatically")
        # print(self)
        self.name= name
        self.course= course

Student1= Student("khushi", "Btech") #init method will be called 
print("Student1 Name-", Student1.name)
print("Student1 Course-", Student1.course)

Student2= Student("Ankit", "Bsc")
print("Student2 Name-", Student2.name)
print("Student2 Course-", Student2.course)
