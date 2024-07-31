
#Function to read data

def datas():
    file=open('data.txt','r')#Upload the data file for reading
    read=file.readlines()
    list_a=[]
    for line in read:
        line=line.strip('\n').split(',')
        list_a.append(line)
    
    file.close()#Close the file
    return list_a#Returns the list

#Function to print
def print_data():
    data = datas()
    for line in data:
        line = ",  ".join(line).replace("\n","")
        print(line, end = " ")
        print("\n")

    



