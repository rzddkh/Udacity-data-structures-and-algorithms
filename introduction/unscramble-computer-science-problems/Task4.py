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


callers=set()  # list of callers   
not_telemarketer=set()    # list of call receivers, text receivers and text senders  

# calls format: ['78130 00821', '98453 94494', '01-09-2016 06:01:12', '186']
# text format: ['97424 22395', '90365 06212', '01-09-2016 06:03:22']

# find the set of numbers for callers, receivers, text senders and text receivers. substract the sets from callers would give us the possible tele marketers.


for e in calls:
        callers.add(e[0])
        not_telemarketer.add(e[1])

for e in texts:
    not_telemarketer.add(e[0])
    not_telemarketer.add(e[1])

tele_marketer=callers-not_telemarketer
tele_marketer= set(tele_marketer)
tele_marketer= list(tele_marketer)
print("These numbers could be telemarketers: ")

# sorting the list 
tele_marketer.sort()

for e in tele_marketer:
    print(e)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

