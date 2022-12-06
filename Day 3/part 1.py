total = 0

# Open the input file
with open("input.txt", "r+") as f:
    # Loop over each line in the file
    for line in f.readlines():
        # Split the line into a list of characters
        inside = [el for el in line.rstrip()]

        # Create two sets of characters from the first and second half of the line
        comp1 = set(inside[:len(inside)//2])
        comp2 = set(inside[len(inside)//2:])

        # Find the intersection of the two sets (i.e., the common characters)
        el = list(comp1.intersection(comp2))[0]

        # Check if the common character is uppercase or lowercase
        if el == el.upper():
            # If the character is uppercase, calculate its value as the ASCII code minus 65 plus 27
            char = ord(el) - 65 + 27
        else:
            # If the character is lowercase, calculate its value as the ASCII code minus 97 plus 1
            char = ord(el) - 97 + 1

        # Add the value of the character to the total
        total += char

    # Print the total
    print(total)
