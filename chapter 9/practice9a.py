#Create a class Laptop with attributes: brand, RAM, price. Create 2 object
#with different values.

class Laptop:
    brand= "default"
    RAM= "default 8GB"
    price= "default 1 Lakh"

laptop1= Laptop()
laptop1.brand= "Mackbook"
laptop1.RAM= "16GB"
print("Laptop1 Brand - ", laptop1.brand)

laptop2= Laptop()
laptop2.brand= "Lenovo"
print("Laptop2 Brand - ", laptop2.brand)