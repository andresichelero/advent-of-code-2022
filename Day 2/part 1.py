import fileinput

# Open the input file
with fileinput.input(files=('input.txt')) as f:
    # Initialize the final points to 0
    final_points = 0

    # Loop over each line in the file
    for line in f:
        # Check if the line is not empty
        if line != '\n':
            # Split the line into the player's and opponent's choices
            player_choice, opponent_choice = line.split()

            # Initialize the points for this round to 0
            points = 0

            # Check if there was a draw
            if player_choice == "A" and opponent_choice == "X" or player_choice == "B" and opponent_choice == "Y" or player_choice == "C" and opponent_choice == "Z":
                # If there was a draw, the player gets 3 points
                points += 3

                # Check if the player chose X, Y, or Z
                if opponent_choice == "X":
                    # If the player chose X, they get an additional point
                    points += 1
                elif opponent_choice == "Y":
                    # If the player chose Y, they get an additional 2 points
                    points += 2
                elif opponent_choice == "Z":
                    # If the player chose Z, they get an additional 3 points
                    points += 3
            # Check if the opponent chose rock
            elif opponent_choice == "A":
                # If the opponent chose rock, check if the player chose Y or Z
                if player_choice == "Y":
                    # If the player chose Y, they get 8 points
                    points += 8
                elif player_choice == "Z":
                    # If the player chose Z, they get 3 points
                    points += 3
            # Check if the opponent chose paper
            elif opponent_choice == "B":
                # If the opponent chose paper, check if the player chose X or Z
                if player_choice == "X":
                    # If the player chose X, they get 1 point
                    points += 1
                elif player_choice == "Z":
                    # If the player chose Z, they get 9 points
                    points += 9
            # Check if the opponent chose scissors
            elif opponent_choice == "C":
                # If the opponent chose scissors, check if the player chose X or Y
                if player_choice == "X":
                    # If the player chose X, they get 7 points
                    points += 7
                elif player_choice == "Y":
                    # If the player chose Y, they get 2 points
                    points += 2

            # Add the points for this round to the final points
            final_points += points

            # Print the final points after each round
            print(final_points)
