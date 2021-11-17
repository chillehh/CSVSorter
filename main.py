######################################################################
# CSVSorter                           Created by Jacob Ling 17/11/21 #
# This program takes 3 input arguments:                              #
#   - The path to the .csv file for sorting.                         #
#   - The name of the first column to be sorted in ascending order.  #
#   - The name of the second column to be sorted in descending order.#
######################################################################

import csv
import sys

# Constants as determined by input
FilePath = ""
ColumnNames = []
ColumnOne = ""
ColumnTwo = ""
ColumnOneIndex = 0
ColumnTwoIndex = 0

# Get input arguments as constants, throw error if input arguments do not meet the index of input
while True:
    try:
        FilePath = sys.argv[1]
        ColumnOne = sys.argv[2]
        ColumnTwo = sys.argv[3]
        break
    except IndexError:
        print("Oops! Please enter three arguments for input:\n    - The file path, "
              "\n    - The first column to be sorted in ascending order, "
              "\n    - The second column to be sorted in descending order.")
        exit()
        break

# Open the .csv file
with open(FilePath) as csvData:
    # Read in the csv data
    reader = csv.reader(csvData)
    # Set the data to a list for sorting
    data = list(reader)

# Set the ColumnNames to the top row, which is the names of each column of data
ColumnNames = data[0]

# Get the column indices from the column names provided by matching the names to the name row in the csv data
for i in range(len(ColumnNames)):
    if ColumnNames[i] == ColumnOne:
        ColumnOneIndex = i
    elif ColumnNames[i] == ColumnTwo:
        ColumnTwoIndex = i

# Delete the first lot of data as its just the names of the columns
del data[0]

# Convert the columns to be sorted to ints
for i in range(len(data)):
    row = data[i]
    for j in range(len(ColumnNames)):
        if ColumnNames[j] == ColumnOne:
            row[j] = int(row[j])
        elif ColumnNames[j] == ColumnTwo:
            row[j] = int(row[j])


# Sort the data by the input ColumnOne from lowest to highest and then by the input ColumnTwo from highest to lowest
data.sort(key=lambda x: (x[ColumnOneIndex], -x[ColumnTwoIndex]))

# Print initial 'records: '
print('records: ')

# Loop over the top 3 results and print accordingly for YAML output
for i in range(len(data)):
    if i < 3:
        result = data[i]
        print('- name: ' + result[0] + ' ' + result[1] + '\ndetails: In division ' + str(result[ColumnOneIndex]) +
              ' from ' + result[2] + ' performing ' + result[5])
