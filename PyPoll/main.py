# Importing modules
import os
import csv
import pandas as pd
# import xlwings as xw  #To use for excel workbook
#from collections import Counter

# Defining a path of data source
path = os.path.join("Resources", "election_data.csv")

# Using pandas to read csv file
df = pd.read_csv(path)

# This will open data in seperate excel workbook
#wb = xw.view(df)

# Reading csv file
with open(path, 'r')as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)
    v_id = []
    county = []
    names = []
    for row in csv_reader:
        # First column is voter_id
        v = row[0]
        v_id.append(v)
        # Second column is County
        c = row[1]
        county.append(c)
        # Third column is names
        n = row[2]
        names.append(n)

# Calculating total votes using len function
total_vote = len(v_id)

# Using set to get individuals name(no repetation)
candidates = list(set(names))


# Using list compresion to get all individual name only
#Khan = [k for k in names if k == 'Khan']
#Correy = [c for c in names if c == 'Correy']
Li = [l for l in names if l == 'Li']
Tooley = [t for t in names if t == "O'Tooley"]

# We can also use count to get individual numbers
khan_total = names.count("Khan")
# Calculating total percent for Khan
khan_per = (khan_total/total_vote)*100

correy_total = names.count("Correy")
# Calculating total percent for Correy
correy_per = (correy_total/total_vote)*100

# Using len function to get total
li_total = len(Li)
# Calculating total percent for Li
li_per = (li_total/total_vote)*100

# Using len function to get total
tooley_total = len(Tooley)
# Calculating total percent for O'Tooley
tooley_per = (tooley_total/total_vote)*100

# Creating a function to get must popular vote


def popular_vote(names):
    counter = 0
    name = names[0]

    for i in names:
        curr_frequency = name.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            name = i

    return name


# Geeting most_frequent name
p_vote = popular_vote(names)

# Another function using 'Counter' to get must popular vote
# def most_frequent(list):
#occur = Counter(list)
# return occur.most_common(1)
# return occur, occur.most_common(1)


# Geeting most_frequent name from most_frequent function
#a, b = most_frequent(names)

# Printing results
print("Election Results")
print("--------------------------------------")
print(f'Total Votes: {total_vote}')
print("--------------------------------------")
print(f'Khan: {khan_per:.3f}% ({khan_total})')
print(f'Correy: {correy_per:.3f}% ({correy_total})')
print(f'Li: {li_per:.3f}% ({li_total})')
print(f"O'Tooley:{tooley_per:.3f}% ({tooley_total})")
print("--------------------------------------")
print(f'winner: {p_vote}')
print("--------------------------------------")

# Saving output file in analysis folder
output_file = os.path.join("analysis", "pypoll.csv")
with open(output_file, "w", newline='')as file:
    file.write("Election Results")
    file.write("\n--------------------------------------")
    file.write(f'\nTotal Votes: {total_vote}')
    file.write("\n--------------------------------------")
    file.write(f'\nKhan: {khan_per:.3f}% ({khan_total})')
    file.write(f'\nCorrey: {correy_per:.3f}% ({correy_total})')
    file.write(f'\nLi: {li_per:.3f}% ({li_total})')
    file.write(f"\nO'Tooley:{tooley_per:.3f}% ({tooley_total})")
    file.write("\n--------------------------------------")
    file.write(f'\nwinner: {p_vote}')
    file.write("\n--------------------------------------")
