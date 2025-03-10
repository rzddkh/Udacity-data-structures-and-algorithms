"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
numbers={} # declare dict numbers 

for e in calls:
    numbers[e[0]]=numbers.get(e[0],0)+int(e[3])
    numbers[e[1]]=numbers.get(e[1],0)+int(e[3])


print(f"{max(numbers,key=numbers.get)} spent the longest time, {numbers[max(numbers,key=numbers.get)]} seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

