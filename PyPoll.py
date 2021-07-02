import csv
import os

#assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")


#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize total vote counter. 
total_votes = 0

#Candidate options list
candidate_options = []

#Candidate votes as dictionary (to hold key/value pairs)
candidate_votes = {}

#Declare variable to hold empty string value for winning candidate
winning_candidate = ""

#Variable for the winning count set = 0
winning_count = 0

#Variable for winning % = 0
winning_percentage = 0

#open the election results & read the file
with open(file_to_load) as election_data:
    #Read file object with reader function
    file_reader=csv.reader(election_data)

    #Read header row
    headers = next(file_reader)

#For each row in the CSV file
    for row in file_reader:
        #Add to total vote count
        total_votes += 1
        
        #Get candidate name from each row
        candidate_name = row[2]
        
        #If candidate name does not match an existing candidate in the list, add it
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
            
    
        #Adding votes to each candidate's count
        candidate_votes[candidate_name] += 1
    
    #Determine % of votes for each candidate
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate=candidate_name

    #Determine winning vote count & winning percentage
    

#Print candidate list.
print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")










