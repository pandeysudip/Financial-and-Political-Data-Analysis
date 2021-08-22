import os
import csv
import pandas as pd
import xlwings as xw
from collections import Counter

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


#Khan = [k for k in names if k == 'Khan']
#Correy = [c for c in names if c == 'Correy']
Li = [l for l in names if l == 'Li']
Tooley = [t for t in names if t == "O'Tooley"]


khan_total = names.count("Khan")
khan_per = (khan_total/total_vote)*100

correy_total = names.count("Correy")
correy_per = (correy_total/total_vote)*100

li_total = len(Li)
li_per = (li_total/total_vote)*100

tooley_total = len(Tooley)
tooley_per = (tooley_total/total_vote)*100


def popular_vote(names):
    counter = 0
    name = names[0]

    for i in names:
        curr_frequency = name.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            name = i

    return name


def most_frequent(list):
    occur = Counter(list)
    # return occur.most_common(1)
    return occur, occur.most_common(1)


a, b = most_frequent(names)

print(a["Khan"])
print(b[0][0])
print(popular_vote(names))
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


output_file = os.path.join("analysis", "pypoll.csv")
with open(output_file, "w", newline='')as file:
    writer = csv.writer(file)
    writer.writerow(["title", "price", "subscriber_count",
                     "number_of_reviews", "course_length"])
    writer.writerows(cleaned_csv)
