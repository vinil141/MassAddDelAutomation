import csv   #importing the csv module


class Setdata():
    
    '''READING THE FILES'''

    file = open("data/CTNList.csv",'r') 
    reader = csv.reader(file)
    
    metadata = {}  #creationg the dictionary
    metadata["file_path"] = 'G:\\Destination\\'  #adding the file path to dictionary


    '''FETCHING VALUES FROM CSV AND PUT INTO DICT'''
    for row in reader:
        metadata[row[0]] = row[2]


    print("\n*******************************************************************")

    print("Dictionary Keys:\n")
    k = metadata.keys()
    print(k,"\n")

    print("\n*******************************************************************")
    print("Dictionary Values:\n")
    for val in metadata:
        data = metadata[val]
    print(data)


    print("\n*******************************************************************")
    print("Key value pair")
    for key,val in metadata.items():
        print(key,"-->",val)

    print("\n*******************************************************************")
    print("\n*******************************************************************")

x = Setdata()

print("using classs\n")
print(x.metadata["Request Type"])
















    
        
    
        
   
