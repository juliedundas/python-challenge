#Import os module
import os

#Import module to read CSV files
import csv

#Read the CSV file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

change = 0
prev = 0
total = 0
total_profit = 0
greatest_increase = 0
greatest_decrease = 0
sum_change = 0
great_increase_month = 0
total_sum = 0
average_change = 0

with open(csvpath, newline='') as csvfile:

    #Create variable to read & specify delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print("Financial Analysis")
    print("-----------------------")
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #Loop through and find the totals
        total = total + 1
        total_profit = total_profit + int(row[1])
        #print(total_profit)

        if total > 1:
            change = int(row[1]) - int(prev)
            #print(change)

        if change > greatest_increase:
            greatest_increase = change

            #if change > greatest_decrease:
            # greatest_decrease = int(change)
            # print(greatest_decrease)

        prev = row[1]
        #print(prev)

        #print(row[0])

print(f"Total Months: {total}")
print(f"Greatest Increase in Profits: {row[0]} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {row[0]} (${greatest_increase})")