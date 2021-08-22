import os
import csv
import pandas as pd
import xlwings as xw

path = os.path.join("Resources", "budget_data.csv")

df = pd.read_csv(path)

#wb = xw.view(df)

with open(path, 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)
    date = []
    profit_loss = []
    for row in csv_reader:
        d = row[0]
        date.append(d)
        p_l = int(row[1])
        profit_loss.append(p_l)

total_months = len(date)
total_amount = sum(profit_loss)

change_profit_loss = [profit_loss[i + 1] - profit_loss[i]
                      for i in range(len(profit_loss)-1)]

avg_profit_loss = (sum(change_profit_loss))/len(change_profit_loss)

max_profit = max(change_profit_loss)
min_profit = min(change_profit_loss)

change_profit_loss = [21588]+change_profit_loss
zip_file = dict(zip(change_profit_loss, date))

month_max_profit = zip_file[max_profit]
month_min_profit = zip_file[min_profit]

print(("Financial Analysis"))
print("--------------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${avg_profit_loss:.2f}')
print(f'Greatest Increase in Profits: {month_max_profit} (${max_profit})')
print(f'Greatest Decrease in Profits: {month_min_profit} (${min_profit})')


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
