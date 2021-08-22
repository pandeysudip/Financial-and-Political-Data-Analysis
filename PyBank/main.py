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

inc_profit = []
dec_profit = []
for n in profit_loss:
    if n >= 0:
        inc_profit.append(n)
    else:
        dec_profit.append(n)

total_inc_profit = sum(inc_profit)
total_dec_profit = sum(dec_profit)

change_profit = (total_inc_profit-total_dec_profit)/total_months

max_profit = max(inc_profit)
min_profit = min(dec_profit)

print(total_months)
print(total_amount)
print(change_profit)
print(max_profit)
print(min_profit)
