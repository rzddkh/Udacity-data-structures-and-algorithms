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

callers=[]  # list of callers   
receivers=[]    # list of receivers 
not_receiving_calls=[] #list of numbers not receiving calls 
receive_text=[] #list of numbers receiving text
send_text=[] #list fo numbers sending text
no_text=[]  #not sending or receiving text

# calls format: ['78130 00821', '98453 94494', '01-09-2016 06:01:12', '186']
# text format: ['97424 22395', '90365 06212', '01-09-2016 06:03:22']

# find the list of numbers that are recieving calls and compare it to the ones making the calls 

for e in calls:
        callers.append(e[0])
        receivers.append(e[1])

for number in callers:
    if (number not in receivers):
        not_receiving_calls.append(number)

for e in texts:
    send_text.append(texts[0])
    receive_text.append(texts[1])

for number in callers:
    if number not in send_text:
        no_text.append(number)
for number in callers:
    if number not in receive_text:
        no_text.append(number)

tele_marketer=not_receiving_calls+no_text
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

