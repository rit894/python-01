Input:
A string originalMSG entered by the user

Output:
A transformed string corruptMSG where:

Lowercase letters become uppercase

Uppercase letters become lowercase

Non-alphabetic characters remain unchanged

Percentage of characters that were flipped (i.e., corrupted)

Steps:
Initialize Variables:

corruptMSG ← "" (empty string to store transformed message)

corruptCount ← 0 (counter for flipped characters)

totalCount ← 0 (counter for all characters)

Read Input:

Prompt user to enter a message → originalMSG ← input(...)

Iterate Through Each Character in originalMSG:

For each char in originalMSG:

If char is a lowercase letter (a to z):

Convert to uppercase using ASCII logic: chr(ord(char) - 32)

Append to corruptMSG

Increment corruptCount and totalCount

Else if char is an uppercase letter (A to Z):

Convert to lowercase using ASCII logic: chr(ord(char) + 32)

Append to corruptMSG

Increment corruptCount and totalCount

Else:

Append char unchanged to corruptMSG

Increment totalCount

Display Transformed Message:

Print "The CORRUPT message is: " + corruptMSG

Calculate Corruption Percentage:

percentCorrupt ← (corruptCount / totalCount) × 100

Round to 2 decimal places

Display Corruption Percentage:

Print "The corruption percentage is: " + percentCorrupt + "%"