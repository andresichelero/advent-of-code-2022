import fileinput

elfs = []
iteration = 0
total = 0

# Open the input file
with fileinput.input(files=('input.txt')) as f:
    # Loop over each line in the file
    for line in f:
        # Check if the line is not empty
        if line != '\n':
            # Add the number on the line to the total
            total += int(line)
        else:
            # If the line is empty, append the total to the list of elves
            # and reset the iteration counter and total
            elfs.append(total)
            iteration += 1
            total = 0

# Sort the list of elves in ascending order
elfs.sort()

# Print the sorted list of elves
print(elfs)
