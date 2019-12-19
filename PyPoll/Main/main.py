import os
import csv

# Path to collect data election data csv file
election_csv = os.path.join('..', 'Resources', 'election_data.csv')

votes = {}
total_votes = 0
winner = ""

with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        candidate = row[2]

        total_votes = total_votes + 1

        if candidate in votes:
            votes[candidate] = votes[candidate] + 1
        else:
            votes[candidate] = 1

        if votes[candidate] > votes[candidate]:
            votes[candidate] = winner

#print(f"Total Votes: {total_votes}")
print("Election Results")
print("-----------------------")
print(f"Total Votes: ${total_votes}")
print("-----------------------")
#for vote, num in votes.items():
#print(candidate + ": " + str(num))
for candidate, votes in votes.items():
    # print(candidate + ":   " + str(round((votes / total_votes) * 100, 2)) +"%   " + str(votes))
    #file.write(candidate + ":   " +
    #str(round((votes / total_votes) * 100, 2)) + "%   " +str(votes) + "\n")
    #winner = sum(total_votes)

    print(
        str(candidate) + ": " + str(round((votes / total_votes) * 100, 3)) +
        "% " + str(votes))

print(winner)

print("-----------------------")

print(f"Winner: {winner}")
print("-----------------------")