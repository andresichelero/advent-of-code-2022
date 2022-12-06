# Initialize a list to store the pairs of intervals
pairs = []

# Open the input file
with open("input.txt", "r+") as f:
    # Loop over each line in the file
    for line in f.readlines():
        # Split the line into the two intervals
        start1, end1 = map(int, line.split(",")[0].split("-"))
        start2, end2 = map(int, line.split(",")[1].split("-"))

        # Add the pairs of intervals to the list
        pairs.append((start1, end1, start2, end2))

# Initialize the count to 0
count = 0

# Loop over each pair of intervals
for (start1, end1, start2, end2) in pairs:
    # Check if the intervals overlap
    if (start1 <= start2 <= end1) or (start1 <= end2 <= end1) or (start2 <= start1 <= end2) or (start2 <= end1 <= end2):
        # If the intervals overlap, increment the count
        count += 1

# Print the count
print(count)
