# Name: Chris Chausse
# Assignment: Weighted Fair Queuing
# Date: 4-14-25


#-----------EXTRACTING DATA FROM TEXT FILE AND CREATING LISTS---------------

# Reading in file contents and putting them into an array called "lines"
input_path = "Week4/inputQueue.txt"

with open(input_path, "r") as file:
    lines = file.readlines()
    
lines = [line.strip() for line in lines]


# Creating three empty lists to represent the different priority levels
premium_queue = []
standard_queue = []
economy_queue = []

# Traverse the text line by line
for line in lines:
    # Strip removes any whitespace
    # Split turns: 'S Mary' into a list: ['S', 'Mary']
    parts = line.strip().split()
    # Separating into two different lists
    priority = parts[0]
    name = parts[1]
    
    # Looping over to see what the priority is, and add to the appropriate queue
    if priority == "P":
        premium_queue.append(name)
    if priority == "S":
        standard_queue.append(name)
    if priority == "E":
        economy_queue.append(name)



#-------------PRINTING LISTS OUT ACCORDING TO PRIORITY SCHEME-----------------

print("\nDequeued Output Based on Priority:\n")

# A loop to continue until all three queues are empty
while premium_queue or standard_queue or economy_queue:
    # Try and print up to 3 Premium packets
    for _ in range(3):
        if premium_queue:
            #
            print("Premium:", premium_queue.pop(0))
    
    # Try and print up to 2 Standard packets     
    for _ in range(2):
        if standard_queue:
            print("Standard:", standard_queue.pop(0))
            
    # Try and print up to 1 Economy packet
    if economy_queue:
        print("Economy:", economy_queue.pop(0))