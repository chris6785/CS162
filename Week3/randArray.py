# Name: Chris Chausse
# Assignment: Manipulating Arrays in Python
# Date: 4-14-25

import numpy as np

#Generate a random 5x5 array of integers between 1-100
randArray = np.random.randint(1, 101, size=(5, 5), dtype=int)

# Print the 5x5 array and its contents
print("\nContents of Array:\n")

# Used for loop to print so they output looked cleaner and easier to read
for row in randArray:
    print(row)

# Value of second row, third column
print("\nValue at second row, third column:\n", randArray[1][2])

# Value of the sum of all elements in the array
print("\nSum of all array elements:\n", np.sum(randArray))

# Print the average of each row
# Did it this way just for readability and formatting rather than a simple print statement
means = np.mean(randArray, axis=1)
print("\nAverage of each row:\n", [round(val, 1) for val in means])

# Print the maximum value in each column
# Chose to do it this way for overall readability and formatting, rather than using just a print statement
col_maxes = np.max(randArray, axis=0)
print("\nMaximum of each column:\n", list(col_maxes))
print("\n")