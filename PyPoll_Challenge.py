print("test")
import csv
import os

#Add variable to load a file from path
file_to_load=os.path.join("Resources", "election_results.csv")

#Add a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")


#Initialize total vote counter
total_votes = 0

#Candidate options & candidate votes
candidate_options = []
candidate_votes = {}

#Create a county list and a county votes dictionary
county_list = []
county_votes = {}

#Track winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Track the largest county & its voter turnout
winning_county = ""
winning_turnout_votes = 0
winning_vote_percentage = 0


#Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    #Read the header
    header = next(reader)

    #For each row in CSV file
    for row in reader:
        #Add to total vote count
        total_votes = total_votes + 1

        #Get candidate name from each row.
        candidate_name = row[2]

        #Extract county name from each row
        county_name = row[1]

        #If candidate does not match any existing candidate, add it to the candidate list
        if candidate_name not in candidate_options:

            #Add candidate name to candidate list
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's voter count.
            candidate_votes[candidate_name]=0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name]+=1

        #Write an if statement that makes sure the county does not match any existing county in the county list
        if county_name not in county_list: 
            county_list.append(county_name)

            #Track county's vote count
            county_votes[county_name] = 0

        #Add a vote to that county's vote count
        county_votes[county_name]+=1


#Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    #print final vote count(to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)


    
    
    #6a Write a for loop to get the county from the county dictionary
    for county_name in county_votes:
        #Retrieve county vote count
        votes = county_votes[county_name]
        #Calculate percentage of votes for county
        vote_percentage = (votes/total_votes) *100
        
        
        
    #6d Print county results
        county_results = (
            f"\n{county_name}: {vote_percentage: .2f}% of the vote.")
        print(county_results, end="")
        
        #6eSave county votes to a text file
        txt_file.write(county_results)
        
        #6f Write an if statement to determine the winning county and get its votes
        














