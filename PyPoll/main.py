import os
import csv
import pandas as pd
import xlwings as xw

path = os.path.join("Resources", "election_data.csv")

df = pd.read_csv(path)

#wb = xw.view(df)

with open(path, 'r')as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)
    v_id = []
    county = []
    names = []
    for row in csv_reader:
        v = row[0]
        v_id.append(v)
        c = row[1]
        county.append(c)
        n = row[2]
        names.append(n)

total_vote = len(v_id)

candidates = list(set(names))

Khan = [k for k in names if k == 'Khan']
Correy = [c for c in names if c == 'Correy']
Li = [l for l in names if l == 'Li']
Tooley = [t for t in names if t == "O'Tooley"]


khan_total = len(Khan)
khan_per = (khan_total/total_vote)*100

correy_total = len(Correy)
correy_per = (correy_total/total_vote)*100

li_total = len(Li)
li_per = (li_total/total_vote)*100

tooley_total = len(Tooley)
tooley_per = (tooley_total/total_vote)*100


print(total_vote)
print(candidates)

print(khan_total)
print(khan_per)
print(correy_total)
print(correy_per)
print(li_total)
print(li_per)
print(tooley_total)
print(tooley_per)
