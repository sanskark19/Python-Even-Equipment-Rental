#Import all the necessary files
from datetime import datetime
from Write import generate_invoice,invoice_return
def rent(data,list):
    name=input("Enter your name:")
    quantity = []
    id = []
    count = 0#Initializing the value to count 0
    for i in list : 
        id.append(list[count][0]) 
        quantity.append(list[count][1])
        count += 1
    number=int(input("Enter your phone number:"))
    time=datetime.today().strftime('%d:%m:%Y')
    generate_invoice(id,name, quantity, number, time,data)


#Creating a function to generate a bill
def returnItem(data,list):
    name=input("Enter your name:")
    quantity = []
    id = []
    days = []
    count = 0#Initializing the value of count 0
    for i in list : 
        id.append(list[count][0]) 
        quantity.append(list[count][1])
        days.append(list[count][2])
        count += 1
    number=int(input("Enter your phone number:"))
    time=datetime.today().strftime('%d:%m:%Y')
    invoice_return(id,name, quantity, number, time,data,days)
    

        
#Function to print the display

def printing():
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("")
    print("Welcome to our Equipment Rental Shop!")
    print("")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("")
    print("Select an option from 1 to 3:")
    print("")
    print("S.N")
    print("1. Press 1 to rent an Equipment.")
    print("2. Press 2 to return an Equipment.")
    print("3. Press 3 to exit the screen.")
    print("")
    print("*************************************************************")



        




 
    
    

