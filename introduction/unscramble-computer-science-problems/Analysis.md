## Task0

**Description**:

**What is the first record of texts and what is the last record of calls?**

**Approach**: Since elements are ordered in ascending order in calls.csv and texts.csv the first and last record is the same as first and last index in the lists.

**Complexity Analysis**:

- **Algorithm**: Simply grabing the first and last records by index
- **Big O Notation**:

  - Time complexity is O(1).

- **Justification**: First and last element is accessed through index. Time complexity doesn't change with the number of inputs. O(1)

## Task1

**Description**:

**How many different telephone numbers are there in the records?**

**Approach**: First, declare an empty set to store the unique numbers.
add the numbers to the set of unique numbers using add fuction for sets.

**Complexity Analysis**:

- **Algorithm**: Using one for loop for texts and one for loop for calls and using set data type we can easily find unique numbers.

- **Big O Notation**:
  - Time complexity for this task is O(n)
- **Justification**:
  - $n$ is the number of elements.
  - Using for loop and adding elements to a set
  - For loop time complexity is O(n)
  - we have 2 for loops so time complexity is O(n)+O(n)=>O(n)

## Task 2

**Description**:

**Which telephone number spent the longest time on the phone
during the period?**

**Approach**:

Declare a dictionary first, run a for loop through calls list. For each element in calls, check the caller and receiver numbers agaisnt the dictionary with .get() method and add the results to the value (which is call duration). if the number doesnt exist we assign get default value to 0.

using get method on dictionary:
for each call element we add results of .get() method for that elemenet in our dictionary to the call duration.
If the phone number doesn't exist in the dictionary add it as a key and add the duration + default value for get( we assign it to be 0 in this case).

If the phone number exists simply add the call duration to the value of the key (which is the phone number).

(one for loop can does both incoming and outgoing calls in one run)

**Complexity Analysis**:

- **Algorithm**: Using 1 for loop and a dictionary (phone number as key/ call duration as value). simply add the duration to the value of the key as the numbers show up in the foor loop.
- **Big O Notation**:
  - Time complexity for this task is O(n)
- **Justification**:
  - $n$ is the number of elements.
  - For loop time complexity is O(n)
  - Dictionary time complexity is O(1)
  - we have 2 for loops and 1 dictionary so the time complexity is:
  - O(2n) + O(1) => O(n)

## Task3

**Description**:

**A. Find all of the area codes and mobile prefixes called by people in Bangalore.**

**B. What percentage of calls from fixed lines in Bangalore are made to fixed lines also in Bangalore?**

**Approach**: Using one for loop to go through calls, if the out going call starts with 080 then we check to see if the outgoing call has a ' ' or '('. If any of the conditions met we simply add the reciving phone number to a set.

**Complexity Analysis**:

- **Algorithm**: Using 1 for loop and a dictionary (phone number as keys and call duration as values). Simply add the duration to the value of the key as the numbers shows up in the for loop. Sort the final list and print
- **Big O Notation**:

  - Time complexity for this task is O(n log n).

- **Justification**:

  - $n$ is the number of elements.
  - Time complexity for sorting using .sort() is O(n log n)
  - Time complexity of a for loop is O(n).
  - The time complexity for this task is:
  - O(2n) + O(n log n) => O(n log n)

## Task4

**Description**:

Create a set of possible telemarketers:
These are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

**Approach**: Using a 2 for loop, create 4 sets for phone numbers doing following actions: outgoing calls, receiving calls, sending text and receiving text. Now we simply substract receivers, test senders and text receivers from callers.

**Complexity Analysis**:

- **Algorithm**: finding the sets for each category: callers, receivers, texters and text receiver. Then substract receivers, texters and text receiver sets from callers set using - operator.

- **Big O Notation**:

  - Time complexity for this task is O(n log n).

- **Justification**:
  - $n$ is the number of elements.
  - Time complexity for sorting using .sort() is O(n log n)
  - Time complexity of a for loop is O(n).
  - The time complexity for this task is O(3n) + O(n log n) => O(n log n)
