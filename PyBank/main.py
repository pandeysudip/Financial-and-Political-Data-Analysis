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

#change_profit_loss = change_profit_loss.insert(0, 1)
zip_file = dict(zip(change_profit_loss, date))

month_max_profit = zip_file[max_profit]
month_min_profit = zip_file[min_profit]

print(total_months)
print(total_amount)
print(avg_profit_loss)
print(max_profit)
print(min_profit)
print(month_max_profit)
print(month_min_profit)
print(type(change_profit_loss))
