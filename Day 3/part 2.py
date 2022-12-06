# Initialize the set of common characters to an empty set
common = set()
elves = 0
sum = 0

# Open the input file
with open("input.txt", "r+") as f:
    # Loop over each line in the file
    for line in f.readlines():
        # Increment the number of elves
        elves += 1

        # Create a set of characters from the line
        carry = set([el for el in line.rstrip()])

        # If this is the first elf, set the common characters to the characters in their line
        common = carry if elves % 3 == 1 else common.intersection(carry)

        # If this is the third elf, find the common character and calculate its value
        if elves % 3 == 0:
            # Find the common character
            badge = list(common)[0]

            # Reset the common characters to an empty set
            common = set()

            # Check if the common character is uppercase or lowercase
            if badge == badge.upper():
                # If the character is uppercase, calculate its value as the ASCII code minus 65 plus 27
                p = ord(badge) - 65 + 27
            else:
                # If the character is lowercase, calculate its value as the ASCII code minus 97 plus 1
                p = ord(badge) - 97 + 1

            # Add the value of the common character to the total
            sum += p

    # Print the total
    print(sum)
