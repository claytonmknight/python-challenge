# dependencies
import os
import csv

# pybank file paths
budget_data = "PyBank/Resources/budget_data.csv"
file_to_output = "PyBank/analysis/budget_analysis.txt"

# financial analysis variables
total_months = 0
total = 0
prev_revenue = 0
revenue_change_list = []
month_of_change = []

# import csv
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        total_months += 1
        total += int(row[1])  
        revenue_change = int(row[1]) - prev_revenue
        prev_revenue = int(row[1])
        revenue_change_list.append(revenue_change)
        month_of_change.append(row[0])

# calculate average change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

# find greatest increase and decrease
greatest_increase = max(revenue_change_list)
greatest_decrease = min(revenue_change_list)

# output
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total}\n"
    f"Average Change: ${revenue_avg:.2f}\n"
    f"Greatest Increase in Profits: {month_of_change[revenue_change_list.index(greatest_increase)]} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {month_of_change[revenue_change_list.index(greatest_decrease)]} (${greatest_decrease})\n"
)

# print output
print(output)

# export to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)