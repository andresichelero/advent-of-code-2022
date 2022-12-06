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
            if opponent_choice == "Y":
                # If there was a draw, check if the player chose A, B, or C
                if player_choice == "A":
                    # If the player chose A, they get 4 points
                    points += 4
                elif player_choice == "B":
                    # If the player chose B, they get 5 points
                    points += 5
                elif player_choice == "C":
                    # If the player chose C, they get 6 points
                    points += 6
            # Check if the player won
            elif opponent_choice == "Z":
                # If the player won, check if they chose A, B, or C
                if player_choice == "A":
                    # If the player chose A, they get 8 points
                    points += 8
                elif player_choice == "B":
                    # If the player chose B, they get 9 points
                    points += 9
                elif player_choice == "C":
                    # If the player chose C, they get 7 points
                    points += 7
            # Check if the player lost
            elif opponent_choice == "X":
                # If the player lost, check if they chose A, B, or C
                if player_choice == "A":
                    # If the player chose A, they get 3 points
                    points += 3
                elif player_choice == "B":
                    # If the player chose B, they get 1 point
                    points += 1
                elif player_choice == "C":
                    # If the player chose C, they get 2 points
                    points += 2

            # Add the points for this round to the final points
            final_points += points

            # Print the final points after each round
            print(final_points)
