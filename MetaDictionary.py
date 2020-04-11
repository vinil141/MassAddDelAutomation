import csv  # importing the csv module
'''READING THE FILES'''

file = open("data/CTNList.csv", 'r')
reader = csv.reader(file)
metadata = {"file_path": "'G:\\Destination\\'"}  # creating the dictionary

'''FETCHING VALUES FROM CSV AND PUT INTO DICT'''
for row in reader:
    metadata[row[0]] = {row[2]}

print("Dictionary Keys:\n")
k = metadata.keys()
print(k, "\n")

print("Dictionary Values:\n")
for val in metadata:
    data = metadata[val]
    print(data)

print("Key value pair")
for key, val in metadata.items():
    print(key, "-->", val)