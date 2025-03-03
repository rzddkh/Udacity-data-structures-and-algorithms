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
receivers=set()    # list of receivers 
not_receiving_calls=set() #list of numbers not receiving calls 
receive_text=set() #list of numbers receiving text
send_text=set() #list fo numbers sending text
no_text=set()  #not sending or receiving text

# calls format: ['78130 00821', '98453 94494', '01-09-2016 06:01:12', '186']
# text format: ['97424 22395', '90365 06212', '01-09-2016 06:03:22']

# find the set of numbers for callers, receivers, text senders and text receivers. substract the sets from callers would give us the possible tele marketers.


for e in calls:
        callers.add(e[0])
        receivers.add(e[1])

for e in texts:
    send_text.add(e[0])
    receive_text.add(e[1])

tele_marketer=callers-send_text-receive_text-receivers
tele_marketer= set(tele_marketer)
tele_marketer= list(tele_marketer)
print("These numbers could be telemarketers: ")

# sorting the list 
tele_marketer.sort()

for e in tele_marketer:
    print(e)
print (len(tele_marketer))
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

