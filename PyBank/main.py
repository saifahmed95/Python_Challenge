import os
import csv
#Initialize Variable
months_count=0
total_profit_loss=0
budget_csv = os.path.join("c:/", "Users", "mango", "Desktop", "Python_Challenge","PyBank","budget_data.csv")

# Open the CSV
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip headers
    next(csvreader, None)

    # Read data
    row = next(csvreader,None)
    max_month = row[0]
    min_month = row[0]
    profitloss = int(row[1])
    min_profitloss = profitloss
    max_profitloss = profitloss
    previous_profitloss = profitloss
    months_count = 1
    total_profit_loss = profitloss
    profitloss_change_sum = 0
    
    for row in csvreader:
            months_count = months_count + 1

            profitloss = int(row[1])
            total_profit_loss = total_profit_loss + profitloss

            profit_change = profitloss - previous_profitloss

            profitloss_change_sum = profitloss_change_sum + profit_change

            if profit_change > max_profitloss:
                max_month = row[0]
                max_profitloss = profit_change

            if profit_change < min_profitloss:
                min_month = row[0]
                min_profitloss = profit_change

            previous_profitloss = profitloss

    average_profit_change=round(float(profitloss_change_sum/(months_count-1)),2)
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months_count}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: $ {average_profit_change}")
    print(f"Greatest Increase in Profits: {max_month} $ {max_profitloss}")
    print(f"Greatest Decrease in Profits: {min_profitloss} $ {min_profitloss}")
  
  

output_file = open("PyBank.txt","w") 
 
output_file.write("Financial Analysis"+ '\n') 
output_file.write("----------------------------"+ '\n')
output_file.write(f"Total Months: {months_count}"+ '\n')
output_file.write(f"Total: ${total_profit_loss}"+ '\n')
output_file.write(f"Average Change: ${average_profit_change}"+ '\n')
output_file.write(f"Greatest Increase in Profits: {max_month} $ {max_profitloss}"+ '\n')
output_file.write(f"Greatest Decrease in Profits: {min_profitloss} $ {min_profitloss}"+ '\n')
 
output_file.close() 