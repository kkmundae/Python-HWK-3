# This code will analyze the data from election_data.csv
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#open file
with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    # this will skip header
    csv_header = next(csvreader)

    #Declaration of Variables
    row = next(csvreader)
    total_votes = 1
    candidates = {}
    vote_count = []
    vote_percentage = {}
    candidate_votes = []
    winning_votes = 0
        

    # Read each row of data after the header 
    for row in csvreader:
        #print(row)

        #Calculate Total Number of Votes
        total_votes = total_votes + 1

        #Calculate Total Number of Votes Cast per Candidate
        #Create a dictionary that shows Candidate : Number of Votes 
        if row[2] in candidates:
            candidates[row[2]] = candidates[row[2]] + 1
        else:
            candidates[row[2]] = 1
    
    #iterate through dictionary to make a list of values (vote count)
    for name, vote_count in candidates.items():
        
        vote_percentage[name] = '{0:.0%}'.format(float(vote_count) / float(total_votes))
        # vote_percentage.append((name,percent))

        if vote_count > winning_votes:
            winning_votes = vote_count
            winner = name

        # #iterate through dictionary to make a list of values ()
        # # vote_count.append((key,value))
        # # candidate_votes((key,vote_count))
        # percent = '{0:.0%}'.format(float(vote_count) / float(total_votes))
        # ##check rounding docs
        # vote_percentage.append((name,percent))

        # if vote_count > winning_votes:
        #     winning_votes = vote_count
        #     winner = name
    
    # candidate_votes = vote_percentage.append((key,percent))

        #iterate through dictionary using the values (vote count) to calculate percentages
  
    #iterate through dictionary using the values (vote count) to calculate percentages
    # for key,value in candidates.items():
    #     percent = round((float(value) / float(total_votes)) * 100,3)
    #     ##check rounding docs
    #     vote_percentage.append((key,percent))
    
   

print("Election Test Results")
print("----------------------------")
print(f"Total votes: {total_votes}")
print("----------------------------")
for name, vote_count in candidates.items():
    print(f"{name}: {vote_percentage[name]} ({vote_count})")

# # print(f"")
# print(candidates)
# # print(vote_count)
# print(vote_percentage)

#{vote_percentage[name]}
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

# Specify the file to write to
output_path = os.path.join('Analysis','output_pypoll.txt')
with open(output_path , 'w') as f:
    f.write("Election Test Results" + "\n")
    f.write("---------------------------------\n")
    for name, vote_count in candidates.items():
        f.write(f"{name}: {vote_percentage[name]} ({vote_count})" + "\n")
    f.write("----------------------------"+ "\n")
    f.write(f"Winner: {winner}" + "\n")
    f.write("----------------------------")

    


     
