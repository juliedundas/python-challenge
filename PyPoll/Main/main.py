import os
import csv

# Path to collect data election data csv file
election_csv = os.path.join('..', 'Resources', 'election_data.csv')

votes = {}
total_rows = 0
total_vote_count = 0

with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        total_rows = total_rows + 1
        total_vote_count = total_vote_count + int(row[0])

        vote = row[0]

        if vote in votes:
            votes[vote] = votes[animal] + 1
        else:
            votes[vote] = 1

for vote, num in votes.items():
    #print(vote + ": " + str(num))

    print(total_rows)
    #print(total_vote_count)