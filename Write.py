

#Create a function to generate invoice
def generate_invoice(id, name, quantity, number, time,data):
    a = open(f"./Rent/invoice-{name}-{time}.txt", "w")#open an invoice file
    total = 0#Initialize the cost to 0
    header = f"name : {name}\nPhone Number : {number}\nTime : {time}\n\n"
    a.write(header)
#Iterate through the items
    for i in range(len(id)) :
        sn = (data[i][0]).replace('.,'," ")
        equipment = data[i][1]
        brand = data[i][2]
        cost = data[i][3]
        inventory = data[i][4]
        total += (int(cost.replace('$','')))*quantity[i]
        items = (f"{sn}, {equipment}, {brand}, Price : {cost}, quantity : {quantity[i]}, total : {(int(cost.replace('$','')))*quantity[i]}\n\n")
        a.write(items)
    totalStr = f"Total : ${total}"
    a.write(totalStr)#Write the total cost to invoice
#Create function to gerenate a invoice for returned items
def invoice_return(id, name, quantity, number, time,data,daysLate):
    a = open(f"./Return/invoice{name}{time}.txt", "w")
    #Initialize the total cost,totalFine,SUbtotal
    total = 0
    totalFine = 0
    subTotal = 0
    header = f"name : {name}\nPhone Number : {number}\nTime : {time}\n"
    a.write(header)
    for i in range(len(id)) :#iterate through the returned items
        sn = (data[i][0]).replace('.,'," ")
        equipment = data[i][1]
        brand = data[i][2]
        cost = data[i][3]
        perdayCost = (int(cost.replace('$','')))/5
        total += (int(cost.replace('$','')))*quantity[i]
        fine = daysLate[i]*(perdayCost)
        totalFine += fine
        items = (f"{sn}, {equipment}, {brand}, Price : {cost}, quantity : {quantity[i]}, total : {(int(cost.replace('$','')))*quantity[i]}, fine : {fine}\n\n")
        a.write(items)
    totalStr = f"Total Amount without Fine : ${total}\n"
    fineStr = f"Total Fine Amount : ${totalFine}\n"
    subTotalStr = f"\nSub Total :{total+totalFine}\n"

    a.write(totalStr)#Write the total cost without fine
    a.write(fineStr)#Write the total fine amount
    a.write(subTotalStr)#Write the sub total

def write(data):
    b=open("data.txt","w")
    for a in data:
        a=",".join(a)
        b.write(a+"\n")


    
   
