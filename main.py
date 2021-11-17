import csv

division = 3
points = 4

# Open the .csv file
with open('data.csv') as csvData:
    # Read in the csv data
    reader = csv.reader(csvData)
    # Set the data to a list for sorting
    data = list(reader)

print(data) # Testing purposes

# Originally using a bool to set to true when the first object in the list was deleted but realised I could just delete
# the first object before iterating over the list
deleteTop = False

# Delete the first lot of data as its just the names of the columns
del data[0]

for i in range(len(data)):
    print(data[i]) # Testing purposes
    div = data[i]
    div[division] = int(div[division])
    point = data[i]
    point[points] = int(point[points])
        #data[i[division]] = data[int(i[division])]
        #i[points] = i[int(points)]
    print('changed to Int') # Testing purposes
    #elif i == 0 and not deleteTop:
     #   print('deleting..')
      #  del data[i]
       # deleteTop = True
        #continue

# Sort the data by division from lowest to highest and then by points from highest to lowest
data.sort(key=lambda x: (x[division], -x[points]))
print(data) # Show the sorted data for output