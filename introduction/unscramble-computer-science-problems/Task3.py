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

areaCode_mobilePreFixed_no_duplciate=[]
mobile_count=0
fixedLine_count=0
fixedLine_to_bangalore=0
tele_marketer=0 # expected to be zero because they don't receive calls 
for e in calls:
  #finding incoming calls made from Bangalore
  if e[0][1:4]=='080':
    #finding mobile prefixes for calls made from Bangalore to mobile numbers
    if e[1][5]==' ':
      mobile_count+=1
      if e[1][0:4] not in areaCode_mobilePreFixed_no_duplciate:
        areaCode_mobilePreFixed_no_duplciate.append(e[1][0:4])
    #finding area codes for calls made from Bangalore to fixed lines
    elif e[1][0]=='(':
      fixedLine_count+=1
      if e[1][1:e[1].find(')')] not in areaCode_mobilePreFixed_no_duplciate:
        areaCode_mobilePreFixed_no_duplciate.append(e[1][1:e[1].find(')')])
      # calls made to a fixed line in Bangalore:
      if e[1][1:4]=='080':
         fixedLine_to_bangalore+=1
    #telemarketers if there is any
    else:
      tele_marketer+=1

print("The numbers called by people in Bangalore have codes: "+'\n')

# sorting the list:
areaCode_mobilePreFixed_no_duplciate.sort()

#printing the list:
for e in areaCode_mobilePreFixed_no_duplciate:
   print(e)

print('\n'+f"{(fixedLine_to_bangalore/(mobile_count+fixedLine_count+tele_marketer))*100:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")



"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
