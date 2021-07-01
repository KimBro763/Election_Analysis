import csv
import os

#assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")


#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results & read the file
with open(file_to_load) as election_data:
    #Read file object with reader function
    file_reader=csv.reader(election_data)

    #Print each row in the CSV file
    #for row in file_reader:
        #print(row)

#Print header row
    headers = next(file_reader)
    print(headers)





