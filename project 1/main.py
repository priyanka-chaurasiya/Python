# Expense Tracker Project

expensesList = []  #List of expenses in form of dictionary
print("Welcome to Expense Tracker :  ")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Khrcha")
    print("4. Exit")

    choice= int(input("please Enter Your Choice : "))

# 1. Add Expense
    if(choice == 1):
        date= input("kis date par khrcha kiya tha?")
        category= input("kis type par khrcha kiya? (food, Travel, Makeup, Books): ")
        description= input("aur details dedo: ")
        amount= float(input("Enter the amount: "))   
        
        expense= {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("\n DONE bro. Expense is added succesfully")

# 2. VIEW ALL EXPENSES
    elif(choice == 2):
            if(len(expensesList)==0):
                print("No Expenses added. Jao pehle Khrcha karo. ")
            else:
                print("==== Ye y apka sara expense ====")  
                count= 1
                for eachKharcha in expensesList:
                    print(f"kharcha Number {count} -> {eachKharcha["date"]}, {eachKharcha["category"]}, {eachKharcha["description"]}, {eachKharcha["amount"]}")
                    count= count+1

# 3. View Total Spending
    elif(choice == 3):
        total= 0
        for eachKracha in expensesList:
            total = total + eachKracha["amount"] 

        print("\n TOTAL KHRCHA = ", total)              

# 4. EXIT 
    elif(choice == 4):
        print("Dhanyawad aapne humara system use kiya")
        break
    else:
        print("INVALD CHOICE. TRY AGAIN")