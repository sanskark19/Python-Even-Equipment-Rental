#Import all the necessary files
import operation
import Read
import Write


#Function to validate and get a input from user
def validateSA():
    
    isvalidate=True
    while isvalidate==True:
        try:
            user_input=int(input("Enter a number:"))
            if user_input in [1,2,3]:
                isvalidate=False
                return user_input
            
        except:
            print("The value you enterd is wrong.Please enter the value again")       
# Function to validate and get a Serial Number from the user

def validateID(length):

    idvalidate=True
    while idvalidate==True:
        try:
            id_input=int(input("Enter a Serial Number:"))
            if id_input >0 and id_input <=length:
                idvalidate=False
                return id_input

        except:
            print("The value you enterd is wrong.Please enter the value again")

# Function to validate and get the quantity for renting           
def validateQuantity(size):
    
    validateQuantity=True
    while validateQuantity==True:
        try:
            validate_quantity=int(input("Enter number of quantity you want to rent:"))
            if validate_quantity >0 and validate_quantity <=size:
                validateQuantity = False
                return validate_quantity
            else : 
                print("Out of Stock") 
                return 0;       
        except:
            print("The value you enterd is wrong.Please enter the value again")
#Function to validatedaysreturn and get no of late days
def validateDaysReturn():
    
    validateDaysReturn=True
    while validateDaysReturn == True:
        try:
            validate_days=int(input("Enter no of late days to return the item:"))
            if validate_days >= 0:
                validateDaysReturn = False
                return validate_days
            else : 
                print("The value you entered is negative.Enter the correct value")
        except:
            print("The value you enterd is wrong.Please enter the value again")
        
def validateQuantityReturn() :
    validateData=True
    while validateData==True:
        try:
            validate_quantity=int(input("Enter number of quantity you want to return:"))
            if validate_quantity >= 0:
                validateData=False
                return validate_quantity
        except:
            print("The value you enterd is wrong.Please enter the value again")
    
#Main program in a loop
running=True
while running==True:
    data = Read.datas()
    length =len(data)
    operation.printing()
    
    user_input=validateSA()
    if user_input == 1:#Rent item
        list_1=[]
        renting=True
        while renting==True:
            Read.print_data()
            id_1=validateID(length)
         
            size = int(data[id_1-1][4])
            quantity=validateQuantity(size)
            data[id_1-1][4] = str(int(data[id_1-1][4]) - quantity)
            Write.write(data)
            
            list_1.append([id_1,quantity])
            cont=input("Do you want to continue.Type no to exit:")
            if cont.lower()=="no":
                renting=False
                Write.generate_invoice
        operation.rent(data,list_1)

    elif user_input==2:#Return Item
        list_2=[]
        returning=True
        while returning==True:
            Read.print_data()
            id_2=validateID(length)
            size = int(data[id_2-1][4])
            quantity=validateQuantityReturn()
            daysReturn = validateDaysReturn()
            data[id_2-1][4] = str(int(data[id_2-1][4]) + quantity)
            Write.write(data)
            list_2.append([id_2,quantity,daysReturn])
            cont=input("Do you want to continue.Type no to exit:")
            if cont.lower()=="no":
                returning=False
                Write.generate_invoice

        operation.returnItem(data,list_2)
        
    elif user_input==3:#Exit the program
        running=False
    
