# Create class Student that takes 3 marks and ha a method averge().

class Student:

    def __init__(self, name, listOfMarks):
        self.name= name
        self.listOfMarks= listOfMarks
        
    def average(self):
        sum= 0
        for eachValue in self.listOfMarks:
            sum= sum+eachValue

        average=  sum/3    
        print("Average is: ", average)

student1= Student("Aditya", [90, 98, 99])
student1.average()