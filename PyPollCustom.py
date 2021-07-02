import csv
import os

total_votes = 0
candidate_votes={}


# OPEN THE FILE AND READ THE DATA
with open("Resources/election_results.csv", 'r') as election_data:
    reader = csv.reader(election_data)

    column_names = next(reader)

    for row in reader:
        total_votes+=1
        candidate_name = row[2]
        if candidate_name not in candidate_votes.keys():
            candidate_votes[candidate_name]=1
        else:
            candidate_votes[candidate_name]+=1


# SAVE & DISPLAY THE ANALYSIS
with open("analysis/election_analysis.txt", "w") as txt_file:

    election_results = f"""Election Results
    -------------------------
    Total Votes: {total_votes}
    -------------------------
    County Votes:
    {candidate_votes}"""


    txt_file.write(election_results)
    print(election_results)

