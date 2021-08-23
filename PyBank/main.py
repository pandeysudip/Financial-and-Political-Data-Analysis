import os
import csv
import pandas as pd
# import xlwings as xw  #importing xlwings for excel

# Defining a path for data source
path = os.path.join("Resources", "budget_data.csv")

# Reading the data using pandas
df = pd.read_csv(path)

# Using xlwings to open data in excel workbook
#wb = xw.view(df)

# Reading a csv file using CSV
with open(path, 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)  # moving to next row (ignoring header)
    date = []
    profit_loss = []
    for row in csv_reader:
        # date column
        d = row[0]
        date.append(d)
        # profit and loss column
        p_l = int(row[1])
        profit_loss.append(p_l)

# Calculating the total months using len function
total_months = len(date)
# Calculating total amount using sum function
total_amount = sum(profit_loss)

# Taking the value by substracting two rows of profit_loss
change_profit_loss = [profit_loss[i + 1] - profit_loss[i]
                      for i in range(len(profit_loss)-1)]

# Calculating the average
avg_profit_loss = (sum(change_profit_loss))/len(change_profit_loss)

# Using max function to calculate maximum profit
max_profit = max(change_profit_loss)

# Using min function to calculate minimum profit
min_profit = min(change_profit_loss)

# Adding first value of profit_loss
change_profit_loss = [21588]+change_profit_loss

# Using zip to create dictionary so that we can easily get date
zip_file = dict(zip(change_profit_loss, date))

# using dictionary to calculate month
month_max_profit = zip_file[max_profit]
month_min_profit = zip_file[min_profit]

# printing results
print(("Financial Analysis"))
print("--------------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${avg_profit_loss:.2f}')
print(f'Greatest Increase in Profits: {month_max_profit} (${max_profit})')
print(f'Greatest Decrease in Profits: {month_min_profit} (${min_profit})')


# Saving output text file
output_file = os.path.join("analysis", "pybank.csv")
with open(output_file, "w", newline='')as file:
    file.write("Financial Analysis")
    file.write("\n--------------------------------------")
    file.write(f'\nTotal Months: {total_months}')
    file.write(f'\nTotal: ${total_amount}')
    file.write(f'\nAverage Change: ${avg_profit_loss:.2f}')
    file.write(
        f'\nGreatest Increase in Profits: {month_max_profit} (${max_profit})')
    file.write(
        f'\nGreatest Decrease in Profits: {month_min_profit} (${min_profit})')
