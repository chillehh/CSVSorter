import csv

division = 3
points = 4

# Open the .csv file
with open('data.csv') as csvData:
    # Read in the csv data
    reader = csv.reader(csvData)
    # Set the data to a list for sorting
    data = list(reader)

# Delete the first lot of data as its just the names of the columns
del data[0]

# Convert the division and points columns to ints for sorting
for i in range(len(data)):
    div = data[i]
    div[division] = int(div[division])
    point = data[i]
    point[points] = int(point[points])


# Sort the data by division from lowest to highest and then by points from highest to lowest
data.sort(key=lambda x: (x[division], -x[points]))

# Print initial 'records: '
print('records: ')

# Loop over the top 3 results and print accordingly
for i in range(len(data)):
    if i < 3:
        result = data[i]
        print('- name: ' + result[0] + ' ' + result[1] + '\ndetails: In division ' + str(result[division]) + ' from ' + result[2] + ' performing ' + result[5])
