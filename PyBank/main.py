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
    months_total = 1
    net_total = int(row[1])
    total = float(row[1])
    current_value = row[1]
    final_profit = int(row[1])
    initial_profit = int(row[1])
    monthly_changes = []
    total_change = 0
    avg_change = 0
    date_list = []


    
    # Read each row of data after the header 
    for row in csvreader:
        # print(row)

        # calculate the total number of months in the dataset
        months_total = months_total + 1
    
         #calculate net total amount of "profit/losses" over the entire period
        # net_total is the final value
        # total is the profit/loss of each row
        total = float(row[1])
        net_total = round((net_total + total))
    
        #calculate average change.
        #create a list of profit/loss changes month to month
        final_profit = int(row[1])

        if months_total == 1:
            initial_profit = int(row[1])

        else:
            monthly_changes_profit = final_profit - initial_profit
            monthly_changes.append(monthly_changes_profit)
            # print(f"{final_profit} , {initial_profit}")
            initial_profit = final_profit 

        # print([monthly_changes])       
          
        total_change = total_change + monthly_changes_profit
        initial_profit = final_profit
        avg_change = round((total_change / (months_total-1)),2)

        greatest_profit = round(max(monthly_changes))
        greatest_loss = round(min(monthly_changes))

        #create list of dates
        date_list.append(str(row[0]))
      
        #find index of greatest profit/loss values
        greatest_profit_month = monthly_changes.index(greatest_profit)
        greatest_loss_month = monthly_changes.index(greatest_loss)

 #print statement to dispay result
print(f"Financial Analysis")
print("---------------------------------")
print(f"Total Months: {months_total}")
print(f"Total: ${net_total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {date_list[greatest_profit_month]}  (${greatest_profit})")
print(f"Greatest Decrease in Profits: {date_list[greatest_loss_month]}  (${greatest_loss})")

#Convert all to strings before writing
a = "Total Months: " + str(months_total) + "\n"
b = "Total: $" + str(net_total) + "\n"
c = "Average Change: $" + str(avg_change) + "\n"
d = "Greatest Increase in Profits: " + str(date_list[greatest_profit_month]) + " " + "($" + str(greatest_profit) + ")\n"
g = "Greatest Decrease in Profits: " + str(date_list[greatest_loss_month]) + " " + "($" + str(greatest_loss) + ")"


#Write to TXT File to be located in Analysis Folder

# Specify the file to write to
output_path = os.path.join('Analysis','output_pybank.txt')
with open(output_path , 'w') as f:

    f.write("Financial Analysis \n")
    f.write("---------------------------------\n")
    f.write(a)
    f.write(b)
    f.write(c)
    f.write(d)
    f.write(g)