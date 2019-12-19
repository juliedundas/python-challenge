import os
import csv

# Path to collect data election data csv file
election_csv = os.path.join('..', 'Resources', 'election_data.csv')

vote_data = {}
total_votes = 0
winning_votes = 0
winning_candidate = ""

with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        candidate = row[2]

        total_votes = total_votes + 1

        if total_votes > total_votes:
            winner = total_votes

        if candidate in vote_data:
            vote_data[candidate] = vote_data[candidate] + 1
        else:
            vote_data[candidate] = 1

#print(f"Total Votes: {total_votes}")
print("Election Results")
print("-" * 30)
print(f"Total Votes: {total_votes}")
print("-" * 30)
#for vote, num in votes.items():
#print(candidate + ": " + str(num))
for candidate, votes in vote_data.items():
    # print(candidate + ":   " + str(round((votes / total_votes) * 100, 2)) +"%   " + str(votes))
    #file.write(candidate + ":   " +
    #str(round((votes / total_votes) * 100, 2)) + "%   " +str(votes) + "\n")
    #winner = sum(total_votes)

    #Create if statement to find the winning candidate
    if votes > winning_votes:
        winning_votes = votes
        winning_candidate = candidate

#Loop though and print each candidate with the percent of votes and the total votes
    print(
        str(candidate) + ": " + str(round((votes / total_votes) * 100, 3)) +
        "% " + str(votes))

#winner = candidate.max()
#print(winning_candidate)

print("-" * 30)
#Print the winning candidate
print(f"Winner: {winning_candidate}")
print("-" * 30)