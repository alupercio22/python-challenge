import os
import csv

budget_data = os.path.join('PyBank', 'Resources', 'budget_data.csv')

total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_decrease = 0
worst_month = 0
greatest_increase = 0
best_month = 0

with open(budget_data, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    row = next(csvreader)
    
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    best_month = row[0]
    
    for row in csvreader:
        
        total_months += 1
        net_amount += int(row[1])

        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            best_month = row[0]
            
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            worst_month = row[0]  
        
    average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)
print("Financial Analysis")
print("---------------------------")
print("Total Months:", total_months)
print("Total: $", net_amount)
print("Average Change: $", '{:.2f}'.format(average_change))
print("Greatest Increase in Profits:", best_month, "($", '{:.2f}'.format(highest),")")
print("Greatest Decrease in Profits:", worst_month, "($", '{:.2f}'.format(lowest),")")

output_path = os.path.join('.', 'PyBank', 'Resources', 'results.txt')

with open(output_path, 'w') as text_file:
    print("Financial Analysis", file=text_file)
    print("---------------------------", file=text_file)
    print("Total Months:", total_months, file=text_file)
    print("Total: $", net_amount, file=text_file)
    print("Average Change: $", '{:.2f}'.format(average_change), file=text_file)
    print("Greatest Increase in Profits:", best_month, "($", '{:.2f}'.format(highest),")", file=text_file)
    print("Greatest Decrease in Profits:", worst_month, "($", '{:.2f}'.format(lowest),")", file=text_file)
