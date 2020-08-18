# This code will analyze the data from budget_data.csv
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#open file
with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is no header)
    #this will skip header
    csv_header = next(csvreader)
    

    #read data from first line after header in CSV file
    row = next(csvreader)
    months_total = 0
    net_total = float(row[1])
    total = float(row[1])

    
    # Read each row of data after the header 
    for row in csvreader:
        # print(row)

    # calculate the total number of months in the dataset
        months_total = months_total + 1
    
    #calculate net total amount of "profit/losses" over the entire period
    # net_total is the final value
    # total is the profit/loss of each row
        total = float(row[1])
        net_total = net_total + total
        

    
    
    
    #print statement to dispay result
    print(months_total)
    print(f"{net_total}")
