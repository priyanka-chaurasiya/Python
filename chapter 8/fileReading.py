#write keyword

file = open("report.txt", "r")
data= file.read()
file.close()

with open("report.txt","r") as f:
    data= f.read()
    print("File Data", data)