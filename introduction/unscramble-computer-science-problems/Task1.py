"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
#print(texts)
unique_numbers=[]
for e in texts:
    if(e[0] not in unique_numbers):
        unique_numbers.append(e[0])
    if(e[1] not in unique_numbers):
        unique_numbers.append(e[1])

for e in calls:
    if(e[0] not in unique_numbers):
        unique_numbers.append(e[0])
    if(e[1] not in unique_numbers):
        unique_numbers.append(e[1])
        
print(f"There are {len(unique_numbers)} different telephone numbers in the records.")